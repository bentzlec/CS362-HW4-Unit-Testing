import unittest

def VolumeCalc(len):
    try:
        if(type(len) == float):
            return "Type Error! Try again"
        if(len > 0 ):
            return (len * len * len)
        if(len < 0):    
            return "Length cannot be negative"
    except TypeError:
        return "Type Error! Try again"
    except OverflowError:
        return "Overflow Error! Try again"


class TestVolumeCalc(unittest.TestCase):
    def test_VolumeCalc(self):
        result = VolumeCalc(3)
        self.assertEqual(result, 27)
    def test_negVolume(self):
        result = VolumeCalc(-3)
        self.assertEqual(result, "Length cannot be negative")
    def test_TypeError(self):
        result = VolumeCalc("a")
        self.assertEqual(result, "Type Error! Try again")
    def test_ComplexNum(self):
        result = VolumeCalc(6.8)
        self.assertEqual(result, "Type Error! Try again")


if __name__ == '__main__':
    unittest.main()
