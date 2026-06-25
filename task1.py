# Approach:
# We iterate over the in-memory 'bookings' list using simple loops,
# conditional 'if' statements, and basic aggregations (len, sum) 
# to isolate and print targeted metrics.

from bookings import bookings

print("--- 1. All Booking Records ---")
for record in bookings:
    print(record)

print("\n--- 2. Customer Names ---")
for record in bookings:
    print(record["customer"])

print(f"\n--- 3. Total Number of Bookings ---\n{len(bookings)}")

print("\n--- 4. Paid Bookings Only ---")
for record in bookings:
    if record["status"] == "paid":
        print(record)

print(f"\n--- 5. Total Amount for All Bookings ---\n{sum(r['amount'] for r in bookings)}")

print(f"\n--- 6. Total Amount for Paid Bookings Only ---\n{sum(r['amount'] for r in bookings if r['status'] == 'paid')}")

print("\n--- 7. Service Names for All Bookings ---")
for record in bookings:
    print(record["service"])
