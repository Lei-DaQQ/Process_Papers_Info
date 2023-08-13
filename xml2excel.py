
import os
import xml.etree.ElementTree as ET
import pandas as pd
import sys
import requests
from bs4 import BeautifulSoup
import json
import glob
import getAbstract

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

        #if pub_dict['ee']:
        #    abstract = get_abstract(pub_dict['ee'])
        #    pub_dict['abstract'] = abstract.strip() if abstract else ''
        #else:
        #    pub_dict['abstract'] = ''       

        publications.append(pub_dict)
    
    return publications

def export_to_excel(data, excel_file, columns):


    df = pd.DataFrame(data)
    
    # Create a DataFrame with specified columns
    df_output = pd.DataFrame(columns=[col["title"] for col in columns])
    
    # Fill in data according to specified columns
    for col in columns:
        if col["name"] != "no":
            df_output[col["title"]] = df[col["name"]]
    
    df_output.to_excel(excel_file, index=False)

def process_single_xml(xml_file, columns):
    publications_data = parse_dblp_xml(xml_file)
    output_excel_file = os.path.splitext(xml_file)[0] + '.xlsx'
    export_to_excel(publications_data, output_excel_file, columns)
    print(f"Data from '{xml_file}' has been successfully exported to '{output_excel_file}'.")


if __name__ == '__main__':
    print("Welcome to the XML to Excel converter!")

    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    while True:
        print("\nPlease select an option:")
        print("1. Process a single XML file")
        print("2. Batch process XML files in a folder")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            input_xml_file = input("Enter the path to the XML file: ")
            process_single_xml(input_xml_file, config["columns"])
            
        elif choice == '2':
            input_folder = input("Enter the path to the folder containing XML files: ")
            xml_files = glob.glob(os.path.join(input_folder, '*.xml'))
            
            if not xml_files:
                print("No XML files found in the specified folder.")
                continue
            
            for xml_file in xml_files:
                process_single_xml(xml_file, config["columns"])
                
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")
