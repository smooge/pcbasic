"""
PC-BASIC - make.linux
Linux packaging

(c) 2015--2022 Rob Hagemans
This file is released under the GNU GPL version 3 or later.
"""

import subprocess

from .common import wash, build_icon, build_docs, wash, mkdir


def build_desktop_file():
    """Build .desktop file."""
    XDG_DESKTOP_ENTRY = """\
[Desktop Entry]
Name=PC-BASIC
GenericName=GW-BASIC compatible interpreter
Exec=/usr/local/bin/pcbasic
Terminal=false
Type=Application
Icon=pcbasic
Categories=Development;IDE;
"""
    with open('resources/pcbasic.desktop', 'w') as xdg_file:
        xdg_file.write(XDG_DESKTOP_ENTRY)


def build_deb_control_file(setup_options):
    """Build control file for deb package."""
    CONTROL_PATTERN = """\
Package: python3-pcbasic
Version: {version}
License: {license}
Vendor: none
Architecture: all
Maintainer: <{author_email}>
Depends: python3-pkg-resources,python3-serial,python3-parallel,libsdl2-2.0-0,libsdl2-gfx-1.0-0
Section: default
Priority: extra
Homepage: {url}
Description: {description}
"""
    with open('resources/control', 'w') as control_file:
        control_file.write(CONTROL_PATTERN.format(**setup_options))


def build_resources(setup_options):
    """Build desktop and package resources."""
    wash()
    mkdir('resources')
    build_desktop_file()
    build_deb_control_file(setup_options)
    build_icon()
    build_docs()


def package(**setup_options):
    """Build Linux packages."""
    subprocess.run('python3 -m make bdist_wheel', shell=True)
    build_resources(setup_options)
    version = setup_options['version']
    subprocess.run(f'make/makedeb.sh {version}', shell=True)
