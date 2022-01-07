from django_auto_static_libs.libraries import jquery,fomantic_ui,masonry,pygal_js,bootstrap,jquery_ui
from django_auto_static_libs.providers.BaseProvider import SingleUrlProvider,SingleUrlByExtractProvider


DJANGO_AUTO_STATIC_LIBS = { 'libraries': {
            'jquery':jquery,
			'jquery-ui':jquery_ui,
            'fomantic-ui':fomantic_ui,
            'masonry':masonry,
            'pygal-js':pygal_js,
			'bootstrap':bootstrap,
            }
}