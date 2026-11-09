# Exercise 1: One customer
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and add
print("--- Exercise 2 ---")
customer["phone"] = "555-0100"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# Exercise 3: Safe lookup
print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError:
    print("KeyError: 'email' is not in the dictionary")

# Exercise 4: Iterate
print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")
# Looping without .items() gives only the keys, not the values.
for key in customer:
    print(key)


# Exercise 5: Lookup table
print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}
rate = tier_discounts.get(customer["tier"], 0)
final_price = 200 * (1 - rate)
print(f"Tier: {customer['tier']}")
print(f"Discount: {rate * 100:.0f}%")
print(f"Final price: ${final_price:.2f}")

# Exercise 6: List of dicts
print("--- Exercise 6 ---")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Cara", "tier": "bronze"},
]
for c in customers:
    discount = 300 * tier_discounts.get(c["tier"], 0)
    print(f"{c['name']} ({c['tier']}): ${discount:.2f} discount on $300")

# Exercise 7: Nested catalog
print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} ({info['stock']} left)")

# Exercise 8: Sales by region
print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
totals = {}
for t in transactions:
    totals[t["region"]] = totals.get(t["region"], 0) + t["amount"]
for region in sorted(totals):
    print(f"{region}: {totals[region]}")
