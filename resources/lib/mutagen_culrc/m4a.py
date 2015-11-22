# -*- coding: utf-8 -*-
# Copyright 2006 Joe Wreschnig
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""
since 1.9: mutagen_culrc.m4a is deprecated; use mutagen_culrc.mp4 instead.
since 1.31: mutagen_culrc.m4a will no longer work; any operation that could fail
            will fail now.
"""

import warnings

from mutagen_culrc import FileType, Metadata, StreamInfo
from ._util import DictProxy, MutagenError

warnings.warn(
    "mutagen_culrc.m4a is deprecated; use mutagen_culrc.mp4 instead.",
    DeprecationWarning)


class error(IOError, MutagenError):
    pass


class M4AMetadataError(error):
    pass


class M4AStreamInfoError(error):
    pass


class M4AMetadataValueError(ValueError, M4AMetadataError):
    pass


__all__ = ['M4A', 'Open', 'delete', 'M4ACover']


class M4ACover(bytes):

    FORMAT_JPEG = 0x0D
    FORMAT_PNG = 0x0E

    def __new__(cls, data, imageformat=None):
        self = bytes.__new__(cls, data)
        if imageformat is None:
            imageformat = M4ACover.FORMAT_JPEG
        self.imageformat = imageformat
        return self


class M4ATags(DictProxy, Metadata):

    def load(self, atoms, fileobj):
        raise error("deprecated")

    def save(self, filename):
        raise error("deprecated")

    def delete(self, filename):
        raise error("deprecated")

    def pprint(self):
        return u""


class M4AInfo(StreamInfo):

    bitrate = 0

    def __init__(self, atoms, fileobj):
        raise error("deprecated")

    def pprint(self):
        return u""


class M4A(FileType):

    _mimes = ["audio/mp4", "audio/x-m4a", "audio/mpeg4", "audio/aac"]

    def load(self, filename):
        raise error("deprecated")

    def add_tags(self):
        self.tags = M4ATags()

    @staticmethod
    def score(filename, fileobj, header):
        return 0


Open = M4A


def delete(filename):
    raise error("deprecated")
