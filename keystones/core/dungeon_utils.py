def get_dungeon_id(dungeon_name: str):
    return _ALTERNATIVE_NAMES.get(dungeon_name.lower())


def get_dungeon_name(dungeon_id):
    return _DUNGEON_IDS.get(dungeon_id)


EXAMPLE_NAMES = {
    'Atal\'Dazar': [
        'ataldazar',
        'ad',
    ],

    'Freehold': [
        'fh',
    ],

    'Tol Dagor': [
        'td',
        'toldagor',
    ],

    'The MOTHERLODE!!': [
        'the motherlode',
        'ml',
        'motherlode',
    ],

    'Waycrest Manor': [
        'waycrest manor',
        'waycrest',
        'wm',
    ],

    'King\'s Rest': [
        'kings rest',
        'kr',
        'kings',
    ],

    'Temple of Sethraliss': [
        'temple',
        'sethraliss',
        'snakes',
        'tos',
    ],

    'The Underrot': [
        'underrot',
        'ur',
    ],

    'Shrine of the Storm': [
        'shrine',
        'storm',
        'sots',
    ],

    'Siege of Boralus': [
        'siege',
        'boralus',
        'sob',
    ],
}

# From the Blizzard API
# This dictionary needs to be available like a two way dictionary.
# This version is used to get the name of a dungeon for users
_DUNGEON_IDS = {
    244: 'Atal\'Dazar',
    245: 'Freehold',
    246: 'Tol Dagor',
    247: 'The MOTHERLODE!!',
    248: 'Waycrest Manor',
    249: 'King\'s Rest',
    250: 'Temple of Sethraliss',
    251: 'The Underrot',
    252: 'Shrine of the Storm',
    353: 'Siege of Boralus',  # Not a typo, the API actually returns 353
}

# This dictionary is used to get the id of a dungeon given its name
_DUNGEON_IDS_REVERSE = {
    'ataldazar': 244,
    'freehold': 245,
    'tol dagor': 246,
    'the motherlode': 247,
    'waycrest manor': 248,
    'kings rest': 249,
    'temple of sethraliss': 250,
    'the underrot': 251,
    'shrine of the storm': 252,
    'siege of boralus': 353,
}

_ALTERNATIVE_NAMES = {
    'ataldazar': _DUNGEON_IDS_REVERSE['ataldazar'],
    'ad': _DUNGEON_IDS_REVERSE['ataldazar'],
    'atal\'dazar': _DUNGEON_IDS_REVERSE['ataldazar'],
    'atal': _DUNGEON_IDS_REVERSE['ataldazar'],

    'freehold': _DUNGEON_IDS_REVERSE['freehold'],
    'fh': _DUNGEON_IDS_REVERSE['freehold'],

    'tol dagor': _DUNGEON_IDS_REVERSE['tol dagor'],
    'td': _DUNGEON_IDS_REVERSE['tol dagor'],
    'toldagor': _DUNGEON_IDS_REVERSE['tol dagor'],
    'tol': _DUNGEON_IDS_REVERSE['tol dagor'],
    'dagor': _DUNGEON_IDS_REVERSE['tol dagor'],

    'the motherlode': _DUNGEON_IDS_REVERSE['the motherlode'],
    'ml': _DUNGEON_IDS_REVERSE['the motherlode'],
    'motherlode': _DUNGEON_IDS_REVERSE['the motherlode'],
    'the motherlode!': _DUNGEON_IDS_REVERSE['the motherlode'],
    'the motherlode!!': _DUNGEON_IDS_REVERSE['the motherlode'],
    'motherlode!': _DUNGEON_IDS_REVERSE['the motherlode'],
    'motherlode!!': _DUNGEON_IDS_REVERSE['the motherlode'],

    'waycrest manor': _DUNGEON_IDS_REVERSE['waycrest manor'],
    'waycrest': _DUNGEON_IDS_REVERSE['waycrest manor'],
    'manor': _DUNGEON_IDS_REVERSE['waycrest manor'],
    'wm': _DUNGEON_IDS_REVERSE['waycrest manor'],

    'kings rest': _DUNGEON_IDS_REVERSE['kings rest'],
    'king\'s rest': _DUNGEON_IDS_REVERSE['kings rest'],
    'kr': _DUNGEON_IDS_REVERSE['kings rest'],
    'kings': _DUNGEON_IDS_REVERSE['kings rest'],
    'rest': _DUNGEON_IDS_REVERSE['kings rest'],

    'temple of sethraliss': _DUNGEON_IDS_REVERSE['temple of sethraliss'],
    'temple': _DUNGEON_IDS_REVERSE['temple of sethraliss'],
    'sethraliss': _DUNGEON_IDS_REVERSE['temple of sethraliss'],
    'temple of sethralis': _DUNGEON_IDS_REVERSE['temple of sethraliss'],
    'sethralis': _DUNGEON_IDS_REVERSE['temple of sethraliss'],
    'snakes': _DUNGEON_IDS_REVERSE['temple of sethraliss'],
    'tos': _DUNGEON_IDS_REVERSE['temple of sethraliss'],

    'the underrot': _DUNGEON_IDS_REVERSE['the underrot'],
    'underrot': _DUNGEON_IDS_REVERSE['the underrot'],
    'underot': _DUNGEON_IDS_REVERSE['the underrot'],
    'ur': _DUNGEON_IDS_REVERSE['the underrot'],

    'shrine of the storm': _DUNGEON_IDS_REVERSE['shrine of the storm'],
    'shrine': _DUNGEON_IDS_REVERSE['shrine of the storm'],
    'storm': _DUNGEON_IDS_REVERSE['shrine of the storm'],
    'sots': _DUNGEON_IDS_REVERSE['shrine of the storm'],

    'siege of boralus': _DUNGEON_IDS_REVERSE['siege of boralus'],
    'siege': _DUNGEON_IDS_REVERSE['siege of boralus'],
    'boralus': _DUNGEON_IDS_REVERSE['siege of boralus'],
    'sob': _DUNGEON_IDS_REVERSE['siege of boralus'],
}
