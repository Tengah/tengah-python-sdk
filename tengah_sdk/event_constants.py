# be sure to update _ALL_ at the bottom 

SYSINFO = {
    'APIKEY': 'key',
    'HOST': 'host',
    'PORT': 'port',
    'SYSINFOKEY' : 'PT',
}

SYSTEM = {
    'BROADCAST':'broadcast'
}

SYSTEM_BROADCAST = {
    'MESSAGE' : 'message',
    'TYPE' : 'type',
}

# User
USER = {
    'FLASH' : 'flash',                       # flash a message
    'SENDREQUEST' : 'sendrequest',           # send a file
    'WORKERSTATUS' : 'workerstatus',         # change in worker status
}


USER_FLASH = {
    'MESSAGE' : 'message',
    'TYPE' : 'type',
}

USER_SENDREQUEST = {
    'DESTINATION' : 'destination',              # a defined service
    'MDID' : 'mdid',                            # MD identifier
}

USER_WORKERSTATUS = {
    'ERROR':'error',
    'MESSAGE':'message',
    'NAME' : 'name', 
    'PROGRESS':'progress',
    'RATE':'rate',
    'STATE':'state',
    'TOTAL':'total',
}

_ALL_ = {
    'SYSINFO' : SYSINFO,
    'SYSTEM'  : SYSTEM,
    'SYSTEM_BROADCAST' : SYSTEM_BROADCAST,
    'USER' : USER,
    'USER_FLASH' : USER_FLASH,
    'USER_SENDREQUEST' : USER_SENDREQUEST,
    'USER_WORKERSTATUS' : USER_WORKERSTATUS,
}
