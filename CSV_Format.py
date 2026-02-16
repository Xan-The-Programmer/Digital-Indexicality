import csv
from pathlib import Path
import shutil

def csv_col_del(column1: int, column2: int):
    des  = Path("C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Session Data Text/Raw CSVs")  
    target = Path("C:/Users/david/OneDrive - Osceola County School District/2025-2026 School Year/AP Research Evans Xan/Data Collection/Session Data Text/Cleaned CSVs")
    columns = [column1, column2]

    for i in range(0,2):
        for csv_file in des.glob("*.csv"):

            output_file = csv_file.with_name(f"{csv_file.stem}_formatted.csv")

            column_index_to_delete = columns[i] # Index 0 is the first column, 1 is the second

            with open(csv_file, 'r', newline='', encoding = "utf-8-sig") as infile, \
                open(output_file, 'w', newline='', encoding = "utf-8") as outfile:
                reader = csv.reader(infile)
                writer = csv.writer(outfile)
    
                for row in reader:
                    # Delete the specified column from the row list
                    if len(row) > column_index_to_delete:
                        del row[column_index_to_delete]
                    writer.writerow(row)

                shutil.move(outfile, target)

            print(
                f"Deleted column {i} from {csv_file.name} "
                f"→ saved as {output_file.name}"
            )
            shutil.move(csv_file, target)
    
