from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import requests, zipfile, io
import os, re, pathlib, errno
from django.conf import settings
from django_static_libs.providers.GithubProvider import GithubProvider

class Command(BaseCommand):
	help = 'Download library from their sources'

	default_library = {
		'suffix_ignore': [],
		'files_include': '.*'
	}
	default_librarys = {
		'jquery': {
			'github_repo': "jquery/jquery",
			'provider' : GithubProvider("jquery/jquery"),
			'suffix_ignore': [".json"],
			'syntax': 'js',
			'files_include': r"jquery-[\d\.]+/dist/.*\.(js|map)",
		}
	}

	#   def add_arguments(self, parser):
	#       parser.add_argument('total', type=int, help='Indicates the number of users to be created')

	def handle_file(self,k, lib, folder, zip_info, zfile=None):
		if not re.match(lib['files_include'], zip_info.filename):
			print("Not extracted " + zip_info.filename + ': Not matching include rule')
			return False
		if pathlib.Path(zip_info.filename).suffix in lib['suffix_ignore']:
			print("Not extracted " + zip_info.filename + ': Suffix matches exclude rule')
			return False

		# now if we think that we accept this file we check that we create the dirs for the file
		try:
			os.makedirs(folder)
		except OSError as e:
			if e.errno != errno.EEXIST:
				print("Could not create folder " + folder)
				return

		zip_info.filename = "%s/%s" % (str(k), os.path.basename(zip_info.filename))

		zfile.extract(zip_info, folder)
		if os.path.isfile(os.path.join(folder, zip_info.filename)):
			print(
				"Extracted " + os.path.basename(zip_info.filename) + ' into ' + os.path.join(folder, zip_info.filename))
		else:
			print("Could not extract " + os.path.basename(zip_info.filename) + ' into ' + os.path.join(folder,
			                                                                                           zip_info.filename))

	def handle(self, *args, **kwargs):
		# total = kwargs['total']

		for k, lib in self.default_librarys.items():
			print('Download and update static lib "%s"' % (k))

			folder = os.path.join(settings.STATIC_ROOT, "latest_static_libs", "%s" % (lib['syntax']))

			r=lib["provider"].download()
			# only continue when there is data
			if r is not None:
				z = zipfile.ZipFile(io.BytesIO(r.content))
				for zip_info in z.infolist():
					self.handle_file(k,lib, folder, zip_info, zfile=z)
			elif r is None:
				print("Could not find type of library")
			else:
				print("Could not download library: %s" % (lib['github_repo']))

	print("Run collect static")

	call_command('collectstatic', verbosity=0, interactive=False)

	print("Finished")
