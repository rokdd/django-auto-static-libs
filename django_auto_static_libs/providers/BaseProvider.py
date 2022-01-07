import requests,re
from django.core.exceptions import ImproperlyConfigured

class BaseProvider:
	def download(self):
		pass

#download files from multiple urls
class SingleUrlProvider(BaseProvider):
	def __init__(self, urls):
		self.urls = urls

	def download(self):
		files = []
		for url in self.urls:
			r = requests.get(url, allow_redirects=True)

			# we got not a valid answer of a file:
			if not r.ok or r.content is None:
				continue
			files.append(r)
		if files == []:
			return None
		return files

#extract a url by the title of a tag of a given webpage
class SingleUrlByExtractProvider(SingleUrlProvider):
	def __init__(self, url,words=None,regex=None):
		self.url = url
		#when either words or regex set:
		if words is None and regex is None:
			raise ImproperlyConfigured("Django-auto-static-libs/"+self.__name__+" needs either words= or regex= argument")
		if regex is not None:
			self.regex=regex
		else:
			#generate regex
			self.regex=r'href="(?P<url>.*)".*?>'+"".join([r'(?=.*\b%s\b)'%x for x in words])+'.+</a>'

	def download(self):
		r = requests.get(self.url,allow_redirects=True)
		match_results = re.search(self.regex, r.text, re.IGNORECASE)
		url= match_results.group("url")
		if url is None:
			return None
		else:
			self.urls=[url]
		return super().download()