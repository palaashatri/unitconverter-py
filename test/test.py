import pytest
from module_package import convert_digital, convert_weight, convert_length, convert_area

def test_convert_digital():
    assert convert_digital.convert(1,"kB","byte") == 1000

def test_convert_weight():
    assert convert_weight.convert(1,"kg","g") == 1000

def test_convert_length():
    assert convert_length.convert(1000,"cm","m") == 10

def test_convert_area():
    assert convert_area.convert(1,"sqm","sqcm") == 10000