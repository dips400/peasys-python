class PeaException(Exception):
    '''Implements the concept of exception encountered during the manipulation of the Peasys library.'''
    pass

class PeaConnexionException(PeaException):
    '''Implements the concept of exception encountered during the connexion to the AS/400.'''
    pass

class PeaInvalidCredentialsException(PeaConnexionException):
    '''Implements the concept of exception due to invalid credentials encountered during the connexion to the AS/400.'''
    pass

class PeaInvalidLicenseKeyException(PeaConnexionException):
    '''Implements the concept of exception due to invalid license key encountered during the connexion to the AS/400.'''
    pass

class PeaQueryException(PeaException):
    '''Implements the concept of exception encountered when making a query to the AS/400.'''
    pass

class PeaInvalidSyntaxQueryException(PeaQueryException):
    '''Implements the concept of exception due to an invalid syntax encountered when making a query to the AS/400.'''
    pass

class PeaUnsupportedOperationException(PeaQueryException):
    '''Implements the concept of exception due to an unsupported operation encountered when making a query to the AS/400.'''
    pass