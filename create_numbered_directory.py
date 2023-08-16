
import os

def create_numbered_directory(path, prefix):
    if os.path.isdir(path):
        pass
    else:
        path = './'

    existing_numbers = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)) and item.startswith(prefix):
            try:
                num = int(item[len(prefix):])
                existing_numbers.append(num)
            except ValueError:
                pass
    
    max_existing_number = max(existing_numbers, default=0)
    new_number = max(max_existing_number, len(existing_numbers)) + 1
    new_dir_name = f"{prefix}{new_number:03}"
    new_dir_path = os.path.join(path, new_dir_name)
    
    os.makedirs(new_dir_path)
    print(f"Created new directory: {new_dir_path}")
    return new_dir_path

def main():
    # Example usage
    path = "bibs"
    prefix = "newdir"
    create_numbered_directory(path, prefix)

if __name__ == "__main__":
    main()
