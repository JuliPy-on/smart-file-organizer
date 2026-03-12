import os
from pathlib import Path
import shutil

# Dictionary with categories and file extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c'],
    'Others': []  # For every other types
}


def get_file_category(file_extension):
    """
    Determines the file category(extension)
    
    Args:
        file_extension: File extension (for example, '.jpg')
    
    Returns:
        Category name (for example, 'Images')
    """
    # Convert the extension to lowercase
    file_extension = file_extension.lower()
    
    # Itterating through all categories 
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    
    # if not match category
    return 'Others'


def organize_files(source_folder):
    """
    Sorts files in the specified filder by categories 
    
    Args:
        source_folder: Path to the folfer that need to be sorted 
    """
    # Convert the batch to Path object 
    source_path = Path(source_folder)
    
    # Check if the folders exists
    if not source_path.exists():
        print(f"❌ Eror: folder '{source_folder}' doesn't exists!")
        return
    
    if not source_path.is_dir():
        print(f"❌ Eror: '{source_folder}' folder is not a directory!")
        return
    
    print(f"📁 Starting folder file organization: {source_folder}\n")
    
    # Сounter for statistics
    files_moved = 0
    files_skipped = 0
    
    # Iterate through all files in the folder
    for item in source_path.iterdir():
        # Skip directories, process only files 
        if item.is_file():
            # get the file extensions
            file_extension = item.suffix  # for example, '.jpg'
            
            # Determine the category
            category = get_file_category(file_extension)
            
            # Create the path to the category folder
            category_folder = source_path / category
            
            # Create a folder if it doesn't exist
            category_folder.mkdir(exist_ok=True)
            
            # Form the new Path for the file
            destination = category_folder / item.name
            
            # Check if a file with the same name alredy exists 
            if destination.exists():
                print(f"⚠️  Skip {item.name} — file already exists in {category}/")
                files_skipped += 1
            else:
                # Move the file 
                shutil.move(str(item), str(destination))
                print(f"✅ {item.name} → {category}/")
                files_moved += 1
    
    # Display Statistics
    print(f"\n📊 READY!")
    print(f"Filles moved: {files_moved}")
    print(f"Files skipped: {files_skipped}")


if __name__ == "__main__":
    # Request folder path from user
    folder_to_organize = input("Enter the folder path (or press Enter for the current one): ")
    
    # if nothing is entered use current folder
    if not folder_to_organize:
        folder_to_organize = "."
    
    organize_files(folder_to_organize)