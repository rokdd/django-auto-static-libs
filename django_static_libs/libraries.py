from django_static_libs.providers.GithubProvider import GithubProvider

jquery = {
	'provider': GithubProvider("jquery/jquery"),
	'suffix_ignore': [".json"],
	'syntax': 'js',
	'files_include': r"jquery-[\d\.]+/dist/.*\.(js|map)",
	'destination': "auto",
}

default = {
	'suffix_ignore': [],
	'files_include': '.*',
	'destination': "auto",
}
