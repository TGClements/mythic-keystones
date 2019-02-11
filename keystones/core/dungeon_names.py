# From the Blizzard API
_DUNGEON_IDS = {
    'ataldazar': 244,
    'freehold': 245,
    'tol dagor': 246,
    'the motherlode': 247,
    'waycrest manor': 248,
    'kings rest': 249,
    'temple of sethraliss': 250,
    'the underrot': 251,
    'shrine of the storm': 252,
    'siege of boralus': 353, # Not a typo, the API actually returns 353
}

ALTERNATIVE_NAMES = {
    'ataldazar': _DUNGEON_IDS['ataldazar'],
    'ad': _DUNGEON_IDS['ataldazar'],
    'atal\'dazar': _DUNGEON_IDS['ataldazar'],
    'atal': _DUNGEON_IDS['ataldazar'],

    'freehold': _DUNGEON_IDS['freehold'],
    'fh': _DUNGEON_IDS['freehold'],

    'tol dagor': _DUNGEON_IDS['tol dagor'],
    'td': _DUNGEON_IDS['tol dagor'],
    'toldagor': _DUNGEON_IDS['tol dagor'],
    'tol': _DUNGEON_IDS['tol dagor'],
    'dagor': _DUNGEON_IDS['tol dagor'],

    'the motherlode': _DUNGEON_IDS['the motherlode'],
    'ml': _DUNGEON_IDS['the motherlode'],
    'motherlode': _DUNGEON_IDS['the motherlode'],
    'the motherlode!': _DUNGEON_IDS['the motherlode'],
    'the motherlode!!': _DUNGEON_IDS['the motherlode'],
    'motherlode!': _DUNGEON_IDS['the motherlode'],
    'motherlode!!': _DUNGEON_IDS['the motherlode'],

    'waycrest manor': _DUNGEON_IDS['waycrest manor'],
    'waycrest': _DUNGEON_IDS['waycrest manor'],
    'manor': _DUNGEON_IDS['waycrest manor'],
    'wm': _DUNGEON_IDS['waycrest manor'],

    'kings rest': _DUNGEON_IDS['kings rest'],
    'king\'s rest': _DUNGEON_IDS['kings rest'],
    'kr': _DUNGEON_IDS['kings rest'],
    'kings': _DUNGEON_IDS['kings rest'],
    'rest': _DUNGEON_IDS['kings rest'],

    'temple of sethraliss': _DUNGEON_IDS['temple of sethraliss'],
    'temple': _DUNGEON_IDS['temple of sethraliss'],
    'sethraliss': _DUNGEON_IDS['temple of sethraliss'],
    'temple of sethralis': _DUNGEON_IDS['temple of sethraliss'],
    'sethralis': _DUNGEON_IDS['temple of sethraliss'],
    'snakes': _DUNGEON_IDS['temple of sethraliss'],
    'tos': _DUNGEON_IDS['temple of sethraliss'],

    'the underrot': _DUNGEON_IDS['the underrot'],
    'underrot': _DUNGEON_IDS['the underrot'],
    'underot': _DUNGEON_IDS['the underrot'],
    'ur': _DUNGEON_IDS['the underrot'],

    'shrine of the storm': _DUNGEON_IDS['shrine of the storm'],
    'shrine': _DUNGEON_IDS['shrine of the storm'],
    'storm': _DUNGEON_IDS['shrine of the storm'],
    'sots': _DUNGEON_IDS['shrine of the storm'],

    'siege of boralus': _DUNGEON_IDS['siege of boralus'],
    'siege': _DUNGEON_IDS['siege of boralus'],
    'boralus': _DUNGEON_IDS['siege of boralus'],
    'sob': _DUNGEON_IDS['siege of boralus'],
}

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
