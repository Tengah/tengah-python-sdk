FIELDS = {
    "OWNER"      : 'owner',
    "SERVICE"    : 'service',
    'ORIGINAL_DOC_ID' : 'original_doc_id',
    'METADATA_TYPE' : 'metadata_type',
    "ATTRIBUTES" : 'attributes',
}

INFO = {
    # Base
    'CREATED_AT' : 'created_at',
    'DESCRIPTION' : 'description',
    'MODIFIED_AT' : 'modified_at',
    'URL' : 'url',
    'LOCATION' : 'location',
    'HASH' : 'hash',
    'CONTENTS' : 'contents',
    'TYPE' : 'type',
    'STATUS_TYPE' : 'status_type',
    
    # Message
    'CC' : 'cc',
    'FROM' : 'from',
    'SUBJECT' : 'subject',
    'TO' : 'to',
    'REFERENCE' : 'reference',
    'REPLYTO' : 'replyto',
    'MENTION' : 'mention',
    'STORY' : 'story',
    'MESSAGE' : 'message',
    'SENT_AT' : 'sent_at',
    'EMAIL' : 'email',
    
    # File
    'FILENAME'   : 'filename',
    'FILESIZE_IN_BYTES' : 'filesize_in_bytes',
    'FILE_PATH' : 'file_path',
    'MIME_TYPE' : 'mime_type',
    'FILE_TYPE' : 'file_type',
    'OWNER' : 'owner',
    'SELF' : 'self',
    'TITLE' : 'title',
    'VIEWED_AT' : 'viewed_at',
    'THUMBNAIL' : 'thumbnail',
    
    # Image
    'DEPTH' : 'image_depth',
    'HEIGHT' : 'image_height',
    'QUANTUM_RANGE' : 'image_quantum_range',
    'UNITS' : 'image_units',
    'WIDTH' : 'image_width',
    'TAG'   : 'tag',
    'EXIF'  : 'exif',
    'QUALITY': 'quality',
    'FOLDER' : 'folder',
    'MAILINGLIST': 'mailinglist',
    'CAPTION' : 'caption',
    
    # EXIF
    'EXIF_CAPTURED' : 'exif_captured',
    'EXIF_ORIENTATION' : 'exif_orientation',
    'IMAGE_LENGTH' : 'exif_image_length',
    'IMAGE_RESOLUTION_UNIT' : 'exif_image_resolution_unit',
    'IMAGE_WIDTH' : 'exif_image_width',
    'IMAGE_XRES' : 'exif_image_xres',
    'IMAGE_YRES' : 'exif_image_yres',
    
    # Event
    'ATTENDEE' : 'attendee',
    'END_AT' : 'end_at',
    'ORGANIZER' : 'organizer',
    'START_AT' : 'start_at',
    'SUMMARY' : 'summary',
    
    # OpenCalais
    'ENTITY' : 'entity',
    'TOPIC'  : 'topic',
    'SOCIAL_TAG' : 'social_tag',
    
    # Contact
    'FRIEND' : 'friend',
    'DISPLAY_NAME' : 'display_name',
    'PROFILE' : 'profile',
    'BIRTHDAY' : 'birthday',
    'ABOUT' : 'about',
    'HOMETOWN' : 'hometown',
    'USERID' : 'userid',
    'WEBSITE' : 'website',
    'AVATAR' : 'avatar',
    
    # Personal
    'CALORIES' : 'calories',
    'STEPS' : 'steps',
    'LIFETIME_CALORIES' : 'lifetime_calories',
    'LIFETIME_STEPS' : 'lifetime_steps',
}

TYPES = {
    'CONTACT'  : 'contact',
    'EVENT'    : 'event',
    'FILE'     : 'file',
    'MESSAGE'  : 'message',
    'PERSONAL' : 'personal',
    'PURCHASE' : 'purchase',
    'PERSON'   : 'person',
}

FILES = {
    'ARCHIVE' : 'archive',
    'AUDIO' : 'audio',
    'BINARY' : 'binary',
    'CALENDAR' : 'calendar',
    'IMAGE' : 'image',
    'MESSAGE'   : 'message',
    'PDF'   : 'pdf',
    'PRESENTATION' : 'presentation',
    'SPREADSHEET' : 'spreadsheet',
    'TEXT'  : 'text',
    'UNKNOWN' : 'unknown',
    'VIDEO' : 'video',
}

SERVICES = {
    'CONTEXTIO' : 'contextio',
    'DROPBOX' : 'dropbox',
    'FACEBOOK' : 'facebook',
    'FITBIT' : 'fitbit',
    'GOOGLEDRIVE' : 'googledrive',
    'ICAL' : 'ical',
    'IMAGES' : 'images',
    'LINKEDIN' : 'linkedin',
    'TWITTER' : 'twitter'
}

DOCUMENT_FILES = (
    FILES['PRESENTATION'],
    FILES['SPREADSHEET'],
    FILES['TEXT'],
    FILES['PDF'],
)
    
