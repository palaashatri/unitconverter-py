import unittest
from module_package import convert_digital, convert_weight, convert_length, convert_area

class TestConvert(unittest.TestCase):
    def test_convert_digi(self):
        result=convert_digital.convert(1,"MB","bit")
        self.assertEqual(result,8000000)
    
    def test_convert_weight(self):
        result=convert_weight.convert(1,"kg","g")
        self.assertEqual(result,1000)
    
    def test_convert_length(self):
        result=convert_length.convert(1000,"cm","m")
        self.assertEqual(result,10)
    
    def test_convert_area(self):
        result=convert_area.convert(1,"sqm","sqcm")
        self.assertEqual(result,10000)
        
if __name__ == '__main__':
    unittest.main()
