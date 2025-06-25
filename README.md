Progress Photo Organizer
========================

This script automates the task of organizing and renaming progress photos stored in subfolders (named by job number) within a source directory. It moves these files to a structured destination path while renaming them with a timestamped format.

How It Works
------------

1. Reads subfolders from a specified <source_base> directory. Each subfolder represents a job number.
2. Iterates through each job folder, collecting all files inside.
3. Moves and renames the files into a corresponding subfolder inside <destination_base>/<job>/site photos/progress pics.
4. Renames files using the format:
   <job>_<MMDDYY> (<index>).<ext>

Example Folder Structure
------------------------

Source Directory (<source_base>):
    <source_base>/
    ├── 1001/
    │   ├── photo1.jpg
    │   └── photo2.jpg
    ├── 1002/
    │   └── image1.png

Destination Directory (<destination_base>):
    <destination_base>/
    ├── 1001/
    │   └── site photos/
    │       └── progress pics/
    │           ├── 1001_062525 (1).jpg
    │           └── 1001_062525 (2).jpg
    ├── 1002/
    │   └── site photos/
    │       └── progress pics/
    │           └── 1002_062525 (1).png

Configuration
-------------

Update the following two lines in the script with your actual directory paths:

    source_folder = "<source_base>"
    destination_path = os.path.join("<destination_base>", job, "site photos", "progress pics")

Replace <source_base> and <destination_base> with your desired full folder paths.

Usage
-----

Run the script using Python 3:

    python progress_photo_organizer.py

Make sure the source and destination directories exist and are accessible. The script will create any missing subfolders under the destination path automatically.

File Naming Convention
----------------------

Files are renamed using:

    <job>_<MMDDYY> (<file index>).<original extension>

This ensures uniqueness, sorting by date, and clear association with the job.

Requirements
------------

- Python 3.x
- No external libraries required (uses os, shutil, and datetime)

Notes
-----

- Files are moved (not copied). Be sure you have backups if needed.
- The script prints out what it's doing at each step for easy tracking.
