from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured
from django_auto_static_libs.libraries import jquery
import os

DJANGO_AUTO_STATIC_LIBS = dict(libraries={
	'jquery': jquery
}, destination_folder='django-auto-static-libs')

if hasattr(django_settings, "DJANGO_AUTO_STATIC_LIBS"):
	if 'libraries' in getattr(django_settings, "DJANGO_AUTO_STATIC_LIBS"):
		DJANGO_AUTO_STATIC_LIBS['libraries'] = getattr(django_settings, "DJANGO_AUTO_STATIC_LIBS")['libraries']
	DJANGO_AUTO_STATIC_LIBS = {**DJANGO_AUTO_STATIC_LIBS, **getattr(django_settings, "DJANGO_AUTO_STATIC_LIBS")}

# check whether the folder is a proper path
if not os.path.isabs(DJANGO_AUTO_STATIC_LIBS['destination_folder']):
	if not hasattr(django_settings, "STATIC_ROOT"):
		raise ImproperlyConfigured("Django-auto-static-libs needs STATIC_ROOT in settings.py")
	STATIC_ROOT = getattr(django_settings, "STATIC_ROOT")
	DESTINATION_ROOT=os.path.join(STATIC_ROOT,DJANGO_AUTO_STATIC_LIBS['destination_folder'])
else:
	DESTINATION_ROOT=DJANGO_AUTO_STATIC_LIBS['destination_folder']
