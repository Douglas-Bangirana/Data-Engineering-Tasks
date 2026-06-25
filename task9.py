import csv

# Approach:
# Read input metrics, gather descriptive statistics, track data maps for 
# modal status fields, and display an organized text metrics dashboard.

total_bookings = 0
paid_bookings = 0
pending_bookings = 0
cancelled_bookings = 0
total_revenue = 0
service_frequency = {}

with open('payments.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_bookings += 1
        status = row.get("STATUS", "").strip().lower()
        amount = float(row.get("AMOUNT", 0))
        service = row.get("SERVICE", "Unknown").strip()
        
        if status == "paid" or status == "success":
            paid_bookings += 1
            total_revenue += amount
        elif status == "pending":
            pending_bookings += 1
        elif status == "cancelled" or status == "failed":
            cancelled_bookings += 1
            
        service_frequency[service] = service_frequency.get(service, 0) + 1

avg_amount = total_revenue / total_bookings if total_bookings > 0 else 0
top_service = max(service_frequency, key=service_frequency.get) if service_frequency else "N/A"

print("Booking Summary Report")
print(f"Total bookings: {total_bookings}")
print(f"Paid bookings: {paid_bookings}")
print(f"Pending bookings: {pending_bookings}")
print(f"Cancelled bookings: {cancelled_bookings}")
print(f"Total revenue: {total_revenue}")
print(f"Average booking amount: {avg_amount:.2f}")
print(f"Top service: {top_service}")