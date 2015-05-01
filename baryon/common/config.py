# Copyright 2015 Cha Dong-Hwi

import os
from oslo.config import cfg
from nova.openstack.common import log as logging
from neutron.openstack.common.gettextutils import _

LOG = logging.getLogger(__name__)

core_opts = [
    cfg.StrOpt('bind_host', default='0.0.0.0',
               help=_("The host IP to bind to")),
    cfg.IntOpt('bind_port', default=30001,
               help=_("The port to bind to"))
]

CONF = cfg.CONF
CONF.register_opts(core_opts)

def init(argv):
    #TODO: change version  string to pbr function
    CONF(argv[1:], project='baryon', version='0.1')

    product_name = "baryon"
    logging.setup(product_name)
    LOG.info(_("Logging enabled!"))