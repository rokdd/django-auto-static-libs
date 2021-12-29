from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import requests, zipfile, io
import os, re, pathlib, errno
from django.conf import settings
from django_static_libs.libraries import jquery


class Command(BaseCommand):
	help = 'Download library from their sources'

	default_settings = {"libraries": {
		'jquery': jquery
	}
	}
	settings = default_settings

	#   def add_arguments(self, parser):
	#       parser.add_argument('total', type=int, help='Indicates the number of users to be created')

	def handle_file(self, k, lib, folder, zip_info, zfile=None):
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
		if hasattr(settings, "DJANGO_STATIC_LIBS"):
			# replace the libraries when set
			if "libraries" in settings["DJANGO_STATIC_LIBS"]:
				self.settings["libraries"] = settings["DJANGO_STATIC_LIBS"]["libraries"]

		for k, lib in self.settings["libraries"].items():
			print('Download and update static lib "%s"' % (k))

			if not "provider" in lib:
				print("Could not find type of library")
				continue
			if not "destination" in lib or lib["destination"] == "auto":
				lib["destination"] = os.path.join(settings.STATIC_ROOT, "latest_static_libs", "%s" % (lib['syntax']))
			else:
				print("Currently only auto path is support")

			r = lib["provider"].download()
			# only continue when there is data
			if r is not None:
				if r.headers.get('content-type') == "application/zip":
					z = zipfile.ZipFile(io.BytesIO(r.content))
					for zip_info in z.infolist():
						self.handle_file(k, lib, folder, zip_info, zfile=z)
				else:
					print("Currently non zip files are not supported yet")
			else:
				print("Could not download library: %s" % (k))

	print("Run collect static")

	call_command('collectstatic', verbosity=1, interactive=False)
