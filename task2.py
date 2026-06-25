# Approach:
# For counting occurrences dynamically without hardcoding keys, we use 
# standard dictionaries. To find specific records like max amount, we
# utilize Python's built-in 'max()' function with a key parameter.

from bookings import bookings 

print("--- 1. Count Bookings by Service ---")
service_counts = {}
for r in bookings:
    service_counts[r["service"]] = service_counts.get(r["service"], 0) + 1
print(service_counts)

print("\n--- 2. Count Bookings by Status (Paid vs Pending) ---")
status_counts = {"paid": 0, "pending": 0}
for r in bookings:
    if r["status"] in status_counts:
        status_counts[r["status"]] += 1
print(status_counts)

print("\n--- 3. Booking with the Highest Amount ---")
highest_booking = max(bookings, key=lambda x: x["amount"])
print(highest_booking)

print("\n--- 4. Customers who booked 'Visa' ---")
for r in bookings:
    if r["service"] == "Visa":
        print(r["customer"])

print(f"\n--- 5. Average Booking Amount ---\n{sum(r['amount'] for r in bookings) / len(bookings)}")
