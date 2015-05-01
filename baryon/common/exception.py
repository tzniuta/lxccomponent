class BaryonException(Exception):

    error_msg = _("An unknown exception occurred.")
    error_code = 500

    def __init__(self, message=None, **kwargs):
        self.emsg = self.error_msg % kwargs

        #TODO: Add fatal exception handling

        super(BaryonException, self).__init__(self.emsg)

class ConfigNotFound(BaryonException):
    error_msg = "Config File Not Found"