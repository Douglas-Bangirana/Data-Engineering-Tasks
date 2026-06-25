import csv

# Approach:
# Apply standard transformation steps to clean raw data lines (strip, string case mapping, 
# defaulting missing values). De-duplicate rows by verifying structural signatures 
# against a tracking state object before exporting output rows.

cleaned_data = []
seen_rows = set()

with open('bookings.csv', mode='r') as file:
    reader = csv.DictReader(file)
    fieldnames = reader.fieldnames
    
    for row in reader:
        # 1. Strip whitespace and 2. Convert name to title case
        row["CUSTOMER"] = row["CUSTOMER"].strip().title() if row["CUSTOMER"] else ""
        row["SERVICE"] = row["SERVICE"].strip().title() if row["SERVICE"] else ""
        
        # 3. Standardize service names if necessary (e.g. Visa stays Visa)
        if row["SERVICE"] == "visa":
            row["SERVICE"] = "Visa"
            
        # 5. Replace missing statuses
        if not row["STATUS"] or row["STATUS"].strip() == "":
            row["STATUS"] = "unknown"
        else:
            row["STATUS"] = row["STATUS"].strip().lower()
            
        # Create unique signature for row comparison to address 4. Deduplication
        row_signature = tuple(row[f] for f in fieldnames)
        if row_signature not in seen_rows:
            seen_rows.add(row_signature)
            cleaned_data.append(row)

# 6. Save data to output file
with open('cleaned_bookings.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_data)

print("Data cleaning complete. Output written to 'cleaned_bookings.csv'.")