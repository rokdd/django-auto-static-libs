from BaseProvider import BaseProvider

class GithubProvider(BaseProvider):
    def __init__(self,repo):
        self.repo=repo