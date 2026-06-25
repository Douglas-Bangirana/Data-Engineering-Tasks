# Approach:
# Encapsulate the core data retrieval logic into clear, single-responsibility 
# functions. We leverage list comprehensions and dictionary tracking to 
# keep code modular and cleanly reusable.

def get_paid_bookings(bookings):
    return [r for r in bookings if r["status"] == "paid"]

def calculate_total_revenue(bookings):
    return sum(r["amount"] for r in bookings)

def calculate_paid_revenue(bookings):
    return sum(r["amount"] for r in bookings if r["status"] == "paid")

def count_by_service(bookings):
    counts = {}
    for r in bookings:
        counts[r["service"]] = counts.get(r["service"], 0) + 1
    return counts

def find_booking_by_customer(bookings, customer_name):
    return [r for r in bookings if r["customer"].lower() == customer_name.lower()]