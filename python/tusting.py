# One row from a customer table
customer = {
     "name" :"rolic",
    "city": "kanpur",
    "orders": 12,
    "total_spent": 4500 }


# Look up specific columns by name
print("Customer:", customer["name"])
print("city:", customer["city"])
print("Spent:", customer["total_spent"])

# Add a new calculated column
customer["avg_order"] = customer["total_spent"] / customer["orders"]
print("Average Order Value:", customer["avg_order"])
