## Installation

For the moment you can install the package with:

´´´
pip install -e git+https://github.com/rokdd/django-static-libs.git#egg=django-static-libs
´´´

Afterwards add ``'django_static_libs'`` after ``'django.contrib.staticfiles'`` to INSTALLED_APPS in
your settings.py:
´´´
   INSTALLED_APPS = (
        # ...

        'django.contrib.staticfiles',
        'django_static_libs',

        # ...
    )
´´´


### How to use

´´´
    {% load staticfiles %}
    {% static 'static_libs/js/jquery.js' %}
´´´