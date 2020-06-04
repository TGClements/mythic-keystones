def get_affix_name(affix_id):
    return _AFFIX_IDS[affix_id]


def get_affix_id(affix_name):
    return _AFFIX_IDS_REVERSE[affix_name]

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
}


_AFFIX_IDS_REVERSE = {
    'Overflowing': 1,
    'Skittish': 2,
    'Volcanic': 3,
    'Necrotic': 4,
    'Teeming': 5,
    'Raging': 6,
    'Bolstering': 7,
    'Sanguine': 8,
    'Tyrannical': 9,
    'Fortified': 10,
    'Bursting': 11,
    'Grievous': 12,
    'Explosive': 13,
    'Quaking': 14,
    'Relentless': 15,
    'Infested': 16,
    'Reaping': 117,
    'Beguiling': 119,
    'Awakened': 120,
}
