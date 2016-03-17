# Copyright 2016 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
This module contains configuration parser for Splunk local.metadata.
"""

import os
import re
import ConfigParser

from splunksolutionlib import splunkenv


class MetadataReader(object):
    '''Metadata reader for `app`.

    :param app: App name.
    :type app: ``string``

    :raises IOError: If Splunk `app` doesn't exist.
    '''

    def __init__(self, app):
        local_meta = splunkenv.make_splunkhome_path(
            ['etc', 'apps', app, 'metadata', 'local.meta'])

        self._cfg = ConfigParser.SafeConfigParser()
        # Loosen restriction on stanzas without header names.
        self._cfg.SECTCRE = re.compile(r'\[(?P<header>[^]]*)\]')

        if os.path.isfile(local_meta):
            # May raise ConfigParser.ParsingError
            self._cfg.read(local_meta)
        else:
            raise IOError('No such file: %s.' % local_meta)

    def get(self, conf, stanza, option):
        '''Return the metadata value of option in [conf/stanza] section.

        :param conf: Conf name.
        :param stanza: Stanza name.
        :param option: Option name in section [conf/stanza].
        :returns: Value of option in section [conf/stanza].
        :rtype: ``string``

        :raises ValueError: Raises ValueError if the value cannot be determined.
            Note that this can occur in several situations:

        - The section does not exist.
        - The section exists but the option does not exist.
        '''

        try:
            # Note: This may return a list because Python's stdlib ConfigParser
            # is broken. The exception raised on lines 550-551 will affect
            # SUCCESSFULLY parsed stanzas, because "join()" on a list of a
            # single item flattens the list. If this is an issue, uncomment
            # the AttributeError-handling block below to attempt to recover.
            return self._cfg.get('/'.join([conf, stanza]), option)
        # except AttributeError:
        #     try:
        #         return self._cfg.get('/'.join([conf, stanza]), option, raw=True)[0]
        #     except:
        #         raise
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            raise ValueError('The metadata value could not be determined.')

    def get_float(self, conf, stanza, option):
        '''Return the metadata value of option in [conf/stanza] section as a float.

        :param conf: Conf name.
        :param stanza: Stanza name.
        :param option: Option name in section [conf/stanza].
        :returns: A float value.
        :rtype: ``float``

        :raises ValueError: Raises ValueError if the value cannot be determined.
            Note that this can occur in several situations:

        - The stanza exists but the value does not exist (perhaps having never
          been updated).
        - The stanza does not exist.
        - The value exists but cannot be converted to a float.
        '''

        try:
            # Note: This may return a list because Python's stdlib ConfigParser
            # is broken. The exception raised on lines 550-551 will affect
            # SUCCESSFULLY parsed stanzas, because "join()" on a list of a
            # single item flattens the list. If this is an issue, uncomment
            # the AttributeError-handling block below to attempt to recover.
            return self._cfg.getfloat('/'.join([conf, stanza]), option)
        # except AttributeError:
        #     try:
        #         return float(self._cfg.get('/'.join([conf, stanza]), option, raw=True)[0])
        #     except:
        #         raise
        except (ConfigParser.NoSectionError, ConfigParser.NoOptionError):
            raise ValueError('The metadata value could not be determined.')
