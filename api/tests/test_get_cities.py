from unittest.mock import Mock
from lib.get_cities import get_cities


def test_api_returns_list_of_cities():
    requester_mock = Mock(name="requester") 
    response_mock = Mock(name="response")

    requester_mock.get.return_value = response_mock

    expected_data = ['Istanbul', 'İstanbul', 'Çukurova']

    response_mock.json.return_value = expected_data
    result = get_cities("r1dBFhG3I7")
    assert result == expected_data