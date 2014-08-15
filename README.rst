.. contents::

pretagov.buildoutmanager
========================

Buildout Manager for buildout

Formalizing a buildout process.
A script that can bootstrap and build a buildout inserting local options.



Configuration inputs - python locations and git checkouts etc.

Suggested process
-----------------

1. Read configuration file
2. Inspect the buildout for buildout version number and distribute or setuptools version number
3. Check for bin/buildout and .installed.cfg if ether are missing then bootstrap
4. Cheek for bin/develop and .mr.developer.cfg if either are missing then run a buildout to create those
5. Checkout sup parts of the buildout.


Assumptions
-----------

* there are multiple git repositories involved with any buildout process.
* buildout.cfg is throwaway or doesn't exist
* the base buildout is already in existance
* there is a bootstrap file already there
* setup tools and zc.buildout are in the same file
* the versions exist in on of the buildout:extends files
* always using setup tools
* all buildout in the configuration file are active

Suggested Stories
-----------------

* Developer wants to bootstrap a buildout with correct python and setuptools and distribute
* Developer wants the buildout to have sup buildout directories managed by mr.developer so
  mr.developer needs to be installed before first buildout.
* Developer wants to update the buildout with the current changes
* Developer wants to run buildout with some extra local inputs
* Developer wants to run a buildout with some contextual differencts / or experimental components.
* Developer wants to run a report on the git changes involed in the current build.


Possible Test Sanario
---------------------


Configuation:


crate tmp dir

base.cfg

[buidout]
parts=cake
versions=versions

[cake]
recipe=collective.recipe.template
output=cake.cfg
input=inline:
  have your cake and eat it too :)

[pineapple]
recipe=collective.recipe.template
output=pineapple.txt
input=inline:
  have your pineapple and eat it too :) 

[versions]
zc.buildout=2.2.1
setuptools=3.8


get the bootstrap.py for buildout 2 file and put it in the directory

create another directory 

mybuildouts.cfg

[testbuild]
location=path/to/tmp/dir
python=path/to/local/python
buildout extends = =base.cfg
buildout parts = +=pineapple


tests:

build
create a bin/buildout file
is the file the correct buildout version and setuptools version?
is cake in cake.txt
is pineapple in pineapple.txt





