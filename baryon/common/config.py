# Copyright 2015 Cha Dong-Hwi

import os
from oslo.config import cfg
from baryon.openstack.common.gettextutils import _

core_opts = [
    cfg.StrOpt('bind_host',
                default='0.0.0.0',
                help=_("The host IP to bind to")),
    cfg.IntOpt('bind_port',
                default=30000,
                help=_("The port to bind to")),
    cfg.StrOpt('api_paste_config',
                default="api-paste.ini",
                help="The API paste config file to use")
]

CONF = cfg.CONF
CONF.register_opts(core_opts)

def init(argv):
    # TODO: change version  string to pbr function
    CONF(argv[1:], project='baryon', version='0.1')

    load_loggin()


def load_loggin():
    # TODO: logging isn't working

    import gettext
    gettext.install('baryon')

    from baryon.openstack.common import gettextutils
    from baryon.openstack.common import log as logging
    gettextutils.install('baryon')

    LOG = logging.getLogger(__name__)
    logging.setup("baryon")
    LOG.info("Logging enabled!")
    LOG.info(_("Logging enabled!"))