# coding=utf-8
from __future__ import absolute_import, print_function


class Error(Exception):
    MESSAGE = ""

    def __init__(self, *args, **kwargs):
        msgs = [msg.format(**kwargs) for msg in (self.MESSAGE, *args) if msg]
        super(Error, self).__init__(*msgs)
