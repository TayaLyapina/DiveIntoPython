import pytest
from file_with_task import get_dict


def test_get_value():
    assert get_dict({1: 'one', 2: 'two', 3: 'three'}, 1, 1) == 'one'


def test_get_default_value_fron_func():
    assert get_dict({1: 'one', 2: 'two', 3: 'three'}, 'a', 'None') == 'None'


def test_get_default_value():
    assert get_dict({1: 'one', 2: 'two', 3: 'three'}, 'two', 'Not Found') == 'Not Found'


if __name__ == '__main__':
    pytest.main(['-v'])