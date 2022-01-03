from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
from django_auto_static_libs.libraries import jquery

DJANGO_AUTO_STATIC_LIBS=getattr(django_settings,"DJANGO_AUTO_STATIC_LIBS",{"libraries": {
		'jquery': jquery
	}
	})
