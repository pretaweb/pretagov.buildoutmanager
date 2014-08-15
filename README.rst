.. contents::

pretagov.buildoutmanager
========================

Buildout Manager for multiple buildouts. Enable for replicateing multiple
environments with different python versions and different zc.buildout versions.


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
* there is a correct version to run a buildout on

Suggested Stories
-----------------

* Developer wants to bootstrap a buildout with correct python and setuptools and distribute
* Developer wants to update the buildout with the current changes
* Developer wants to run buildout with some extra local inputs
* Developer wants to run a buildout with some contextual differencts / or experimental components.
* Developer wants to run a report on the git changes involed in the current build.





