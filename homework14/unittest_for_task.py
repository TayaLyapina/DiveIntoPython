import unittest
from file_with_task import get_dict
    

class TestCaseGetValue(unittest.TestCase):

    def test_get_value(self):
        self.assertEqual(get_dict({1: 'one', 2: 'two', 3: 'three'}, 1, 1), 'one')

    def test_get_default_value_fron_func(self):
        self.assertEqual(get_dict({1: 'one', 2: 'two', 3: 'three'}, 'a'), 'None')

    def test_get_default_value(self):
        self.assertEqual(get_dict({1: 'one', 2: 'two', 3: 'three'}, 'two', 'Not Found'), 'Not Found')


if __name__ == '__main__':
    unittest.main(verbosity=2)