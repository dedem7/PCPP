#CREATE STRUCTURED TABLE FROM XML FILE
import xml.etree.ElementTree


try:
    stock = xml.etree.ElementTree.parse('nyse.xml').getroot()
except FileNotFoundError:
    print("File was not found")
except xml.etree.ElementTree.ParseError:
    print("Can't parse the file")
except Exception as e:
    print("Some error occured",e.message)
else:
    print("COMPANY".ljust(50), "LAST".ljust(9),"CHANGE".ljust(8),"MIN".ljust(8),"MAX")
    print("-"*85)
    for item in stock:
        print(item.text.ljust(50),item.attrib['last'].ljust(9),item.attrib['change'].ljust(8),item.attrib['min'].ljust(8),item.attrib['max'])





#SOME PRE-CHECKS
##tags_list = []
##header = []
##tags_list.append(stock.tag)
##for item in stock:
##    tags_list.append(item.tag)
##    header.append(list(item.attrib.keys()))
##    #print(item.attrib, item.text)
##
##
##
###tags_list = tuple(set(tags_list))
###header = tuple(set([i for j in header for i in j]))
###header = set(header)
###print(tags_list)
###print(header)
