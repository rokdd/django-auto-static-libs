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

### Usage

In your templates add:
```
{% load static %}
<script src="{% static 'latest_static_libs/js/jquery/jquery.min.js' %}" type="text/javascript"></script>
```

You must run the downloading at the beginning (and to update again):
```
python manage.py static-libs-download
```

### Configuration

Currently we support following libraries:


In your settings.py:
```
#some imports
from django_static_libs.libraries import jquery
DJANGO_STATIC_LIBS = {
#The default is the jquery library. If you add other or custom libraries it will replace the default. it need always to be a dict
'libraries': { 
            'jquery':jquery,
            
            'custom_full':
                {
                'provider' : GithubProvider("jquery/jquery"),
			    'suffix_ignore': [".json"],
			    'syntax': 'js',
			    'files_include': r"jquery-[\d\.]+/dist/.*\.(js|map)",
			    #auto creates in your static root a folder "latest_static_libs". If you change this default path be careful in the templates
			    'destination':"auto",
                }
            }
}
```


### Future features

* own folder in static
* add other librarys for downloading
* improve process of downloading for other librarys
* at install is always a old version of the librarys?
* list of all librarys as command
* remember the currently installed version
* better error handling for download
* testing