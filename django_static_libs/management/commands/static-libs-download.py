from django.core.management.base import BaseCommand, CommandError
import requests, zipfile, io
import os,re,pathlib
from django.conf import settings

class Command(BaseCommand):
	help = 'Download librarys'

	default_library={
		'suffix_ignore':[],
		'files_include':'.*'
	}
	default_librarys={
		'jquery':{
			'github_repo':"jquery/jquery",
			'suffix_ignore' : [".json"],
			'syntax':'js',
			'files_include':r"jquery-[\d\\.]+/dist/.*",
		}
	}

	#   def add_arguments(self, parser):
	#       parser.add_argument('total', type=int, help='Indicates the number of users to be created')

	def handle(self, *args, **kwargs):
		#total = kwargs['total']

		for k,pkg in self.default_librarys.items():
			print('Download and update static lib "%s"' % (k))

			response = requests.get("https://api.github.com/repos/%s/releases/latest" % (pkg['github_repo']))
			#print(response.json()["tag_name"])

			r = requests.get("https://github.com/%s/archive/refs/tags/%s.zip" % (pkg['github_repo'],response.json()["tag_name"]))
			z = zipfile.ZipFile(io.BytesIO(r.content))
			top_folder=z.namelist()[0]

			for zip_info in z.infolist():
				if not re.match(pkg['files_include'],zip_info.filename) or pathlib.Path(zip_info.filename).suffix in pkg['suffix_ignore']:
					continue
				folder = os.path.join(settings.STATIC_ROOT,"static_libs","%s"%(pkg['syntax']))
				zip_info.filename = "%s/%s"%(str(k),os.path.basename(zip_info.filename))

				z.extract(zip_info,folder)
				if os.path.isfile(os.path.join(folder,zip_info.filename)):
					print("Extracted "+os.path.basename(zip_info.filename)+' into '+os.path.join(folder,zip_info.filename))
				else:
					print("Could not extract "+os.path.basename(zip_info.filename)+' into '+os.path.join(folder,zip_info.filename))



#hello=Command()
#hello.handle()