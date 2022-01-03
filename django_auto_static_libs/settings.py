from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
from django_auto_static_libs.libraries import jquery

if not hasattr(django_settings,"STATIC_ROOT"):
	raise ImproperlyConfigured("Django-auto-static-libs needs STATIC_ROOT in settings.py")
STATIC_ROOT=getattr(django_settings,"STATIC_ROOT")

DJANGO_AUTO_STATIC_LIBS=getattr(django_settings,"DJANGO_AUTO_STATIC_LIBS",{"libraries": {
		'jquery': jquery
	}
	})
