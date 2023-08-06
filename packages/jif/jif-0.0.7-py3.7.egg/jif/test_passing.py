import unittest

class PassingTestCase(unittest.TestCase):

    def test_passing(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()