import csv
import shutil
from pathlib import Path
from datetime import datetime, date

def session_sort():
    # Define source and destination paths
    print("initializing file paths")

    source_location = Path("C:/Users/david/Downloads")
    destination_location = Path("C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Session Data Text/Raw CSVs")

    # get todays date
    print("initializing date information")
    today = date.today()

    print("sorting downloads")
    csv_files = sorted(
        source_location.glob("*.csv"),
        key=lambda f: f.stat().st_ctime,
        reverse=True
    )
    print("iterating through downloads")
    #iterate through downloads and move files
    for csv_file in csv_files:
        #get file creation time
        creation_timestamp = csv_file.stat().st_mtime
        creation_date = datetime.fromtimestamp(creation_timestamp).date()

        print(f"verifying file: {csv_file} was created today")
        if creation_date == today:
            print(f"file: {csv_file} was created today")

            print("verifying file does not already exist in target location")
            target = destination_location / csv_file.name
            if not target.exists():
                print(f"file {csv_file} has been moved")
                shutil.move(csv_file, target)
            else:
                print(f"File: {csv_file} already exist in target directory, skipping this file.")
                continue

        else:
            continue

    print("downloads have been transfered")