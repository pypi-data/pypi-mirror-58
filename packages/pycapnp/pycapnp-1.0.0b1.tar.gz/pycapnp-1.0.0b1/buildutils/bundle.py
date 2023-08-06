"""utilities for fetching build dependencies."""

#
#  Copyright (C) PyZMQ Developers
#  Distributed under the terms of the Modified BSD License.
#
#  This bundling code is largely adapted from pyzmq-static's get.sh by
#  Brandon Craig-Rhodes, which is itself BSD licensed.
#
# Adapted for use in pycapnp from pyzmq. See https://github.com/zeromq/pyzmq
# for original project.


import fileinput
import os
import shutil
import tarfile

from urllib.request import urlopen
from .msg import info

pjoin = os.path.join


#
# Constants
#


bundled_version = (0, 7, 0)
libcapnp_name = "capnproto-c++-%i.%i.%i.tar.gz" % (bundled_version)
libcapnp_url = "https://capnproto.org/" + libcapnp_name

HERE = os.path.dirname(__file__)
ROOT = os.path.dirname(HERE)


#
# Utilities
#


def untgz(archive):
    """Remove .tar.gz"""
    return archive.replace('.tar.gz', '')


def localpath(*args):
    """construct an absolute path from a list relative to the root pycapnp directory"""
    plist = [ROOT] + list(args)
    return os.path.abspath(pjoin(*plist))


def fetch_archive(savedir, url, fname, force=False):
    """download an archive to a specific location"""
    dest = pjoin(savedir, fname)
    if os.path.exists(dest) and not force:
        info("already have %s" % fname)
        return dest
    info("fetching %s into %s" % (url, savedir))
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    req = urlopen(url)
    with open(dest, 'wb') as f:
        f.write(req.read())
    return dest


#
# libcapnp
#


def fetch_libcapnp(savedir, url=None):
    """download and extract libcapnp"""
    is_preconfigured = False
    if url is None:
        url = libcapnp_url
        is_preconfigured = True
    dest = pjoin(savedir, 'capnproto-c++')
    if os.path.exists(dest):
        info("already have %s" % dest)
        return
    fname = fetch_archive(savedir, url, libcapnp_name)
    tf = tarfile.open(fname)
    with_version = pjoin(savedir, tf.firstmember.path)
    tf.extractall(savedir)
    tf.close()
    # remove version suffix:
    if is_preconfigured:
        shutil.move(with_version, dest)
    else:
        cpp_dir = os.path.join(with_version, 'c++')
        shutil.move(cpp_dir, dest)

    # XXX (HaaTa): There's a bug in capnproto-0.7.0 on CentOS 6 (or any glibc older than 2.16)
    #              This patches the issue
    with fileinput.FileInput(os.path.join(dest, 'src', 'kj', 'table.c++'), inplace=True, backup='.bak') as f:
        for line in f:
            print(
                line.replace(
                    '__APPLE__ || __BIONIC__', '__APPLE__ || __BIONIC__ || (defined(__GLIBC__) && (__GLIBC__ == 2) && (__GLIBC_MINOR__ < 16))'
                ),
                end=''
            )
