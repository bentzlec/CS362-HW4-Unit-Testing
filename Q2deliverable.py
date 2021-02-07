import unittest

def findAverage(array):
    try:
        return sum(array) / len(array)   
    except TypeError:
        return "Type Error! Try again"
    except ZeroDivisionError:
        return "Zero Division Error! Try again"
    except FloatingPointError:
        return "Floating Point Error! Try again"
    except OverflowError:
        return "Overflow error! Try again"
    except IndexError:
        return "Index Error! Try again"

class TestAvgCalc(unittest.TestCase):
    def test_Avg(self):
        arr = [1, 3, 7, 9, 9]
        result = findAverage(arr)
        self.assertEqual(result, 5.8)
    def test_TypeErr(self):
        arr = ["cat", "dog", "rat"]
        result = findAverage(arr)
        self.assertEqual(result, "Type Error! Try again")
    def test_MixedTypes(self):
        arr = [3.4, 8.5, 9, 10, 14]
        result = findAverage(arr)
        self.assertEqual(result, 8.98)
    def test_MixedTypes2(self):
        arr = [3.4, "cat", "dog", 4]
        result = findAverage(arr)
        self.assertEqual(result, "Type Error! Try again")
    def test_EmptyList(self):
        arr = []
        result = findAverage(arr)
        self.assertEqual(result, "Zero Division Error! Try again")

if __name__ == '__main__':
    unittest.main()