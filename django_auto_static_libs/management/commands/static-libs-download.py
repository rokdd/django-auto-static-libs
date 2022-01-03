from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import requests, zipfile, io
from pathlib import Path
import os, re, pathlib, errno
from django_auto_static_libs import settings
from django_auto_static_libs.libraries import jquery


class Command(BaseCommand):
	help = 'Download library from their sources'

	#   def add_arguments(self, parser):
	#       parser.add_argument('total', type=int, help='Indicates the number of users to be created')

	def handle_file(self, k, lib, folder, zip_info, zfile=None):
		mt=re.match(lib['files_include'], zip_info.filename)
		if not mt:
			print("Not extracted " + zip_info.filename + ': Not matching include rule')
			return False
		if pathlib.Path(zip_info.filename).suffix in lib['suffix_ignore']:
			print("Not extracted " + zip_info.filename + ': Suffix matches exclude rule')
			return False

		zip_info.filename = "%s/%s" % (str(k), mt.group(1))
		#os.path.basename(zip_info.filename)
		#
		try:
			os.makedirs(Path(zip_info.filename).parent)
		except OSError as e:
			if e.errno != errno.EEXIST:
				print("Could not create folder " + folder)
				return

		zfile.extract(zip_info, folder)
		if os.path.isfile(os.path.join(folder, zip_info.filename)):
			print(
				"Extracted " + os.path.basename(zip_info.filename) + ' into ' + os.path.join(folder, zip_info.filename))
		else:
			print("Could not extract " + os.path.basename(zip_info.filename) + ' into ' + os.path.join(folder,
			                                                                                           zip_info.filename))

	def handle(self, *args, **kwargs):
		# total = kwargs['total']

		for k, lib in getattr(settings,"DJANGO_AUTO_STATIC_LIBS")["libraries"].items():
			print('Download and update static lib "%s"' % (k))

			if not "provider" in lib:
				print("Could not find type of library")
				continue
			if not "destination" in lib or lib["destination"] == "auto":
				lib["destination"] = os.path.join(settings.STATIC_ROOT, "latest_auto_static_libs")
			else:
				print("Currently only auto path is support as destination")
				#>> > variables = {"publication": "article", "author": "Me"}
				#template.format(**variables)

			r = lib["provider"].download()
			# only continue when there is data
			if r is not None:
				if r.headers.get('content-type') == "application/zip":
					z = zipfile.ZipFile(io.BytesIO(r.content))
					for zip_info in z.infolist():
						self.handle_file(k, lib, lib["destination"] , zip_info, zfile=z)
				else:
					print("Currently non zip files are not supported yet")
			else:
				print("Could not download library: %s" % (k))

	#print("Run collect static")

	#call_command('collectstatic', verbosity=1, interactive=False)
