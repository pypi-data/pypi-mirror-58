# coding: utf-8

__all__ = ['ElektronError']


class ElektronError(Exception):
    """Base class for exceptions in this module.

    :param _code:
    :param message: description
    """
    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return 'Error code {} | {}'.format(self.code, self.message)
