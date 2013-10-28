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

from django.db import models

import dingos.models as dingos_models

#
# We create MANTIS proxy models for the dingos models.
# Thus, we can add Mantis-specific python stuff without
# touching the generic Dingo code
#

mantis_class_map = {}

class MantisManager(models.Manager):
    use_for_related_fields = True
    def get_query_set(self):
        #print "Get Query Set called for %s" % self.model
        qs = super(MantisManager, self).get_query_set()
        qs.model = mantis_class_map[self.model.__name__]
        return qs




class FactValue(dingos_models.FactValue):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(FactValue,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["FactValue"] = FactValue

class FactDataType(dingos_models.FactDataType):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(FactDataType,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["FactDataType"] = FactDataType



class IdentifierNameSpace(dingos_models.IdentifierNameSpace):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(IdentifierNameSpace,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["IdentifierNameSpace"] = IdentifierNameSpace


class DataTypeNameSpace(dingos_models.DataTypeNameSpace):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(DataTypeNameSpace,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["DataTypeNameSpace"] = DataTypeNameSpace

class FactTerm(dingos_models.FactTerm):
    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map

        super(FactTerm,self).__init__(*args,**kwargs)
    
    objects = MantisManager()

    @property
    def iobject_type_thru(self):
        qs = super(FactTerm,self).iobject_type_thru
        qs.model = FactTerm2Type
        return qs

    class Meta:
        proxy = True

mantis_class_map["FactTerm"] = FactTerm

class InfoObjectFamily(dingos_models.InfoObjectFamily):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(InfoObjectFamily,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["InfoObjectFamily"] = InfoObjectFamily


class Revision(dingos_models.Revision):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(Revision,self).__init__(*args,**kwargs)


    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["Revision"] = Revision


class FactTerm2Type(dingos_models.FactTerm2Type):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(FactTerm2Type,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["FactTerm2Type"] = FactTerm2Type



class InfoObjectNaming(dingos_models.InfoObjectNaming):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(InfoObjectNaming,self).__init__(*args,**kwargs)

    objects = MantisManager()


    class Meta:
        proxy = True

mantis_class_map["InfoObjectNaming"] = InfoObjectNaming


class InfoObjectType(dingos_models.InfoObjectType):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(InfoObjectType,self).__init__(*args,**kwargs)

    objects = MantisManager()


    class Meta:
        proxy = True

mantis_class_map["InfoObjectType"] = InfoObjectType



class InfoObject(dingos_models.InfoObject):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(InfoObject,self).__init__(*args,**kwargs)

    objects = MantisManager()





    class Meta:
        proxy = True

mantis_class_map["InfoObject"] = InfoObject

class Identifier(dingos_models.Identifier):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(Identifier,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["Identifier"] = Identifier

class NodeID(dingos_models.NodeID):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(NodeID,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True



mantis_class_map["NodeID"] = NodeID



class InfoObject2Fact(dingos_models.InfoObject2Fact):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(InfoObject2Fact,self).__init__(*args,**kwargs)

    objects = MantisManager()



    class Meta:
        proxy = True

mantis_class_map["InfoObject2Fact"] = InfoObject2Fact

class Fact(dingos_models.Fact):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(Fact,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["Fact"] = Fact

class Relation(dingos_models.Relation):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(Relation,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["Relation"] = Relation


class Marking2X(dingos_models.Marking2X):

    def __init__(self, *args, **kwargs):
        kwargs['dingos_class_map'] = mantis_class_map
        super(Marking2X,self).__init__(*args,**kwargs)

    objects = MantisManager()

    class Meta:
        proxy = True

mantis_class_map["Marking2X"] = Marking2X




