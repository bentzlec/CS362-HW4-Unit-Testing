import unittest

def makeName(first, last):
    try:
        fullname = first + " " + last
        return fullname
    except TypeError:
        return "Error!"

    
class TestNameMakerCalc(unittest.TestCase):
    def test_makeName(self):
        first = "Connor"
        last = "Bentzley"
        result = makeName(first, last)
        self.assertEqual(result, "Connor Bentzley")
    def test_error1(self):
        first = 2
        last = "Johnson"
        result = makeName(first, last)
        self.assertEqual(result, "Error!")
    def test_error2(self):
        first = "Jam3s"
        last = "J0hns0n"
        result = makeName(first, last)
        self.assertEqual(result, "Jam3s J0hns0n")
    def test_error3(self):
        first = ""
        last = "Washington"
        result = makeName(first, last)
        self.assertEqual(result, " Washington")


if __name__ == '__main__':
    unittest.main()