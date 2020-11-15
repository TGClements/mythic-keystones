def get_affix_name(affix_id):
    return _AFFIX_IDS.get(affix_id)


def get_affix_id(affix_name):
    return _AFFIX_IDS_REVERSE.get(affix_name.lower())

# From the Blizzard API
# Needs to be kept like a two way dictionary
_AFFIX_IDS = {
    1: 'Overflowing',
    2: 'Skittish',
    3: 'Volcanic',
    4: 'Necrotic',
    5: 'Teeming',
    6: 'Raging',
    7: 'Bolstering',
    8: 'Sanguine',
    9: 'Tyrannical',
    10: 'Fortified',
    11: 'Bursting',
    12: 'Grievous',
    13: 'Explosive',
    14: 'Quaking',
    15: 'Relentless',
    16: 'Infested',
    117: 'Reaping',
    119: 'Beguiling',
    120: 'Awakened',
    121: 'Prideful',
    122: 'Inspiring',
    123: 'Spiteful',
    124: 'Storming',
}


_AFFIX_IDS_REVERSE = {
    'overflowing': 1,
    'skittish': 2,
    'volcanic': 3,
    'necrotic': 4,
    'teeming': 5,
    'raging': 6,
    'bolstering': 7,
    'sanguine': 8,
    'tyrannical': 9,
    'fortified': 10,
    'bursting': 11,
    'grievous': 12,
    'explosive': 13,
    'quaking': 14,
    'relentless': 15,
    'infested': 16,
    'reaping': 117,
    'beguiling': 119,
    'awakened': 120,
    'prideful': 121,
    'inspiring': 122,
    'spiteful': 123,
    'storming': 124,
}
