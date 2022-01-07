from django_auto_static_libs.providers.GithubProvider import GithubProvider
from django_auto_static_libs.providers.BaseProvider import SingleUrlProvider,SingleUrlByExtractProvider
default = {
	'suffix_ignore': [],
	'files_include': '(.*)',
	'destination': "auto",
}

jquery = {
	'provider': GithubProvider("jquery/jquery"),
	'suffix_ignore': [".json"],
	'files_include': r"jquery-[\d\.]+/dist/(.*\.(js|map))",
	'destination': "auto",
}
jquery_ui = {
	'provider': SingleUrlByExtractProvider("https://jqueryui.com/",regex=r'href="(?P<url>.*)".*class="button".*>(?=.*\bstable\b).+</a>'),
	'suffix_ignore': [""],
	'files_include': r"jquery-ui-[\d\.]+/(.*)",
	'destination': "auto",
}
fomantic_ui = {
	'provider': GithubProvider("fomantic/Fomantic-UI"),
	'suffix_ignore': [".json"],
	'files_include': r"Fomantic-UI-[\d\.]+/dist/(.*)",
	'destination': "auto",
}
semantic_ui = {
	'provider': GithubProvider("Semantic-Org/Semantic-UI"),
	'suffix_ignore': [".json"],
	'files_include': r"Semantic-UI-[\d\.]+/dist/(.*)",
	'destination': "auto",
}
masonry = {
	'provider': GithubProvider("desandro/masonry"),
	'suffix_ignore': [],
	'files_include': r"masonry-[\d\.]+/dist/(.*)",
	'destination': "auto",
}
pygal_js = {
	'provider': SingleUrlProvider(
		["https://raw.githubusercontent.com/Kozea/pygal.js/gh-pages/javascripts/pygal-tooltips.js",
		 "https://raw.githubusercontent.com/Kozea/pygal.js/gh-pages/javascripts/svg.jquery.js"]),
	'suffix_ignore': [],
	'files_include': '(.*)',
	'destination': "auto",
}
bootstrap={
    'provider':SingleUrlByExtractProvider("https://github.com/twbs/bootstrap",words=["download","latest","release"]),
	'suffix_ignore': [],
	'files_include': 'bootstrap-.*/dist/(.*)',
	'destination': "auto",
}