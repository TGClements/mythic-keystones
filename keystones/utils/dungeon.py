def get_dungeon_id(dungeon_name: str):
    return _ALTERNATIVE_NAMES.get(dungeon_name.lower())


def get_dungeon_name(dungeon_id):
    return _DUNGEON_IDS.get(dungeon_id)


EXAMPLE_NAMES = {
    'The Necrotic Wake': [
        'necrotic wake',
        'wake',
        'necrotic',
        'tnw',
    ],

    'Plaguefall': [
        'pf',
        'plague',
    ],

    'Mists of Tirna Scithe': [
        'mts',
        'mists',
        'tirna scithe',
    ],

    'Halls of Atonement': [
        'hot',
        'ht',
        'halls',
        'atonement',
    ],

    'Theater of Pain': [
        'theater',
        'pain',
        'top',
    ],

    'De Other Side': [
        'other side',
        'dos',
        'os',
    ],

    'Spires of Ascension': [
        'soa',
        'sa',
        'spires',
        'ascension',
    ],

    'Sanguine Depths': [
        'sanguine',
        'depths',
        'sd',
    ],
}

# From the Blizzard API
# This dictionary needs to be available like a two way dictionary.
# This version is used to get the name of a dungeon for users
_DUNGEON_IDS = {
    375: 'Mists of Tirna Scithe',
    376: 'The Necrotic Wake',
    377: 'De Other Side',
    378: 'Halls of Atonement',
    379: 'Plaguefall',
    380: 'Sanguine Depths',
    381: 'Spires of Ascension',
    382: 'Theater of Pain',
}

# This dictionary is used to get the id of a dungeon given its name
_DUNGEON_IDS_REVERSE = {
    'mists of tirna scithe': 375,
    'the necrotic wake': 376,
    'de other side': 377,
    'halls of atonement': 378,
    'plaguefall': 379,
    'sanguine depths': 380,
    'spires of ascension': 381,
    'theater of pain': 382,
}

_ALTERNATIVE_NAMES = {
    'the necrotic wake': _DUNGEON_IDS_REVERSE['the necrotic wake'],
    'necrotic wake': _DUNGEON_IDS_REVERSE['the necrotic wake'],
    'tnw': _DUNGEON_IDS_REVERSE['the necrotic wake'],
    'nw': _DUNGEON_IDS_REVERSE['the necrotic wake'],
    'wake': _DUNGEON_IDS_REVERSE['the necrotic wake'],
    'necrotic': _DUNGEON_IDS_REVERSE['the necrotic wake'],
    'necro': _DUNGEON_IDS_REVERSE['the necrotic wake'],

    'plaguefall': _DUNGEON_IDS_REVERSE['plaguefall'],
    'pf': _DUNGEON_IDS_REVERSE['plaguefall'],
    'plague': _DUNGEON_IDS_REVERSE['plaguefall'],

    'mists of tirna scithe': _DUNGEON_IDS_REVERSE['mists of tirna scithe'],
    'mists': _DUNGEON_IDS_REVERSE['mists of tirna scithe'],
    'tirna scithe': _DUNGEON_IDS_REVERSE['mists of tirna scithe'],
    'mts': _DUNGEON_IDS_REVERSE['mists of tirna scithe'],
    'mots': _DUNGEON_IDS_REVERSE['mists of tirna scithe'],
    'tirna': _DUNGEON_IDS_REVERSE['mists of tirna scithe'],

    'halls of atonement': _DUNGEON_IDS_REVERSE['halls of atonement'],
    'halls': _DUNGEON_IDS_REVERSE['halls of atonement'],
    'hot': _DUNGEON_IDS_REVERSE['halls of atonement'],
    'atonement': _DUNGEON_IDS_REVERSE['halls of atonement'],
    'atone': _DUNGEON_IDS_REVERSE['halls of atonement'],
    'ht': _DUNGEON_IDS_REVERSE['halls of atonement'],
    'hall of atonement': _DUNGEON_IDS_REVERSE['halls of atonement'],
    'hall': _DUNGEON_IDS_REVERSE['halls of atonement'],

    'theater of pain': _DUNGEON_IDS_REVERSE['theater of pain'],
    'theater': _DUNGEON_IDS_REVERSE['theater of pain'],
    'top': _DUNGEON_IDS_REVERSE['theater of pain'],
    'tp': _DUNGEON_IDS_REVERSE['theater of pain'],
    'pain': _DUNGEON_IDS_REVERSE['theater of pain'],

    'de other side': _DUNGEON_IDS_REVERSE['de other side'],
    'other side': _DUNGEON_IDS_REVERSE['de other side'],
    'dos': _DUNGEON_IDS_REVERSE['de other side'],
    'os': _DUNGEON_IDS_REVERSE['de other side'],
    'the other side': _DUNGEON_IDS_REVERSE['de other side'],
    'tos': _DUNGEON_IDS_REVERSE['de other side'],

    'spires of ascension': _DUNGEON_IDS_REVERSE['spires of ascension'],
    'spires': _DUNGEON_IDS_REVERSE['spires of ascension'],
    'spire': _DUNGEON_IDS_REVERSE['spires of ascension'],
    'soa': _DUNGEON_IDS_REVERSE['spires of ascension'],
    'sa': _DUNGEON_IDS_REVERSE['spires of ascension'],
    'ascension': _DUNGEON_IDS_REVERSE['spires of ascension'],

    'sanguine depths': _DUNGEON_IDS_REVERSE['sanguine depths'],
    'sanguine': _DUNGEON_IDS_REVERSE['sanguine depths'],
    'depths': _DUNGEON_IDS_REVERSE['sanguine depths'],
    'sd': _DUNGEON_IDS_REVERSE['sanguine depths'],
    'sanguine depth': _DUNGEON_IDS_REVERSE['sanguine depths'],
    'depth': _DUNGEON_IDS_REVERSE['sanguine depths'],
}
