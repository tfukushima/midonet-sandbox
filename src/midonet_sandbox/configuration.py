# Copyright (c) 2015 Midokura SARL, All Rights Reserved.
#
# @author: Antonio Sagliocco <antonio@midokura.com>, Midokura

import ConfigParser
import logging

from os.path import isfile
from midonet_sandbox.utils import Singleton


log = logging.getLogger('midonet-sandbox.configuration')

DEFAULT_SETTINGS = {
    'extra_components': None,
    'docker_socket': 'unix://var/run/docker.sock'
}

DEFAULT_CONFIGURATION_FILE = '~/.midonet-sandboxrc'


@Singleton
class Config(object):
    """
    Read and parse the configuration file. The configuration file format is:
    ---------------
    [sandbox]
    extra_components = None
    docker_socket = 'unix://var/run/docker.sock'
    -----------------
    """


    def __init__(self, config_file=None):
        self._config = ConfigParser.SafeConfigParser(defaults=DEFAULT_SETTINGS)

        if config_file and isfile(config_file):
            log.info('Trying configuration file: {}'.format(config_file))
            self._config.read(config_file)
        else:
            self._config.add_section('sandbox')
            log.info(
                'Cannot read configuration {}. Using default settings'.format(
                    config_file))

        log.debug('Settings: {}'.format(self._config))

    def get_default_value(self, param):
        return self._config.get('sandbox', param)
