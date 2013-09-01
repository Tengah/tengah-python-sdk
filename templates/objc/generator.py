import string


def generate(template, tfile, subs):
    print "Starting OBJC generator", subs.keys()
    print template, tfile, subs['name']
    tparts = tfile.split('.')
    modulename = "TE" + (('').join(map(string.capitalize, subs['name'].split('_'))))
    outfilename = modulename +  '.' + tparts[1]
    print modulename, outfilename

    subs['filename'] = outfilename
    subs['modulename'] = modulename

    print >>open(outfilename, 'w'), template.render(subs)

