import csv
from datetime import datetime

# Approach:
# Design dedicated structural evaluation logic. We implement sequential checks 
# to build an aggregated validation registry. The script reports global error totals 
# along with highly informative row-level diagnostic messages.

total_rows = 0
valid_rows = 0
invalid_rows = 0
problems = []

with open('bookings.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for index, row in enumerate(reader, start=1):
        total_rows += 1
        row_errors = []
        
        # Rules Verification
        if not row.get("#") and not row.get("booking_id"):
            row_errors.append("missing booking_id")
        if not row.get("CUSTOMER") or row["CUSTOMER"].strip() == "":
            row_errors.append("missing customer_name")
            
        try:
            if float(row.get("AMOUNT", 0)) <= 0:
                row_errors.append("negative or zero amount")
        except ValueError:
            row_errors.append("invalid amount format")
            
        if row.get("STATUS", "").strip().lower() not in {"paid", "pending", "cancelled"}:
            row_errors.append("invalid status")
            
        date_str = row.get("DATE") or row.get("booking_date", "2026-01-01")
        try:
            datetime.strptime(date_str.strip(), "%Y-%m-%d")
        except ValueError:
            row_errors.append("invalid date")
            
        if row_errors:
            invalid_rows += 1
            problems.append(f"Row {index}: " + ", ".join(row_errors))
        else:
            valid_rows += 1

print("Validation Report")
print(f"Total rows checked: {total_rows}")
print(f"Valid rows: {valid_rows}")
print(f"Invalid rows: {invalid_rows}")
print("Problems found:")
for p in problems:
    print(f"- {p}")