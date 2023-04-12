#CREATE XML FILE AND APPEND FILE WITH NEW PRODUCTS
import xml.etree.ElementTree as ET

root_shop = ET.Element('shop')
root_category = ET.SubElement(root_shop,'category',{'name':'Vegan Products'})

def add_tags(root_name,lst_texts,parent_root = root_category, root_tag = 'product',lst_tags=['type','producer','price','currency']):
    root_tmp = ET.SubElement(parent_root, root_tag,{'name':root_name})
    i = 0
    for txt in lst_texts:
        txt_tmp = ET.SubElement(root_tmp,lst_tags[i])
        txt_tmp.text = txt
        i+=1
        

add_tags('Good Morning Sunshine',["cereals","OpenEDG Testing Service","9.90","USD"])     
add_tags('Spaghetti Veganietto',["pasta","Programmers Eat Pasta","15.49","EUR"])     
add_tags('Fantastic Almond Milk',["beverages","Drinks4Coders Inc.","19.75","EUR"]) 


ET.dump(root_shop)

tree = ET.ElementTree(root_shop)
tree.write("python_shop.xml", "UTF-8", True)
