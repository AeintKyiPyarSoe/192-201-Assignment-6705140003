# Assignment 03 — CHANGES

**Name:** Aeint Kyi Pyar Soe  **Student ID:** 6705140003

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products stored as bare tuples with index access `("Laptop", 1200.0, "electronics")` | `Product` class storing `name`, `price`, `category`, with validation in `__init__` | Classes / Encapsulation | Ran `python Assignment_03.py` → PASS |
| 2 | Items stored as raw index-quantity pairs `(0, 1)` | `OrderItem` class that holds a `Product` object and `quantity`, with `line_total()` | Composition (has-a) | Ran `python Assignment_03.py` → PASS |
| 3 | Repeated `if tier == ...` chains for tier discount and points | Base `Customer` class with `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses | Inheritance & Polymorphism | Ran `python Assignment_03.py` → PASS |
| 4 | `calc()` function mixed math calculations together with `print()` receipt output | `Order` class with pure calculation methods (`subtotal`, `discount`, `tax`, `total`, `points`) and separate `receipt()` formatting | Pure functions / Separation of concerns | Ran `python Assignment_03.py` → PASS |
| 5 | Hardcoded tax check in loop: `if cat == "food": ... else: ...` | Moved tax calculation to `Product.tax(amount)` so each product calculates its own tax | Encapsulation | Ran `python Assignment_03.py` → PASS |
| 6 | Magic numbers (`0.07`, `100`, `10`, `0.03`) and mutable `global TAXRATE` | Defined named constants (`TAX_RATE`, `DISCOUNT_THRESHOLD`, `BULK_QTY_THRESHOLD`, etc.) and removed `global` | Clean code / Constants | Ran `python Assignment_03.py` → PASS |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

> The change that improved the code the most was replacing the `if tier == ...` chains with customer subclasses and polymorphism. It removed repeated conditional checks and makes it easy to add new membership tiers later without modifying existing order code. Separating calculations from receipt printing also made the methods pure, readable, and easy to test. Keeping the behaviour identical forced me to be careful with the discount rules, especially adding the 3% bulk discount to the tier discount when total quantity reached 10. I also had to make sure points used integer division (`total // 10`) before multiplying by the customer multiplier, and that receipt lines and spacing matched the original output exactly.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | *"Help me create Product and OrderItem classes to replace the tuples"* | Suggested `Product` and `OrderItem` classes with constructor validation and `line_total()` | Accepted; kept validation checks simple and clear | Tested instantiating objects and ran `python Assignment_03.py` |
| 2 | *"How do I replace the tier if/elif discount and points with polymorphism?"* | Base `Customer` class with `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses | Edited (added `create_customer()` helper to map tier strings to classes) | Self-test PASS; verified discount rates match table |
| 3 | *"Help me write Order class so calculation methods return numbers instead of printing"* | Created pure methods `subtotal()`, `discount()`, `tax()`, `total()`, `points()`, and separate `receipt()` | Accepted; checked receipt string format against original receipts | Ran `python Assignment_03.py` → PASS |
| 4 | *"Find magic numbers and global variables to clean up"* | Named constants like `TAX_RATE`, `BULK_QTY_THRESHOLD`, `DISCOUNT_THRESHOLD`, and removed `global` | Accepted directly | Read through code and confirmed PASS on self-test |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] No tuples / parallel lists left — products, orders, and items are objects.
- [x] No `if tier == ...` chains — tiers are a class family.
- [x] Calculation methods **return** values and do not `print`; printing is separate.
- [x] Constructors validate state; no leftover `global`; magic numbers are named.
- [x] The change table and reflection above are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
