VERSION=3

import datetime, inspect, os, importlib, string

from tengah_sdk import metadata_constants as Metadata
from tengah_sdk import metadata_attribute_constants as MetadataAttribute
from tengah_sdk import event_constants as Event

# init templating
from jinja2 import Template, Environment, FileSystemLoader

# build contants
def make_const(prefix, d):
    #print prefix
    #print d
    return {prefix+k:v for k,v in d.items()}

# generate constants for some item in a file
def generate_constants(outputname, items):
    if outputname.lower().endswith('constants'):
        outputname = outputname[:-9]
    consts = {}
    # print items
    for key,vals in items.items():
        # print "name,key,vals = ", outputname, key, vals
        consts.update(make_const("TE_%s_%s_" % (outputname.upper(),key), vals))

    return consts

# make a list of all the .py files in tengah_sdk

modules = {}
for pyfile in os.listdir('tengah_sdk'):
    pyparts = pyfile.split('.')
    if pyparts[1] == 'py' and pyparts[0] != '__init__':
        print "importing : " + 'tengah_sdk.' + pyparts[0]
        modules[pyparts[0]] = importlib.import_module('tengah_sdk.' + pyparts[0])

for modname,mod in modules.items():
    # for k in mod: # .__dict__.keys():
    # print map(str.capitalize, mod.__name__.split('.')[1].split('_')[:-1]).join('')
    words = mod.__name__.split('.')[1].split('_')
    outputname = string.capwords("_".join(words[:-1]), '_') + string.capwords(words[-1], '_')

    items = mod.__dict__.get('_ALL_')
    if items == None:
        print mod, " doesn't contain _ALL_"
        continue

    consts =  generate_constants(outputname, items)

    subs = {
        'name' : modname,
        'program': inspect.getfile(inspect.currentframe()),
        'date': datetime.datetime.utcnow(),
        'version' : VERSION,
        'consts' : consts,
        'year': '2013',

    }

    # now look for subdirectories for different languages
    # and generate libraries for them

    for languagedir in os.listdir('templates'):
        languagedirparts = languagedir.split('.')
        if languagedirparts[0] == '__init__':
            continue

        genmodname = 'templates.' + languagedir + '.generator'
        print genmodname
        genmod = importlib.import_module(genmodname)

        directory = 'templates/' + languagedir
        for tfile in os.listdir(directory):
            tparts = tfile.split('.')
            if tparts[1] in ('m', 'h') and tparts[2] == 'template':
                print tparts
                env = Environment(loader=FileSystemLoader('templates/' + languagedir))
                template = env.get_template(tfile);
                genmod.generate(template, tfile, subs)



