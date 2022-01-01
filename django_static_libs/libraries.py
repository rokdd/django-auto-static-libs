from django_static_libs.providers.GithubProvider import GithubProvider

default = {
	'suffix_ignore': [],
	'files_include': '.*',
	'destination': "auto",
}

jquery = {
	'provider': GithubProvider("jquery/jquery"),
	'suffix_ignore': [".json"],
	'files_include': r"jquery-[\d\.]+/dist/.*\.(js|map)",
	'destination': "auto",
}
fomantic_ui = {
	'provider': GithubProvider("fomantic/Fomantic-UI"),
	'suffix_ignore': [".json"],
	'files_include': r"fomantic-[\d\.]+/dist/.*",
	'destination': "auto",
}
