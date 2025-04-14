import unittest
from imagekit import _generate_access_key

class TestImageKit(unittest.TestCase):
    def test_generate_access_key(self):
        key = _generate_access_key(12345)
        self.assertEqual(len(key), 32)

if __name__ == "__main__":
    unittest.main()