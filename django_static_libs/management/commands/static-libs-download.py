from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import requests, zipfile, io
import os,re,pathlib,errno
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
			'files_include':r"jquery-[\d\\.]+/dist/.*\\.(js|map)",
		}
	}

	#   def add_arguments(self, parser):
	#       parser.add_argument('total', type=int, help='Indicates the number of users to be created')

	def handle_file(self,pkg,folder,zip_info,zfile=None):
		if not re.match(pkg['files_include'], zip_info.filename):
			print("Not extracted "+os.path.basename(zip_info.filename)+': Not matching include rule')
			return False
		if pathlib.Path(zip_info.filename).suffix in pkg['suffix_ignore']:
			print("Not extracted " + os.path.basename(zip_info.filename) + ': Suffix matches exclude rule')
			return False

		#now if we think that we accept this file we check that we create the dirs for the file
		try:
			os.makedirs(folder)
		except OSError as e:
			if e.errno != errno.EEXIST:
				print("Could not create folder "+folder)
				return

		zip_info.filename = "%s/%s" % (str(k), os.path.basename(zip_info.filename))

		zfile.extract(zip_info, folder)
		if os.path.isfile(os.path.join(folder, zip_info.filename)):
			print(
				"Extracted " + os.path.basename(zip_info.filename) + ' into ' + os.path.join(folder, zip_info.filename))
		else:
			print("Could not extract " + os.path.basename(zip_info.filename) + ' into ' + os.path.join(folder,zip_info.filename))

	def handle(self, *args, **kwargs):
		#total = kwargs['total']

		for k,pkg in self.default_librarys.items():
			print('Download and update static lib "%s"' % (k))
			#reset request
			r=None
			if 'github_repo' in pkg:
				response = requests.get("https://api.github.com/repos/%s/releases/latest" % (pkg['github_repo']),allow_redirects=True)
				folder = os.path.join(settings.STATIC_ROOT,"latest_static_libs","%s"%(pkg['syntax']))
				r = requests.get("https://github.com/%s/archive/refs/tags/%s.zip" % (pkg['github_repo'],response.json()["tag_name"]),allow_redirects=True)
			#only continue when there is data
			if r is not None and r.ok and r.content is not None:
				z = zipfile.ZipFile(io.BytesIO(r.content))
				for zip_info in z.infolist():
					self.handle_file(pkg,folder,zip_info,zfile=z)
			elif r is None:
				print("Could not find type of library")
			else:
				print("Could not download library: "+"https://github.com/%s/archive/refs/tags/%s.zip" % (pkg['github_repo'],response.json()["tag_name"]))

		print("Run collect static")
		

		call_command('collectstatic', verbosity=0, interactive=False)