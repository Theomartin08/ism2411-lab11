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

