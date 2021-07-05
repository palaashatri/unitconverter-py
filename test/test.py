import pytest
from module_package import convert_digital, convert_weight, convert_length, convert_area

def test_convert_digital():
    assert convert_digital.convert(1,"MB","bit") == 8000000

def test_convert_weight():
    assert convert_weight.convert(1,"kg","g") == 1000
