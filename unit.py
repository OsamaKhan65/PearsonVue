
import unittest


# class TestSum(unittest.TestCase):

#     def test_sum(self):
#         self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

# if __name__ == '__main__':
#     unittest.main()

#.assertEqual(a, b) 	a == b
#assertNotEqual(a, b) 	a != b
#.assertTrue(x) 	    bool(x) is True
#.assertFalse(x) 	    bool(x) is False
#.assertIs(a, b) 	    a is b
#.assertIsNone(x) 	    x is None
#assertIsNotNone(a) 	a is not None
#.assertIn(a, b) 	    a in b
#assertNotIn(a, b)  	a not in b
#assertIsInstance(a, b)  isinstance(a, b)
	

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

#execute the code on python console    
#run -m unittest
#run -m unittest unit
#run -m unittest -v unit.py   # for higher verbosity i.e wordy
#run -m unittest -h   #For a list of all the command-line options:
