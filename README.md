## Idea

Provide basic libraries and resources like jQuery or semantic-ui in django applications. Make it easier for keeping them updated and self-hosted. 

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

#### Manage libraries
Currently it supports the following libraries (bold is the name of the corresponding configuration):

* **jquery**: jQuery from github
* **fomantic_ui**: [Fomantic-UI](https://fomantic-ui.com/) from github (fork of semantic UI)
* **semantic_ui**: [Semantic-UI](https://semantic-ui.com/) from github

In your settings.py:
```
#some imports
from django_static_libs.libraries import jquery
DJANGO_STATIC_LIBS = {
#The default is the jquery library. If you add other or custom libraries it will replace the default. it need always to be a dict, the key represents your folder and will be needed for the static import
'libraries': { 
            'jquery':jquery,
            
            'custom_full':
                {
                'provider' : GithubProvider("jquery/jquery"),
			    'suffix_ignore': [".json"],
			    'files_include': r"jquery-[\d\.]+/dist/(.*\.(js|map))",
			    #auto creates in your static root a folder "latest_static_libs". If you change this default path be careful in the templates
			    'destination':"auto",
                }
            }
}
```
#### Add your own library

You can add your own library as a dict into the config. Please submit your configurations by pull request or issue that it can be added for everyone.

| Property      | Value                  | Example                                 | Description                                                                                            |
|---------------|------------------------|-----------------------------------------|--------------------------------------------------------------------------------------------------------|
| **provider**    | object of BaseProvider | ```GithubProvider("jquery/jquery")```   | Take github class as example, it gives access to the files                                             |
| **files_include** | regex as str           | ```[".json"]```                         | regex to include file or dir when extracting / downloading (the first matching group defines the path of folder) |
| **suffix_ignore** | list                   | ```r"jquery-[\d\.]+/dist/(.*\.(js))"``` | list of suffixes to exclude when extracting / downloading                                              |
| **destination** | str                    | "auto"                                    | Future releases to define path                                                                         |

### Future features

* own folder in static
* add other libraries for downloading
* improve process of downloading for other libraries
* when install is not running automatically
* new command: list of all libraries
* remember the currently installed version
* better error handling for download
* testing