
# Tuple-Based Product Catalogue Audit

print("==========================================")
print("       PRODUCT CATALOGUE AUDIT")
print("==========================================")

# Product tuple format:
# (Product ID, Price, Stock Quantity)

products = [
    ("P101", 250.0, 10),
    ("P102", 120.0, 3),
    ("P103", -50.0, 8),
    ("", 80.0, 5),
    ("P104", 500.0, 0),
    ("P105", 75.0, 12)
]

# Minimum stock level
reorder_level = 5

# Initialize variables
total_inventory_value = 0
valid_count = 0
invalid_count = 0

valid_products = []
invalid_products = []
replenishment_products = []

# Audit each product
print("\nPRODUCT VALIDATION REPORT")

for product in products:

    product_id, price, quantity = product
    errors = []

    # Validate product ID
    if not isinstance(product_id, str) or product_id.strip() == "":
        errors.append("Invalid Product ID")

    # Validate price
    if not isinstance(price, (int, float)) or price <= 0:
        errors.append("Invalid Price")

    # Validate stock quantity
    if not isinstance(quantity, int) or quantity < 0:
        errors.append("Invalid Stock Quantity")

    # Check product record
    if len(errors) == 0:

        valid_count += 1
        valid_products.append(product)

        # Calculate inventory value
        inventory_value = price * quantity
        total_inventory_value += inventory_value

        print("\nProduct ID:", product_id)
        print("Price: Rs.", price)
        print("Stock Quantity:", quantity)
        print("Inventory Value: Rs.", inventory_value)
        print("Status: Valid")

        # Check replenishment requirement
        if quantity <= reorder_level:
            replenishment_products.append(product)

    else:

        invalid_count += 1
        invalid_products.append((product, errors))

        print("\nProduct Record:", product)
        print("Status: Invalid")

        for error in errors:
            print("-", error)

# Display valid products
print("\n==========================================")
print("          VALID PRODUCTS")
print("==========================================")

for product in valid_products:
    print(product)

# Display invalid products
print("\n==========================================")
print("          INVALID PRODUCTS")
print("==========================================")

for product, errors in invalid_products:
    print(product, ":", ", ".join(errors))

# Display replenishment list
print("\n==========================================")
print("       REPLENISHMENT REQUIRED")
print("==========================================")

if len(replenishment_products) > 0:

    for product in replenishment_products:
        print("Product ID:", product[0])
        print("Available Stock:", product[2])
        print("Required Action: Replenish stock")

else:
    print("No products require replenishment.")

# Final summary
print("\n==========================================")
print("          INVENTORY SUMMARY")
print("==========================================")

print("Total Product Records:", len(products))
print("Valid Products:", valid_count)
print("Invalid Products:", invalid_count)

print("Total Inventory Value: Rs.",
      round(total_inventory_value, 2))

print("Products Requiring Replenishment:",
      len(replenishment_products))

print("\n==========================================")
print("          AUDIT COMPLETED")
print("==========================================")
