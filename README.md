## Installation

For the moment you can install the package with:

```
pip install -e git+https://github.com/rokdd/django-static-libs.git#egg=django-static-libs
```

Afterwards add ``'django_static_libs'`` after ``'django.contrib.staticfiles'`` to INSTALLED_APPS in
your settings.py:
```
   INSTALLED_APPS = (
        # ...

        'django.contrib.staticfiles',
        'django_static_libs',

        # ...
    )
```


### How to use

```
    {% load staticfiles %}
    {% static 'static_libs/js/jquery.js' %}
```

### Future features

* add other librarys for downloading
* custom librarys to add
* improve process of downloading for other librarys
* at install is always a old version of the librarys?
* list of all librarys as command
* remember the currently installed version
* better error handling for download
* testing