# TODO: Add _ to Error Message
from baryon.openstack.common.gettextutils import _


class BaryonException(Exception):
    """Base Nova Exception

    To correctly use this class, inherit from it and define
    a 'msg_fmt' property. That msg_fmt will get printf'd
    with the keyword arguments provided to the constructor.

    """
    error_msg = "An unknown exception occurred."
    error_code = 500

    def __init__(self, message=None, **kwargs):
        self.emsg = self.error_msg % kwargs

        # TODO: Add fatal exception handling

        super(BaryonException, self).__init__(self.emsg)

class ConfigNotFound(BaryonException):
    error_msg = "Config File Not Found"