import csv
from datetime import datetime

# Approach:
# Data Profiling: Evaluate data rows sequentially against a checklist of standard clean data metrics.
# Catch potential string parse errors (like dates or numbers) via try/except blocks to record issues safely.

seen_ids = set()

with open('payments.csv', mode='r') as file:
    reader = csv.DictReader(file)
    print("--- Data Quality Report ---")
    for index, row in enumerate(reader, start=1):
        # 1. Check missing customer name
        if not row.get("CUSTOMER") or row["CUSTOMER"].strip() == "":
            print(f"Row {index}: Missing customer name")
            
        # 2. Check negative amounts
        try:
            if float(row.get("AMOUNT", 0)) < 0:
                print(f"Row {index}: Negative amount ({row['AMOUNT']})")
        except ValueError:
            print(f"Row {index}: Invalid amount format")
            
        # 3. Check invalid status
        valid_statuses = {"paid", "pending", "cancelled", "success", "failed", "refunded"}
        if row.get("STATUS", "").strip().lower() not in valid_statuses:
            print(f"Row {index}: Missing or invalid status ({row.get('STATUS')})")
            
        # 4. Check duplicate booking IDs
        b_id = row.get("#") or row.get("booking_id")
        if b_id:
            if b_id in seen_ids:
                print(f"Row {index}: Duplicate booking ID ({b_id})")
            else:
                seen_ids.add(b_id)
                
        # 5. Check invalid date
        if "DATE" in row or "booking_date" in row:
            date_str = row.get("DATE") or row.get("booking_date")
            try:
                datetime.strptime(date_str.strip(), "%Y-%m-%d") # adjusting to expected pattern
            except (ValueError, TypeError):
                print(f"Row {index}: Invalid booking date ({date_str})")