def convert_celToFah(celTemp):
    return celTemp* 9/5 + 32

def covert_celToKel(celTemp):
    return celTemp + 273.15

def convert_fahToCel(fahTemp):
    return ((fahTemp - 32) * (5/9))

def convert_fahToKel(fahTemp):
    return (fahTemp - 32) * (5/9) + 273.15

def convert_kelToCel(kelTemp):
    return kelTemp - 273.15

def convert_kelTofah(kelTemp):
    return (kelTemp - 273.15) * 9/5 + 32
    

