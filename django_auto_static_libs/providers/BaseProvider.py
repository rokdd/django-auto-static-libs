import requests


class BaseProvider:
	def download(self):
		pass


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
