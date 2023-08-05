import glob
import sys
from io import StringIO
from os.path import expanduser
from pkgutil import get_data

import re
from scrapy.utils.conf import closest_scrapy_cfg
from six.moves.configparser import ConfigParser, NoSectionError, NoOptionError


class Config(object):
    """A ConfigParser wrapper to support defaults when calling instance
    methods, and also tied to a single section"""

    SECTION = 'scrapydartx'

    def __init__(self, values=None, extra_sources=()):
        if values is None:
            sources = self._getsources()
            default_config = get_data(__package__, 'default_scrapyd.conf').decode('utf8')
            self.cp = ConfigParser()
            self.cp.read_file(StringIO(default_config))
            self.cp.read(sources)
            for fp in extra_sources:
                self.cp.read_file(fp)
        else:
            self.cp = ConfigParser(values)
            self.cp.add_section(self.SECTION)

    def _getsources(self):
        sources = ['/etc/scrapydartx/scrapydartx.conf', r'c:\scrapyd\scrapyd.conf']
        sources += sorted(glob.glob('/etc/scrapydartx/conf.d/*'))
        sources += ['scrapydartx.conf']
        sources += [expanduser('~/.scrapydartx.conf')]
        scrapy_cfg = closest_scrapy_cfg()
        if scrapy_cfg:
            sources.append(scrapy_cfg)
        return sources

    def _getany(self, method, option, default):
        try:
            return method(self.SECTION, option)
        except (NoSectionError, NoOptionError):
            if default is not None:
                return default
            raise

    def get(self, option, default=None):
        return self._getany(self.cp.get, option, default)

    def getint(self, option, default=None):
        return self._getany(self.cp.getint, option, default)

    def getfloat(self, option, default=None):
        return self._getany(self.cp.getfloat, option, default)

    def getboolean(self, option, default=None):
        return self._getany(self.cp.getboolean, option, default)

    def items(self, section, default=None):
        try:
            return self.cp.items(section)
        except (NoSectionError, NoOptionError):
            if default is not None:
                return default
            raise
