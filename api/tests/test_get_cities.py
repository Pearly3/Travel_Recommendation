from unittest.mock import Mock
from ..lib.get_cities import get_cities


def test_when_calling_api_with_specific_country_code_it_returns_countrys_list_of_cities():
    requester_mock = Mock() 
    response_mock = Mock()

    #tell `requester_mock` to return `response_mock` when we call `get()` on it.
    requester_mock.get.return_value = response_mock  

    response_mock.json.return_value = ['Istanbul', 'İstanbul', 'Çukurova']

    result = get_cities("r1dBFhG3I7", requests_get=requester_mock)
    assert result == response_mock.json.return_value



