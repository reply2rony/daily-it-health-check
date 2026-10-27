# Daily IT Health Check — summary script (starter learning template)
# Reads health-check-log-template.csv and prints a simple summary.
# It does not change the file and does not change any system setting.
# Sample data only.

import csv
from collections import Counter
from pathlib import Path

# Find the CSV file next to this script's parent folder.
CSV_FILE = Path(__file__).resolve().parent.parent / "health-check-log-template.csv"

def main():
    # Open the CSV and read every row as a dictionary.
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"Total checks logged: {len(rows)}")
    print()

    # Count checks by their Result column.
    print("Checks by result:")
    for result, count in Counter(row["Result"] for row in rows).items():
        print(f"  {result}: {count}")
    print()

    # List checks that need attention.
    print("Needs attention:")
    attention = [row for row in rows if row["Result"] == "Needs attention"]
    if attention:
        for row in attention:
            print(f"  {row['Date']} — {row['System']}: {row['Check']}")
    else:
        print("  None logged as needing attention.")
    print()

    # List checks that were not checked.
    print("Not checked:")
    unchecked = [row for row in rows if row["Result"] == "Not checked"]
    if unchecked:
        for row in unchecked:
            print(f"  {row['Date']} — {row['System']}: {row['Check']}")
    else:
        print("  None — every listed check has a result.")

if __name__ == "__main__":
    main()
