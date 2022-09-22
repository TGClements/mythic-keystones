def get_dungeon_id(dungeon_name: str):
    return _ALTERNATIVE_NAMES.get(dungeon_name.lower())


def get_dungeon_name(dungeon_id):
    return _DUNGEON_IDS.get(dungeon_id)


EXAMPLE_NAMES = {
    'Ruby Life Pools': [
	'ruby life pools',
	'rlp',
        'ruby',
        'life',
	'pools',
	'pool',
	'life pools',
    ],

    'The Nokhud Offensive': [
	'the nokhud offensive',
	'tno',
	'no',
        'nokhud offensive',
	'offensive',
    ],

    'The Azure Vault': [
	'the azure vault',
	'tav',
        'av',
        'azure vault',
        'azure',
	'vault',
    ],

    'Algeth\'ar Academy': [
	'aa',
        'algethar',
        'academy',
        'algethar academy',
    ],

    'Halls of Valor': [
	'halls of valor',
        'hov',
        'hv',
	'halls',
	'valor',
    ],

    'Court of Stars': [
	'court of stars',
        'cos',
	'cs',
        'court',
	'stars',
    ],

    'Shadowmoon Burial Grounds': [
	'shadowmoon burial grounds',
	'sbg',
	'shadowmoon',
        'burial',
	'grounds',
	'burial grounds',
	'shadowmoon burial',
    ],

    'Temple of the Jade Serpent': [
        'temple of the jade serpent',
	'tjs',
	'temple',
	'jade',
	'serpent',
	'jade serpent',
    ],
}

# From the Blizzard API
# This dictionary needs to be available like a two way dictionary.
# This version is used to get the name of a dungeon for users
_DUNGEON_IDS = {
# DF Season 1 Dungeons
    000: 'Ruby Life Pools',
    000: 'The Nokhud Offensive',
    000: 'The Azure Vault',
    000: 'Algeth\'ar Academy',
    000: 'Halls of Valor',
    000: 'Court of Stars',
    000: 'Shadowmoon Burial Grounds',
    000: 'Temple of the Jade Serpent',
}

# This dictionary is used to get the id of a dungeon given its name
_DUNGEON_IDS_REVERSE = {
# DF Season 1 Dungeons
    'ruby life pools': 000,
    'the nokhud offensive': 000,
    'the azure vault': 000,
    'algeth\'ar academy': 000,
    'halls of valor': 000,
    'court of stars': 000,
    'shadowmoon burial grounds': 000,
    'temple of the jade serpent': 000,
}

_ALTERNATIVE_NAMES = {
    'ruby life pools': _DUNGEON_IDS_REVERSE['ruby life pools'],
    'rlp': _DUNGEON_IDS_REVERSE['ruby life pools'],
    'ruby': _DUNGEON_IDS_REVERSE['ruby life pools'],
    'life': _DUNGEON_IDS_REVERSE['ruby life pools'],
    'pools': _DUNGEON_IDS_REVERSE['ruby life pools'],
    'pool': _DUNGEON_IDS_REVERSE['ruby life pools'],
    'life pools': _DUNGEON_IDS_REVERSE['ruby life pools'],

    'the nokhud offensive': _DUNGEON_IDS_REVERSE['the nokhud offensive'],
    'tno': _DUNGEON_IDS_REVERSE['the nokhud offensive'],
    'no': _DUNGEON_IDS_REVERSE['the nokhud offensive'],
    'nokhud offensive': _DUNGEON_IDS_REVERSE['the nokhud offensive'],
    'offensive': _DUNGEON_IDS_REVERSE['the nokhud offensive'],

    'the azure vault': _DUNGEON_IDS_REVERSE['the azure vault'],
    'tav': _DUNGEON_IDS_REVERSE['the azure vault'],
    'av': _DUNGEON_IDS_REVERSE['the azure vault'],
    'azure vault': _DUNGEON_IDS_REVERSE['the azure vault'],
    'azure': _DUNGEON_IDS_REVERSE['the azure vault'],
    'vault': _DUNGEON_IDS_REVERSE['the azure vault'],

    'aa': _DUNGEON_IDS_REVERSE['algeth\'ar academy'],
    'algethar': _DUNGEON_IDS_REVERSE['algeth\'ar academy'],
    'academy': _DUNGEON_IDS_REVERSE['algeth\'ar academy'],
    'algethar academy': _DUNGEON_IDS_REVERSE['algeth\'ar academy'],

    'halls of valor': _DUNGEON_IDS_REVERSE['halls of valor'],
    'hov': _DUNGEON_IDS_REVERSE['halls of valor'],
    'hv': _DUNGEON_IDS_REVERSE['halls of valor'],
    'halls': _DUNGEON_IDS_REVERSE['halls of valor'],
    'valor': _DUNGEON_IDS_REVERSE['halls of valor'],

    'court of stars': _DUNGEON_IDS_REVERSE['court of stars'],
    'cos': _DUNGEON_IDS_REVERSE['court of stars'],
    'cs': _DUNGEON_IDS_REVERSE['court of stars'],
    'court': _DUNGEON_IDS_REVERSE['court of stars'],
    'stars': _DUNGEON_IDS_REVERSE['court of stars'],

    'shadowmoon burial grounds': _DUNGEON_IDS_REVERSE['shadowmoon burial grounds'],
    'sbg': _DUNGEON_IDS_REVERSE['shadowmoon burial grounds'],
    'shadowmoon': _DUNGEON_IDS_REVERSE['shadowmoon burial grounds'],
    'burial': _DUNGEON_IDS_REVERSE['shadowmoon burial grounds'],
    'grounds': _DUNGEON_IDS_REVERSE['shadowmoon burial grounds'],
    'burial grounds': _DUNGEON_IDS_REVERSE['shadowmoon burial grounds'],
    'shadowmoon burial': _DUNGEON_IDS_REVERSE['shadowmoon burial grounds'],

    'temple of the jade serpent': _DUNGEON_IDS_REVERSE['temple of the jade serpent'],
    'tjs': _DUNGEON_IDS_REVERSE['temple of the jade serpent'],
    'temple': _DUNGEON_IDS_REVERSE['temple of the jade serpent'],
    'jade': _DUNGEON_IDS_REVERSE['temple of the jade serpent'],
    'serpent': _DUNGEON_IDS_REVERSE['temple of the jade serpent'],
    'jade serpent': _DUNGEON_IDS_REVERSE['temple of the jade serpent'],

}
