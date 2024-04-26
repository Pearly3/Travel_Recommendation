from unittest.mock import Mock
from lib.get_countries import get_countries 
import requests
from lib.Location import Location
from lib.get_cities import get_cities

def test_api_returns_dictionary_of_country_names_and_ids():
    requester_mock = Mock(name="requester") 
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock
    
    expected_data = {
        'gXKD3sCcJI': 'Bahrain', 'hVs5HyPvID': 'Armenia',
        'VqASvLCk8S': 'United Arab Emirates', 'W1DBYJ0DT4': 'Brunei',
        'ZvhrzA2APU': 'Bhutan', 'MEzedNnNVw': 'Afghanistan', 
        'mDMzJJXtB2': 'Azerbaijan', 'KtRJin3dy9': 'Hong Kong', 
        'jPsWdF78Gn': 'China', 'wv4OCjRaNi': 'Iran', 
        'DlHQBjd2Ke': 'India', '8tlFatlW3B': 'Christmas Island', 
        'Ovzp6Ca4tr': 'Cocos [Keeling] Islands', 
        'AWnxgoUzw0': 'Bangladesh', 'AVGAFwTSFb': 'Jordan', 
        'pOykqMaxZB': 'Indonesia', 'J7QoCukbse': 'Georgia', 
        '4lBFb6Wpq5': 'Israel', 
        'WUeznxS4oA': 'British Indian Ocean Territory', 
        'nvhpnKO5rE': 'Iraq', 'cbUYyXWdUS': 'North Korea', 
        'EpBnGVkBLF': 'Cambodia', '9N0Bhm2Ge4': 'Sri Lanka', 
        'UN9yBtQstI': 'Japan', 'H27W1K2Jx0': 'South Korea', 
        'nRlkwMtWiB': 'Kazakhstan', 'eaNpdUY6IC': 'Laos', 
        'KoZCNHDS5X': 'Kyrgyzstan', 'qlkgJorlNV': 'Kuwait', 
        'P2wZxWNxtr': 'Lebanon', 'ovfuQeRszZ': 'Maldives', 
        'uq5oiRuEKm': 'Nepal', '76H3yHIo7U': 'Mongolia', 
        'larowCNukg': 'Macao', 'yP5OXMfgmQ': 'Palestine', 
        'PqGe1JXHMY': 'Saudi Arabia', 'ta4EmTNWmu': 'Oman', 
        'fadJTpiTZO': 'Qatar', 'cz9fi68eVU': 'Myanmar [Burma]', 
        'k2lukc4AyV': 'Thailand', 'AnLxFNCcFS': 'Singapore', 
        'SHOmq2VQlZ': 'Malaysia', 'pmnzGTREty': 'Philippines', 
        'YE4pRFqDqA': 'Pakistan', 'qURMHRB5Bh': 'Turkmenistan', 
        'aCjqJX3che': 'Syria', 'MFNxWtOZIm': 'Vietnam', 
        'E4wHs4HoxE': 'Uzbekistan', 'temdDhXHMy': 'Tajikistan', 
        'r1dBFhG3I7': 'Turkey'
    }

    response_mock.json.return_value = expected_data
    result = get_countries("Asia")
    assert result == expected_data