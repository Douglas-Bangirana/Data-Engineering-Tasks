# Approach:
# Processes the payments dataset. We use filters to check specific conditions
# (like tracking string matches for 'success' or 'failed') and isolate key 
# consumer behavior metrics.
from payments import payments 

print(f"1. Total successful payments: {sum(1 for p in payments if p['status'] == 'success')}")
print(f"2. Total failed payments: {sum(1 for p in payments if p['status'] == 'failed')}")
print(f"3. Total amount from successful: {sum(p['amount'] for p in payments if p['status'] == 'success')}")

highest_payment = max(payments, key=lambda x: x["amount"])
print(f"4. Customer with highest payment: {highest_payment['customer']} (${highest_payment['amount']})")

print("5. Payments by method:")
method_counts = {}
for p in payments:
    method_counts[p["method"]] = method_counts.get(p["method"], 0) + 1
print(method_counts)

print("6. All failed payments:")
failed_payments = [p for p in payments if p["status"] == "failed"]
print(failed_payments)
