#PARSING FROM XML FILE. CREATE A TABLE WITH DEGREES IN CELCIUS AND FARENGHEIT

import xml.etree.ElementTree as ET


class TemperatureConverter:
    def __init__(self):
        pass
        
    def convert_celsius_to_fahrenheit(self,celcius):
        try:
            float(celcius)
        except AssertionError:
            print("Celcius must be a number")
        except Exception as e:
            print(e.message)
        else:
            return round((9/5)* int(celcius) + 32, 1)
        

class ForecastXmlParser:
    def __init__(self):
        pass
        
    def parse(self, filename):
        try:
            assert isinstance(filename, str)
            xml_file = ET.parse(filename)
        except AssertionError:
            print("File name must be string")
        except Exception as e:
            print(e.message)
        else:
            root = xml_file.getroot()
            for item in root:
                tmp = TemperatureConverter()
                print(item[0].text + ": ", item[1].text, "Celcius, ", tmp.convert_celsius_to_fahrenheit(item[1].text)," Fahrenheit")

fxp = ForecastXmlParser()
fxp.parse('forecast.xml')


