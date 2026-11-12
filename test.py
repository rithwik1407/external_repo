import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10,20),40)
if __name__=="__main__":
    unittest.main()
