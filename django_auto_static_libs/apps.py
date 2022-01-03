# -*- coding: utf-8 -*-
from django.apps import AppConfig
import sys
from django.core import management


class AutoStaticLibsConfig(AppConfig):
	name = 'django_auto_static_libs'
	verbose_name = 'Django auto static lib updater'

	def ready(self):
		pass
		if 'manage.py' in sys.argv and "migrate" in sys.argv and len(sys.argv) == 2:
			management.call_command('static-libs-download', verbosity=0, interactive=False)