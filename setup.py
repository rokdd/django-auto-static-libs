from os.path import join, dirname
from distutils.core import setup

try:
    f = open(join(dirname(__file__), 'README.md'))
    long_description = f.read()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-static-libs',
    version='0.0.1',
    url="https://github.com/rokdd/django-static-libs",
    description='jQuery and other librarys ready to embed into templates',
    long_description=long_description,
    author='rokdd',
    author_email='r0kdd@yahoo.com',
    license='BSD',
    keywords='django jquery fontawesome pygal javascript static'.split(),
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['django_static_libs'],
    package_data={
        'django_static_libs': [
            'static/static_libs/js/*.js',
            'static/static_libs/js/*.map',
        ],
    },
)