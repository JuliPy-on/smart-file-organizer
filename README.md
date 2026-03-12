Smart File Organizer

A simple Python tool that automatically organizes files in a selected directory by sorting them into categories based on their file extensions.

Overview

Smart File Organizer helps keep directories clean and structured by automatically moving files into categorized folders.
The script scans a target folder, detects file types, and sorts them into predefined categories such as images, documents, videos, audio files, archives, and source code.

This tool is useful for organizing Downloads folders, project directories, or large collections of mixed files.

Features
	•	Automatic file classification based on file extensions
	•	Automatic creation of category folders
	•	File processing statistics
	•	Protection against overwriting existing files
	•	Simple and lightweight implementation in Python

File Categories

The program currently supports the following categories:
	•	Images — jpg, jpeg, png, gif, svg, webp
	•	Documents — pdf, docx, txt, xlsx, pptx
	•	Videos — mp4, avi, mkv, mov
	•	Audio — mp3, wav, flac, aac
	•	Archives — zip, rar, 7z, tar, gz
	•	Code — py, js, html, css, json

Installation

Clone the repository:

git clone https://github.com/JuliPy-on/smart-file-organizer.git
cd smart-file-organizer

Make sure you have Python installed:

python3 --version

Usage

Run the script from the terminal:

python3 organizer.py

After running the script, the program will scan the selected directory and move files into automatically created category folders.

Example

Before running the script:

Downloads/
file1.jpg
document.pdf
music.mp3
archive.zip
script.py

After running the script:

Downloads/
Images/file1.jpg
Documents/document.pdf
Audio/music.mp3
Archives/archive.zip
Code/script.py

Requirements
	•	Python 3.x

Future Improvements
	•	Custom user-defined categories
	•	CLI arguments for selecting directories
	•	Logging system
	•	GUI version of the organizer

License

This project is open-source and available for educational and personal use.
