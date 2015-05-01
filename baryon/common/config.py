from oslo.config import cfg
from nova.openstack.common import log as logging
from neutron.openstack.common.gettextutils import _

LOG = logging.getLogger(__name__)

CONF = cfg.CONF


def init(argv):
    #TODO: change version  string to pbr function
    CONF(argv[1:], project='baryon', version='0.1')

    product_name = "baryon"
    logging.setup(product_name)
    LOG.info(_("Logging enabled!"))
