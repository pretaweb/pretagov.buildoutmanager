
import sys
import subprocess
import os
from os import path
import re
from ConfigParser import RawConfigParser
from StringIO import StringIO

import logging
logger = logging.getLogger("pretagov.buildoutmanager")


class BuildoutManager(object):

    def __init__ (self, options):
        self._options = options
        self._location = options["location"]
        self._python = options.get("python", sys.executable)

        buildout_cfg_sections = {}
        for key, value in options.items():
            if ' ' in key:
                part, varable = key.split(' ')
                section = buildout_cfg_sections.get(part, {})
                section[varable] = value
                buildout_cfg_sections[part] = section
        self._buildout_cfg_sections = buildout_cfg_sections



    def write_buildout_cfg(self, sections):
        fout = open(path.join(self._location, "buildout.cfg"), "w")
        for section, options in self._buildout_cfg_sections.items():
            fout.write("[%s]\n" % section)
            for key, value in options.items():
                fout.write(key)
                for line in value.split("\n"):
                    fout.write(line + "\n  ")
                fout.write("\n")
        fout.close()

    def run_python(self, *args):
        cwd = os.getcwd()
        args = [self._python] + list(args)

        try:
            os.chdir(self._location)
            subprocess.check_output(args, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError, e:
            logger.error("run_python fail:\n" + e.output)
            raise RuntimeError("Could not run_python: %s" % args)
        finally:
            os.chdir(cwd)

    def run_buildout(self):
        cwd = os.getcwd()

        try:
            os.chdir(self._location)
            subprocess.check_output(['bin/buildout', '-N'], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError, e:
            logger.error("run_buildout fail:\n" + e.output)
            raise RuntimeError("Could not run_buildout" % args)
        finally:
            os.chdir(cwd)

    def get_version(self, name):

        # possibility - test to see if it is in self._buildout_cfg_sections ??


        # this is quite rudementry probably needs more smarts #HACK
        buildout_section = self._buildout_cfg_sections.get("buildout", {})

        # strip off equals sign
        extends = buildout_section.get("extends", "").strip("=")

        # filter non files
        search_files = [ f for f in extends.split() if len(f) > 0 ]


        for f in search_files:
            text = open(path.join(self._location, f), "r").read()
            mo = re.search("^%s\s*=\s*(\S+)\s*$" % name, text, flags=re.MULTILINE)
            if mo is not None:
                return mo.groups()[0]



    def bootstrap(self):

        version_zc_buildout = self.get_version('zc.buildout')
        version_setuptools = self.get_version('setuptools')

        self.write_buildout_cfg({
                'buildout': {
                   'parts': '=',
                   'extensions': '=',
                   'versions': '=versions'
                },
                'versions': {
                    'zc.buildout': '=' + version_zc_buildout,
                    'setuptools': '=' + version_setuptools
                }
            })

        self.run_python('bootstrap.py', "-v", version_zc_buildout)

        self.run_buildout()

    # Not a feature yet
    #def bootstrap_mr_developer(self):
    #    raise NotImplementedError()

    def buildout(self):
        self.write_buildout_cfg(self._buildout_cfg_sections)
        self.run_buildout()

    def build(self):

        
        l = self._location
        if not (path.isfile(path.join(l, "bin", "buildout"))) or \
                 not(path.isfile(path.join(l, ".installed.cfg"))):
            self.bootstrap()
        
        # Not a feature yet
        #if  exists(path.join(l, "bin", "develop") and exists(path.join(l, ".mr.developer.cfg") :
        #    self.bootstrap_mr_developer()

        self.buildout()

        

def main():
    
    cfg = RawConfigParser()
    cfg.read("managed_buildouts.cfg")
    for section in cfg.sections():
        buildout_opts = dict(cfg.items(section))
        bm = BuildoutManager(buildout_opts)
        bm.build()



