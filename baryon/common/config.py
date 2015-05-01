# Copyright 2015 Cha Dong-Hwi

from oslo.config import cfg
from nova.openstack.common import log as logging
from neutron.openstack.common.gettextutils import _

LOG = logging.getLogger(__name__)

core_opts = [
    cfg.StrOpt('bind_host', default='0.0.0.0',
               help=_("The host IP to bind to")),
    cfg.IntOpt('bind_port', default=9696,
               help=_("The port to bind to")),
    cfg.StrOpt('api_paste_config', default="api-paste.ini",
               help=_("The API paste config file to use"))
]

CONF = cfg.CONF


def init(argv):
    #TODO: change version  string to pbr function
    CONF(argv[1:], project='baryon', version='0.1')

    product_name = "baryon"
    logging.setup(product_name)
    LOG.info(_("Logging enabled!"))
