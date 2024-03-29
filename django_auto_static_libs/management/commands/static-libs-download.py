from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import requests, zipfile, io
from pathlib import Path
import os, re, pathlib, errno
from django_auto_static_libs import settings



class Command(BaseCommand):
	help = 'Download library from their sources'

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
			os.makedirs(os.path.join(folder, Path(zip_info.filename).parent))
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
				lib["destination"] = settings.DESTINATION_ROOT
			else:
				print("Currently only auto path is support as destination")
				#>> > variables = {"publication": "article", "author": "Me"}
				#template.format(**variables)

			r = lib["provider"].download()

			# only continue when there are files
			if r is not None:
				# make sure that we iterate over a list
				if not r is list:
					r=list(r)

				for rfile in r:
					z = None

					# some work on the url to detect the correct filetype later:
					if isinstance(rfile,requests.Response) and hasattr(rfile.headers,"Content-Disposition") and "filename" in getattr(rfile.headers,"Content-Disposition"):
						url=getattr(rfile.headers,"Content-Disposition").split("filename=")[1]
					else:
						url=rfile.url

					# when zip extract it directly
					if isinstance(rfile,requests.Response) and (rfile.headers.get('content-type') == "application/zip" or '.zip' in url):
						z = zipfile.ZipFile(io.BytesIO(rfile.content))
					elif isinstance(rfile,requests.Response):
						#create empty temporary zip file if z not yet exists
						if z is None:
							bytes_zip_buffer = io.BytesIO(b'PK\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
							z = zipfile.ZipFile(bytes_zip_buffer, "a", zipfile.ZIP_DEFLATED, False)

						z.writestr(os.path.basename(url),rfile.content)
					else:
						print("Currently the files or method to download is not supported yet",rfile)
					if z is not None:
						for zip_info in z.infolist():
							self.handle_file(k, lib, lib["destination"] , zip_info, zfile=z)

			else:
				print("Could not download library: %s" % (k))

	#print("Run collect static")

	#call_command('collectstatic', verbosity=1, interactive=False)
