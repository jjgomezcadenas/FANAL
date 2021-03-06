"""
Define Fanal-specific exceptions
"""

class FException(Exception):
    """ Base class for Fanal exceptions hierarchy """

class DetectorNameNotDefined(FException):
    """ Detector name is not defined """
