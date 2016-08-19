from setuptools import setup, find_packages
import os
import demoapp
from pip.req import parse_requirements
import pip

requirements = parse_requirements('requirements.txt', session=pip.download.PipSession())
requires = [str(item.req) for item in requirements]
links = [str(item.url) for item in requirements if item.url is not None]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Daniel Boczek",
    author_email="daniel.boczek@gmail.com",
    name='django-demo',
    version=demoapp.__version__,
    description='Reusable app to protect access to project under development',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/dboczek/django-demo',
    license='Public Domain',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=requires,
    # tests_require=[
    # ],
    dependency_links=links,
    packages=find_packages(exclude=["project", "project.*"]),
    include_package_data=True,
    zip_safe=False,
    # test_suite='runtests.main',
)
