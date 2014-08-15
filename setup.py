from setuptools import setup, find_packages
import os

version = '1.0dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')
tests_require = []
setup(name='pretagov.buildoutmanager',
      version=version,
      description="Buildout manager for buildout",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Adam Terrey (PretaGov)',
      author_email='adam@pretagov.com',
      url='http://www.pretagov.com.au',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['pretagov'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      build = pretagov.buildoutmanager.build [main]
      """,

      tests_require=tests_require,
      extras_require={'test': tests_require},

      )
