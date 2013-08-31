VERSION=2

import datetime, inspect, os

from tengah_sdk import metadata_constants as Metadata
from tengah_sdk import metadata_attribute_constants as MetadataAttribute
from tengah_sdk import event_constants as Event

from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

mdconsts = {}
evconsts = {}

def add_const(prefix, d):
    return {prefix+k:v for k,v in d.items()}

mdconsts.update(add_const("TE_METADATA_FIELDS_", Metadata.FIELDS))
mdconsts.update(add_const("TE_METADATA_INFO_", Metadata.INFO))
mdconsts.update(add_const("TE_METADATA_SERVICES_", Metadata.SERVICES))
mdconsts.update(add_const("TE_METADATA_FILES_", Metadata.FILES))
mdconsts.update(add_const("TE_METADATA_TYPES_", Metadata.TYPES))
mdconsts.update(add_const("TE_METADATA_ATTRIBUTE_TYPES_", MetadataAttribute.TYPES))
mdconsts.update(add_const("TE_METADATA_ATTRIBUTE_FIELDS_", MetadataAttribute.FIELDS))

evconsts.update(add_const('TE_EVENT_SYSTEM_', Event.SYSTEM))
evconsts.update(add_const('TE_EVENT_USER_',   Event.USER))

consts = {'TEMetadataConstants' : mdconsts,
          'TEEventConstants'    : evconsts,
}

subs = {
    'program': inspect.getfile(inspect.currentframe()),
    'date': datetime.datetime.utcnow(),
    'version' : VERSION,
    'consts' : mdconsts,
    'year': '2013',
}

for tfile in os.listdir('templates'):
    tparts = tfile.split('.')
    if tparts[1] in ('m', 'h') and tparts[2] == 'template':
        print tparts
        template = env.get_template(tfile);
        gfilename = tparts[0] + '.' + tparts[1]
        subs['filename'] = gfilename
        subs['consts']   = consts[tparts[0]]
        print >>open(gfilename, 'w'), template.render(subs)
        

