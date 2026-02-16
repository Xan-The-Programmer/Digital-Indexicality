import csv
import shutil
from pathlib import Path
from datetime import datetime, date

def session_end():
    # Define source and destination paths
    print("initializing file paths")

    source_location = Path("C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Session Data Text/Cleaned CSVs")
    destination_location = Path("C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Master Raw Text")

    print("iterating through downloads")
    #iterate through downloads and move files
    for csv_file in source_location.glob("*.csv"):
        print("verifying file does not already exist in target location")
        target = destination_location / csv_file.name
        if not target.exists():
            print(f"file {csv_file} has been moved")
            shutil.move(csv_file, target)
        else:
            print(f"File: {csv_file} already exist in target directory, skipping this file.")
            continue

    print("files have been transfered")