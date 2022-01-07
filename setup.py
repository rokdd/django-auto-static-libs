from os.path import join, dirname
from distutils.core import setup

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

except IOError:
    long_description = None

version = __import__('django_auto_static_libs').get_version()

setup(
    name='django-auto-static-libs',
    version=version,
    url="https://github.com/rokdd/django-auto-static-libs",
    download_url="https://github.com/rokdd/django-auto-static-libs/archive/refs/tags/v%s.tar.gz" % version,
    description='jQuery and other librarys ready to download self hosted and embed into templates',
    long_description=long_description,
    author='rokdd',
    author_email='r0kdd@yahoo.com',
    license='BSD',
    keywords='django jquery fontawesome pygal javascript static'.split(),
    platforms='any',
    long_description_content_type="text/markdown",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['django_auto_static_libs'],

    install_requires=[
        'requests',
    ]
)