import os
import shutil
from datetime import datetime  # <-- Added to get today’s date

# Creates variable for source folder
source_folder = "<source_base>"


# Creates function that reads the source folder and outputs the job numbers and number of jobs
def get_immediate_subfolders(path):
    subfolders = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            subfolders.append(entry)
    return subfolders, len(subfolders)


# Creates variables using function above
jobs_to_move, num_jobs_to_move = get_immediate_subfolders(source_folder)

# Gets today’s date in MMDDYY format for renaming files
today = datetime.today().strftime("%m%d%y")

# Prints to test that jobs and num of jobs look reasonable
print(jobs_to_move)
print(num_jobs_to_move)

# Runs loop to move files from source folders to appropriate destination folders
for job in jobs_to_move:
    # Creates job-specific source and destination paths
    source_path = os.path.join(source_folder, job)
    destination_path = os.path.join("<destination_base>", job, "site photos",
                                    "progress pics")

    # Creates list of files to move
    files_to_move = os.listdir(source_path)

    # Prints message to ensure files move
    print(f"Moving files from: {source_path}")
    print(f"To: {destination_path}")
    print(files_to_move)

    # Ensures that destination path exists
    os.makedirs(destination_path, exist_ok=True)

    # Moves and renames files before moving
    for idx, file_name in enumerate(files_to_move, start=1):
        # Gets file extension
        _, ext = os.path.splitext(file_name)

        # Creates new filename in the format: job_MMDDYY (1).ext
        new_file_name = f"{job}_{today} ({idx}){ext}"

        # Full paths for source and destination
        full_source = os.path.join(source_path, file_name)
        full_destination = os.path.join(destination_path, new_file_name)

        # Moves and renames the file
        shutil.move(full_source, full_destination)
        print(f"Moved: {file_name} → {new_file_name}")
