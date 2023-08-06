__version__ = '0.0.5'
"""Extensions to the 'distutils' for large or complex distributions"""
NAME = "AIserver"
from AIserver import server as s
from AIserver import client as c
__metaclass__ = type
__all__ = [
    'client', 'server'
]


class Server(object):

    @staticmethod
    def left(step):
        s.left(step)
        # print("向左转")


class Client(object):

    @staticmethod
    def left(step):
        c.left(step)
