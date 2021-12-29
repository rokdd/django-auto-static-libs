from django_static_libs.providers.BaseProvider import BaseProvider


class GithubProvider(BaseProvider):
    def __init__(self, repo):
        self.repo = repo
