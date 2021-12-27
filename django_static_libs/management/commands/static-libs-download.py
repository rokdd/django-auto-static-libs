from django.core.management.base import BaseCommand, CommandError
import requests, zipfile, io
import os
import pathlib


class Command(BaseCommand):
    help = 'Download packages'

    default_package={
        'ext_ignore':[]
    }
    default_packages={
        'jquery':{
            'github_repo':"jquery/jquery",
            'ext_ignore' : [".json"],
            'syntax':'js'
        }
    }

	#   def add_arguments(self, parser):
	#       parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        #total = kwargs['total']

        for k,pkg in self.default_packages.items():

            response = requests.get("https://api.github.com/repos/%s/releases/latest" % (pkg['github_repo']))
            #print(response.json()["tag_name"])

            r = requests.get("https://github.com/%s/archive/refs/tags/%s.zip" % (pkg['github_repo'],response.json()["tag_name"]))
            z = zipfile.ZipFile(io.BytesIO(r.content))
            top_folder=z.namelist()[0]

            for zip_info in z.infolist():
                if not (zip_info.filename.startswith(top_folder+'dist/') and not pathlib.Path(zip_info.filename).suffix in pkg['ext_ignore']):
                    continue
                zip_info.filename = os.path.join(STATIC_ROOT,"static_libs","%s/%s/%s"%(pkg['syntax'],str(k),os.path.basename(zip_info.filename)))

                z.extract(zip_info,"")



#hello=Command()
#hello.handle()