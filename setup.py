from os.path import join, dirname
from distutils.core import setup

try:
    f = open(join(dirname(__file__), 'README.md'))
    long_description = f.read()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-auto-static-libs',
    version='v0.2',
    url="https://github.com/rokdd/django-auto-static-libs",
    download_url="https://github.com/rokdd/django-auto-static-libs/archive/refs/tags/v0.2.tar.gz",
    description='jQuery and other librarys ready to embed into templates',
    long_description="Provide basic libraries and resources like jQuery or semantic-ui updated and self-hosted in django applications",
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