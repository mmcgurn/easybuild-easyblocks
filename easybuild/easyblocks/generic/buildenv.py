##
# Copyright 2015-2018 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://www.vscentrum.be),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/easybuilders/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for creating a module that loads the build 
environment flags for the current toolchain 

@author: Alan O'Cais (Juelich Supercomputing Centre)
"""
from easybuild.tools.toolchain import DUMMY_TOOLCHAIN_NAME
from easybuild.easyblocks.generic.bundle import Bundle


class BuildEnv(Bundle):
    """
    Build environment of toolchain: only generate module file
    """
    def make_module_extra(self):
        """Add all the build environment variables."""
        txt = super(BuildEnv, self).make_module_extra()

        # include environment variables defined for (non-dummy) toolchain
        if self.toolchain.name != DUMMY_TOOLCHAIN_NAME:
            for key, val in sorted(self.toolchain.vars.items()):
                txt += self.module_generator.set_environment(key, val)

        self.log.debug("make_module_extra added this: %s" % txt)
        return txt
