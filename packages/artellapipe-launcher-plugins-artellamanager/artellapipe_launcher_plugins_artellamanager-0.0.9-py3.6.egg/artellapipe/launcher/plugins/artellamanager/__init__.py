#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for artellapipe-launcher-plugins-artellamanager
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import os
import inspect
import logging.config


def init(do_reload=False, dev=False):
    """
    Initializes module
    :param do_reload: bool, Whether to reload modules or not
    """

    logging.config.fileConfig(get_logging_config(), disable_existing_loggers=False)

    if not dev:
        import sentry_sdk
        try:
            sentry_sdk.init("https://80e52f34344c4dcab363dd767db14398@sentry.io/1832267")
        except RuntimeError:
            sentry_sdk.init("https://80e52f34344c4dcab363dd767db14398@sentry.io/1832267", default_integrations=False)

    from tpPyUtils import importer

    class ArtellaManagerPlugin(importer.Importer, object):
        def __init__(self, debug=False):
            super(ArtellaManagerPlugin, self).__init__(
                module_name='artellapipe.launcher.plugins.artellamanager', debug=debug)

        def get_module_path(self):
            """
            Returns path where tpNameIt module is stored
            :return: str
            """

            try:
                mod_dir = os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)
            except Exception:
                try:
                    mod_dir = os.path.dirname(__file__)
                except Exception:
                    try:
                        import tpDccLib
                        mod_dir = tpDccLib.__path__[0]
                    except Exception:
                        return None

            return mod_dir

    packages_order = []

    artellamanager_importer = importer.init_importer(importer_class=ArtellaManagerPlugin, do_reload=False, debug=dev)
    artellamanager_importer.import_packages(order=packages_order, only_packages=False)
    if do_reload:
        artellamanager_importer.reload_all()

    create_logger_directory()

    from artellapipe.utils import resource
    resources_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')
    resource.ResourceManager().register_resource(resources_path)


def create_logger_directory():
    """
    Creates artellapipe logger directory
    """

    artellapipe_logger_dir = os.path.normpath(os.path.join(os.path.expanduser('~'), 'artellapipe', 'logs'))
    if not os.path.isdir(artellapipe_logger_dir):
        os.makedirs(artellapipe_logger_dir)


def get_logging_config():
    """
    Returns logging configuration file path
    :return: str
    """

    create_logger_directory()

    return os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))


def get_logging_level():
    """
    Returns logging level to use
    :return: str
    """

    if os.environ.get('ARTELLAPIPE_LAUNCHER_PLUGINS_ARTELLA_MANAGER_LOG_LEVEL', None):
        return os.environ.get('ARTELLAPIPE_LAUNCHER_PLUGINS_ARTELLA_MANAGER_LOG_LEVEL')

    return os.environ.get('ARTELLAPIPE_LAUNCHER_PLUGINS_ARTELLA_MANAGER_LOG_LEVEL', 'DEBUG')
