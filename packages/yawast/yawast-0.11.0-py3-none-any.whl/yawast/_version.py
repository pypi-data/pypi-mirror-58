# -*- coding: utf-8 -*-

#  Copyright (c) 2013 - 2019 Adam Caudill and Contributors.
#  This file is part of YAWAST which is released under the MIT license.
#  See the LICENSE file or go to https://yawast.org/license/ for full license details.

import os
import subprocess
import sys

# This file is part of 'miniver': https://github.com/jbweston/miniver
#
from collections import namedtuple
from distutils.command.build_py import build_py as build_py_orig

from setuptools.command.sdist import sdist as sdist_orig

Version = namedtuple("Version", ("release", "dev", "labels"))

__all__ = ["get_version"]

if getattr(sys, "frozen", False):
    # frozen
    package_root = os.path.dirname(sys.executable)
else:
    # unfrozen
    package_root = os.path.dirname(os.path.realpath(__file__))
package_name = os.path.basename(package_root)
distr_root = os.path.dirname(package_root)

STATIC_VERSION_FILE = "_static_version.py"


def get_version(version_file=STATIC_VERSION_FILE):
    version_info = get_static_version_info(version_file)
    version = version_info["version"]
    if version == "__use_git__":
        version = get_version_from_git()
        if not version:
            version = get_version_from_git_archive(version_info)
        if not version:
            version = Version("unknown", None, None)
        return pep440_format(version)
    else:
        return version


def get_static_version_info(version_file=STATIC_VERSION_FILE):
    version_info = {}
    with open(os.path.join(package_root, version_file), "rb") as f:
        exec(f.read(), {}, version_info)
    return version_info


def version_is_from_git(version_file=STATIC_VERSION_FILE):
    return get_static_version_info(version_file)["version"] == "__use_git__"


def pep440_format(version_info):
    release, dev, labels = version_info

    version_parts = [release]
    if dev:
        if release.endswith("-dev") or release.endswith(".dev"):
            version_parts.append(dev)
        else:  # prefer PEP440 over strict adhesion to semver
            version_parts.append(".dev{}".format(dev))

    if labels:
        version_parts.append("+")
        version_parts.append(".".join(labels))

    return "".join(version_parts)


def get_version_from_git():
    try:
        p = subprocess.Popen(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=distr_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except OSError:
        return
    if p.wait() != 0:
        return
    if not os.path.samefile(p.communicate()[0].decode().rstrip("\n"), distr_root):
        # The top-level directory of the current Git repository is not the same
        # as the root directory of the distribution: do not extract the
        # version from Git.
        return

    # git describe --first-parent does not take into account tags from branches
    # that were merged-in. The '--long' flag gets us the 'dev' version and
    # git hash, '--always' returns the git hash even if there are no tags.
    for opts in [["--first-parent"], []]:
        try:
            p = subprocess.Popen(
                ["git", "describe", "--long", "--always", "--tags"] + opts,
                cwd=distr_root,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except OSError:
            return
        if p.wait() == 0:
            break
    else:
        return

    description = (
        p.communicate()[0]
        .decode()
        .strip("v")  # Tags can have a leading 'v', but the version should not
        .rstrip("\n")
        .rsplit("-", 2)  # Split the latest tag, commits since tag, and hash
    )

    try:
        release, dev, git = description
    except ValueError:  # No tags, only the git hash
        # prepend 'g' to match with format returned by 'git describe'
        git = "g{}".format(*description)
        release = "unknown"
        dev = None

    labels = []
    if dev == "0":
        dev = None
    else:
        labels.append(git)

    try:
        p = subprocess.Popen(["git", "diff", "--quiet"], cwd=distr_root)
    except OSError:
        labels.append("confused")  # This should never happen.
    else:
        if p.wait() == 1:
            labels.append("dirty")

    return Version(release, dev, labels)


# TODO: change this logic when there is a git pretty-format
#       that gives the same output as 'git describe'.
#       Currently we can only tell the tag the current commit is
#       pointing to, or its hash (with no version info)
#       if it is not tagged.
def get_version_from_git_archive(version_info):
    try:
        refnames = version_info["refnames"]
        git_hash = version_info["git_hash"]
    except KeyError:
        # These fields are not present if we are running from an sdist.
        # Execution should never reach here, though
        return None

    if git_hash.startswith("$Format") or refnames.startswith("$Format"):
        # variables not expanded during 'git archive'
        return None

    vtag = "tag: v"
    refs = set(r.strip() for r in refnames.split(","))
    version_tags = set(r[len(vtag) :] for r in refs if r.startswith(vtag))
    if version_tags:
        release, *_ = sorted(version_tags)  # prefer e.g. "2.0" over "2.0rc1"
        return Version(release, dev=None, labels=None)
    else:
        return Version("unknown", dev=None, labels=["g{}".format(git_hash)])


__version__ = get_version()


# The following section defines a module global 'cmdclass',
# which can be used from setup.py. The 'package_name' and
# '__version__' module globals are used (but not modified).


def _write_version(fname):
    # This could be a hard link, so try to delete it first.  Is there any way
    # to do this atomically together with opening?
    try:
        os.remove(fname)
    except OSError:
        pass
    with open(fname, "w") as f:
        f.write(
            "# This file has been created by setup.py.\n"
            "version = '{}'\n".format(__version__)
        )


class _BuildPy(build_py_orig):
    def run(self):
        super().run()
        _write_version(os.path.join(self.build_lib, package_name, STATIC_VERSION_FILE))


class _SDist(sdist_orig):
    def make_release_tree(self, base_dir, files):
        super().make_release_tree(base_dir, files)
        _write_version(os.path.join(base_dir, package_name, STATIC_VERSION_FILE))


cmdclass = dict(sdist=_SDist, build_py=_BuildPy)

# Hacks to deal with the Windows build
try:
    from cx_Freeze.dist import build_exe as _build_exe

    class CmdBuildExe(_build_exe):
        def run(self):
            # Start by running the normal stuff
            _build_exe.run(self)

            # Now overwrite the static version file with our actual version
            _write_version(os.path.join(self.build_exe, STATIC_VERSION_FILE))

            # The validator_collection library incorrectly accesses its
            #  own _version.py file (using __file__, which is not cx_Freeze compatible)

            # Delete any existing _version.py file for the validator_collection library
            destination = os.path.join(
                self.build_exe, "lib", "validator_collection", "_version.py"
            )
            try:
                os.remove(destination)
            except Exception:
                pass

            # Create a dummy _version.py file (which is actually our own
            #  version number, not validator_collection's -- doesn't matter)
            with open(destination, "w") as f:
                f.write("__version__ = '{}'\n".format(__version__))

    # Add this derived class to cmdclass
    cmdclass["build_exe"] = CmdBuildExe
except Exception:
    pass
