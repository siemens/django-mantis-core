# Copyright (c) Siemens AG, 2013
#
# This file is part of MANTIS.  MANTIS is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either version 2
# of the License, or(at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from mantis_core.models import mantis_class_map

from dingos.import_handling import DingoImportHandling


class MantisImportHandling(DingoImportHandling):
    def __init__(self, *args, **kwargs):
        self._DCM = kwargs.get('dingos_class_map',mantis_class_map)
        try:
            del(kwargs['dingos_class_map'])
        except:
            pass
        super(MantisImportHandling,self).__init__(*args,**kwargs)

MantisImporter = MantisImportHandling()
