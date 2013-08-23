VERSION=1

import datetime, inspect

from tengah_sdk import metadata_constants as Metadata
from tengah_sdk import metadata_attribute_constants as MetadataAttribute

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

consts = {}

def add_const(prefix, d):
    return {prefix+k:v for k,v in d.items()}

consts.update(add_const("TE_METADATA_FIELDS_", Metadata.FIELDS))
consts.update(add_const("TE_METADATA_INFO_", Metadata.INFO))
consts.update(add_const("TE_METADATA_SERVICES_", Metadata.SERVICES))
consts.update(add_const("TE_METADATA_FILES_", Metadata.FILES))
consts.update(add_const("TE_METADATA_TYPES_", Metadata.TYPES))

consts.update(add_const("TE_METADATA_ATTRIBUTE_TYPES_", MetadataAttribute.TYPES))
consts.update(add_const("TE_METADATA_ATTRIBUTE_FIELDS_", MetadataAttribute.FIELDS))

subs = {
    'program': inspect.getfile(inspect.currentframe()),
    'date': datetime.datetime.utcnow(),
    'version' : VERSION,
    'consts' : consts,
    'year': '2013',
}


h_template = env.get_template('TEMetadata.h.template')
m_template = env.get_template('TEMetadata.m.template')

subs['filename'] = 'TEMetadata.h'
print >>open('TEMetadata.h','w'), h_template.render(subs)


subs['filename'] = 'TEMetadata.m'
print >>open('TEMetadata.m','w'), m_template.render(subs)


