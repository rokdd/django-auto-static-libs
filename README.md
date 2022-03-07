[![PyPI version](https://badge.fury.io/py/django-auto-static-libs.svg)](https://badge.fury.io/py/django-auto-static-libs)

# Idea

Provide basic libraries and resources like jQuery or semantic-ui in django applications. Make it easier for keeping them updated and self-hosted. 

# Installation

You can install the package with pip:

```bash
pip install django-auto-static-libs
```

Afterwards add `'django_auto_static_libs'` after `'django.contrib.staticfiles'` to INSTALLED_APPS in
your settings.py:

```python
INSTALLED_APPS = (
# ...
'django.contrib.staticfiles',
'django_auto_static_libs',
# ...
)
```

# Usage

In your templates add depending on the library and how you named the folder:
```html
{% load static %}
<script src="{% static 'latest-auto-static-libs/jquery/jquery.min.js' %}" type="text/javascript"></script>
```

You must run the downloading at the beginning (or to update). It will run automatically at migration:
```python
python manage.py migrate
#or as command
python manage.py static-libs-download
```

# Configuration

## Manage libraries
Currently it supports the following libraries (bold is the name of the corresponding configuration):

* **jquery**: jQuery from github
* **jquery_ui**: [jQuery UI](https://jqueryui.com/) from their website
* **jquery_mobile**: [jQuery mobile](https://jquerymobile.com/) from their website
* **bootstrap**: [bootstrap](https://getbootstrap.com)Javascript helper functions for pygal from their website
* **fontawesome**: [Fontawesome](https://fontawesome.com) from github
* **fomantic_ui**: [Fomantic-UI](https://fomantic-ui.com/) from github (fork of semantic UI)
* **semantic_ui**: [Semantic-UI](https://semantic-ui.com/) from github
* **masonry**: [Masonry](https://masonry.desandro.com/) from github
* **pygal_js**: [pygal.js](https://github.com/Kozea/pygal.js/) Javascript helper functions for pygal from github
* **initter_js**: [initter.js](https://github.com/rokdd/initter-js/) Javascript conditioner for initiating from github

Is your favorite or own library missing? Just drop as an issue or even better a PR that we can integrate your library.

In your settings.py:
```python
#some imports
from django_auto_static_libs.libraries import jquery
DJANGO_AUTO_STATIC_LIBS = {
#The default is the jquery library. If you add other or custom libraries it will replace the default. it need always to be a dict, the key represents your folder and will be needed for the static import
    'libraries': {
        'jquery': jquery,
        'custom_full': {
            'provider' : GithubProvider("jquery/jquery"),
            'suffix_ignore': [".json"],
            'files_include': r"jquery-[\d\.]+/dist/(.*\.(js|map))",
            #auto creates in your static root a folder "latest_static_libs". If you change this default path be careful in the templates
            'destination': "auto",
        }
    },
    'destination_folder': 'django-auto-static-libs'
}
```
## Add your custom library

You can add your own library as a dict into the config. Please submit your configurations by pull request or issue that it can be added for everyone.

| Property          | Value                  | Example                                 | Description                                                                                                      |
|-------------------|------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------|
| **provider**      | object of BaseProvider | ```GithubProvider("jquery/jquery")```   | Take github class as example, it gives access to the files                                                       |
| **files_include** | regex as str           | ```[".json"]```                         | regex to include file or dir when extracting / downloading (the first matching group defines the path of folder) |
| **suffix_ignore** | list                   | ```r"jquery-[\d\.]+/dist/(.*\.(js))"``` | list of suffixes to exclude when extracting / downloading                                                        |
| **destination**   | str                    | ```"auto"```                            | Future releases to define path                                                                                   |


# Future features

* templates for include in header and footer
* add more libraries for downloading
* new command: list of all libraries
* remember the currently installed version
* improve logging / no prints
* testing
