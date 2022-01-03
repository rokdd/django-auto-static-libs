from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured

DJANGO_AUTO_STATIC_LIBS=getattr(django_settings,"DJANGO_AUTO_STATIC_LIBS",{"libraries": {
		'jquery': jquery
	}
	})
