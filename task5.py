import csv

# Approach:
# Open and ingest the structured 'bookings.csv' file using the native python 'csv' module. 
# Extract the header row first, track data points sequentially, and construct a list 
# of unique elements via standard sets.

total_rows = 0
total_revenue = 0
paid_revenue = 0
pending_count = 0
unique_services = set()

with open('bookings.csv', mode='r') as file:
    reader = csv.DictReader(file)
    print("--- CSV Rows ---")
    for row in reader:
        print(dict(row))
        total_rows += 1
        amount = float(row["AMOUNT"])
        total_revenue += amount
        unique_services.add(row["SERVICE"])
        
        if row["STATUS"].strip().lower() == "paid":
            paid_revenue += amount
        if row["STATUS"].strip().lower() == "pending":
            pending_count += 1

print(f"\nTotal rows: {total_rows}")
print(f"Unique services: {unique_services}")
print(f"Total revenue: {total_revenue}")
print(f"Paid revenue: {paid_revenue}")
print(f"Pending rows: {pending_count}")