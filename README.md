# product_catalogue_audit.py
# Tuple-Based Product Catalogue Audit

## Python Activity-Based Learning

### Student Details

- **Name:** DURGA SURYA PRAVALLIKA
- **Roll Number:** N26V01A0383
- **Branch:** CSE
- **Section:** 5
- **Programming Language:** Python

---

## 1. Problem Statement

Tuple-Based Product Catalogue Audit is a Python-based program that stores product identifiers, prices and stock quantities using tuples.

The program validates product records, detects invalid entries, calculates the total inventory value and identifies products that require replenishment based on their available stock.

## 2. Objectives

- To store product information using tuples.
- To validate product identifiers.
- To check product prices and stock quantities.
- To detect invalid product records.
- To calculate the total inventory value.
- To identify products with low stock.
- To generate a complete inventory audit report.

## 3. Assumptions

1. Each product record contains a product ID, price and stock quantity.
2. Product details are stored using tuples.
3. Product IDs must not be empty.
4. Product prices must be greater than zero.
5. Stock quantities must be non-negative integers.
6. The minimum stock level is 5 units.
7. Products with stock quantities less than or equal to 5 require replenishment.
8. Invalid product records are excluded from inventory calculations.

## 4. Algorithm

1. Start the program.
2. Initialize the product records using tuples.
3. Set the minimum stock level to 5.
4. Initialize inventory value and product counters.
5. Read each product tuple.
6. Extract product ID, price and stock quantity.
7. Validate the product ID.
8. Validate the price.
9. Validate the stock quantity.
10. If any field is invalid, display the error and reject the record.
11. Otherwise, calculate the product inventory value.
12. Add the value to the total inventory value.
13. Check whether the stock quantity is below or equal to the minimum stock level.
14. If yes, add the product to the replenishment list.
15. Display valid and invalid products.
16. Display products requiring replenishment.
17. Display the final inventory summary.
18. Stop the program.

## 5. Pseudocode

```text
START

INITIALIZE product tuples

SET reorder_level = 5

INITIALIZE:
    total_inventory_value = 0
    valid_count = 0
    invalid_count = 0

FOR each product

    EXTRACT product ID, price, quantity

    INITIALIZE errors list

    IF product ID is empty
        ADD ID error
    END IF

    IF price <= 0
        ADD price error
    END IF

    IF quantity < 0
        ADD quantity error
    END IF

    IF errors list is empty

        MARK product as valid

        CALCULATE inventory value
        ADD value to total inventory value

        IF quantity <= reorder_level
            ADD product to replenishment list
        END IF

    ELSE

        MARK product as invalid
        DISPLAY errors

    END IF

END FOR

DISPLAY valid products
DISPLAY invalid products
DISPLAY replenishment products

DISPLAY total inventory value
DISPLAY product counts

STOP
```

## 6. Python Source Code

**File name:** `product_catalogue_audit.py`

The complete Python implementation is available in this folder.

## 7. Test Cases

| Test Case | Product ID | Price | Quantity | Expected Result |
|---|---|---:|---:|---|
| 1 | P101 | 250 | 10 | Valid |
| 2 | P102 | 120 | 3 | Replenishment required |
| 3 | P103 | -50 | 8 | Invalid price |
| 4 | Empty | 80 | 5 | Invalid product ID |
| 5 | P104 | 500 | 0 | Replenishment required |
| 6 | P105 | 75 | 12 | Valid |
| 7 | P106 | 100 | -2 | Invalid stock quantity |

## 8. Expected Output

```text
PRODUCT CATALOGUE AUDIT

Total Product Records: 6
Valid Products: 4
Invalid Products: 2

Total Inventory Value: Rs. 3760.0

REPLENISHMENT REQUIRED

Product ID: P102
Available Stock: 3

Product ID: P104
Available Stock: 0

Products Requiring Replenishment: 2

AUDIT COMPLETED
```

## 9. Conclusion

The Tuple-Based Product Catalogue Audit program successfully stores and analyses product information using Python tuples. It identifies invalid records, calculates inventory values and detects products that require replenishment.

This project helps us understand Python variables, tuples, lists, conditional statements, loops, operators and basic data validation. It also demonstrates how Python can be used to manage and audit product inventory.

---

**Project:** Python Activity-Based Learning  
**Topic:** Tuple-Based Product Catalogue Audit
