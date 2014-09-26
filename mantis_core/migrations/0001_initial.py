# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dingos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlobStorage',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.blobstorage',),
        ),
        migrations.CreateModel(
            name='DataTypeNameSpace',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.datatypenamespace',),
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.fact',),
        ),
        migrations.CreateModel(
            name='FactDataType',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.factdatatype',),
        ),
        migrations.CreateModel(
            name='FactTerm',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.factterm',),
        ),
        migrations.CreateModel(
            name='FactTerm2Type',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.factterm2type',),
        ),
        migrations.CreateModel(
            name='FactTermNamespaceMap',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.facttermnamespacemap',),
        ),
        migrations.CreateModel(
            name='FactValue',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.factvalue',),
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.identifier',),
        ),
        migrations.CreateModel(
            name='IdentifierNameSpace',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.identifiernamespace',),
        ),
        migrations.CreateModel(
            name='IdentifierNameSpaceSubstitutionMap',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.identifiernamespacesubstitutionmap',),
        ),
        migrations.CreateModel(
            name='InfoObject',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.infoobject',),
        ),
        migrations.CreateModel(
            name='InfoObject2Fact',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.infoobject2fact',),
        ),
        migrations.CreateModel(
            name='InfoObjectFamily',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.infoobjectfamily',),
        ),
        migrations.CreateModel(
            name='InfoObjectNaming',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.infoobjectnaming',),
        ),
        migrations.CreateModel(
            name='InfoObjectType',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.infoobjecttype',),
        ),
        migrations.CreateModel(
            name='Marking2X',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.marking2x',),
        ),
        migrations.CreateModel(
            name='NodeID',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.nodeid',),
        ),
        migrations.CreateModel(
            name='PositionalNamespace',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.positionalnamespace',),
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.relation',),
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.revision',),
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('dingos.userdata',),
        ),
    ]
