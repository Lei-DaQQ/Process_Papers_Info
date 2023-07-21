
import xml.etree.ElementTree as ET
import pandas as pd
import sys

def parse_dblp_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    publications = []
    
    for hit in root.findall('.//hit'):
        pub_dict = {}
        info = hit.find('info')
        
        pub_dict['title'] = info.find('title').text.strip() if info.find('title') is not None else ''
        pub_dict['authors'] = ', '.join([author.text.strip() for author in info.findall('.//author')])
        pub_dict['year'] = info.find('year').text.strip() if info.find('year') is not None else ''
        pub_dict['venue'] = info.find('venue').text.strip() if info.find('venue') is not None else ''
        pub_dict['ee'] = info.find('ee').text.strip() if info.find('ee') is not None else ''
        
        publications.append(pub_dict)
    
    return publications

def export_to_excel(data, excel_file):
    df = pd.DataFrame(data)
    df.to_excel(excel_file, index=False)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <input.xml>")
    else:
        input_xml_file = sys.argv[1]
        output_excel_file = 'output.xlsx'

        publications_data = parse_dblp_xml(input_xml_file)
        export_to_excel(publications_data, output_excel_file)
        print(f"Data from '{input_xml_file}' has been successfully exported to 'output.xlsx'.")
