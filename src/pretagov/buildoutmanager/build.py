

from os import path
from ConfigParser import RawConfigParser

class BuildoutManager(object):

    def __init__ (self, options):
        self._options = options
        self._location = options["location"]

        buildout_cfg_sections = {}
        for key, value in options.items():
            if ' ' in key:
                part, varable = key.split(' ')
                section = buildout_cfg_sections.get(part, {})
                section[varable] = value
                buildout_cfg_sections[part] = section
        self._buildout_cfg_sections = buildout_cfg_sections

    def run_python(self, *args):
        raise NotImplementedError()

    def run_buildout(self):
        raise NotImplementedError()

    def get_version(self, version_name):
        raise NotImplementedError()

    def write_buildout_cfg(self, sections):
        raise NotImplementedError()

    def bootstrap(self):

        version_zc_buildout = self.get_versions('zc.buildout')
        version_setuptools = self.get_versions('setuptools')

        write_buildout_cfg(self, {
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
        if path.isfile(path.join(l, "bin", "buildout")) and \
                 path.isfile(path.join(l, ".installed.cfg")):
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



