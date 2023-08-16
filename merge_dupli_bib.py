import os
import re
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import BibDatabase
from create_numbered_directory import create_numbered_directory


def merge_duplicate_dois(input_file, output_file):
    with open(input_file, "r") as f:
        parser = BibTexParser()
        bib_database = bibtexparser.load(f, parser=parser)
    
    doi_to_entries = {}
    invalid_entries = []
    
    found_duplicate = False
    for entry in bib_database.entries:
        doi = entry.get("doi")
        if doi:
            doi = doi.lower()  # Convert to lowercase for case-insensitive matching
            if doi in doi_to_entries:
                found_duplicate = True
                doi_to_entries[doi].append(entry)
            else:
                doi_to_entries[doi] = [entry]
        else:
            invalid_entries.append(entry)

    # Check if there are duplicates or invalid entries
    if not found_duplicate and not invalid_entries:
        return False

    merged_entries = []
    remaining_entries = []
    
    for doi, entries in doi_to_entries.items():
        if len(entries) > 1:
            merged_entry = entries[0]
            bib_database.entries.remove(merged_entry)
            for entry in entries[1:]:
                merged_entry.update(entry)
                bib_database.entries.remove(entry)
            merged_entries.append(merged_entry)
        else:
            remaining_entries.append(entries[0])
    
    merged_db = BibDatabase()
    merged_db.entries = merged_entries

    remaining_db = BibDatabase()
    remaining_db.entries = remaining_entries

    with open(output_file, "w") as f:
        bibtexparser.dump(merged_db, f)
        f.write("\n\n")
        
        for entry in invalid_entries:
            f.write("@invalid{" + entry["ID"] + ",\n")
            for key, value in entry.items():
                f.write("  " + key + " = {" + value + "},\n")
            f.write("}\n\n")
        
        bibtexparser.dump(remaining_db, f)
        f.write("\n\n")
    return True

def process_single_file(file_path, output_path):
    print(f"### Now start to process file -> {os.path.basename(file_path)}")

    # Construct the merged filepath including the input file's directory
    merged_filename = os.path.basename(file_path).replace(".bib", "_merged.bib")
    merged_filepath = os.path.join(output_path, merged_filename)

    Merged = merge_duplicate_dois(file_path, merged_filepath)
    if Merged:
        print(f"Duplicates merged and saved. Merged file saved as -> {merged_filepath} ###\n")
    else:
        print(f"No duplicate or invalid references found in file -> {file_path}. No processing needed. ###\n")

def main():
    path = input("Enter the path to the BibTeX file or directory: ")

    # Find the latest merged directory or create a new one
    merged_dir = create_numbered_directory(path, 'merged')

    if os.path.isfile(path):
        process_single_file(path, merged_dir)
    elif os.path.isdir(path):
        print(f"### Now start to process directory -> {path}\n")
        for filename in os.listdir(path):
            if filename.endswith(".bib"):
                file_path = os.path.join(path, filename)
                process_single_file(file_path, merged_dir)
        print("Duplicates merged for all .bib files in the directory. ###")
    else:
        print("Invalid path.")

if __name__ == "__main__":
    main()
