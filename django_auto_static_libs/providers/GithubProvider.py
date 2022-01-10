from django_auto_static_libs.providers.BaseProvider import BaseProvider
import requests, zipfile, io
import os, re, pathlib, errno

class GithubProvider(BaseProvider):
    def __init__(self, repo,file="response_json[tag_name].zip"):
        self.repo = repo
        self.file=file
    def download(self):
        response = requests.get("https://api.github.com/repos/%s/releases/latest" % (self.repo),
                                allow_redirects=True)
        #to use in format of string
        response_json=response.json()
        r = requests.get("https://github.com/%s/archive/refs/tags/%s" % (
            self.repo, self.file.format(**locals())), allow_redirects=True)

        #we got not a valid answer of a file:
        if not r.ok or r.content is None:
            return None
        
        return [r]


