# 🏷️ Python – More Classes and Objects

![Project Status](https://img.shields.io/badge/status-100%25-brightgreen)

This project dives deep into Python’s object-oriented features: defining classes, managing attributes and methods, and leveraging special (“dunder”) methods, properties, class/static methods, and more. We built and tested a `Rectangle` class through successive iterations, culminating in factories, comparison utilities, and instance counting.

---

## 📚 Resources

Read or watch the following (stop at “Inheritance” where indicated):

- **“Object Oriented Programming”** (read through “Inheritance” *excluded*)
- **“Object-Oriented Programming”** by Real Python (only these sections):
  - General Introduction
  - First-class Everything
  - A Minimal Class in Python
  - Attributes
  - Methods
  - The `__init__` Method
  - Data Abstraction, Data Encapsulation, and Information Hiding
  - `__str__`- and `__repr__`-Methods
  - Public/Protected/Private Attributes
  - Destructor
- **Class and Instance Attributes**
- **`classmethod` and `staticmethod`**
- **Properties vs. Getters and Setters** (focus on “Public instead of Private Attributes”)
- **`str` vs. `repr`**

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain and implement:

1. **Why Python programming is awesome**
2. **What is OOP** and **“first-class everything”**
3. **Classes vs. Objects/Instances**
4. **Attributes**: public, protected (`_attr`), private (`__attr`)
5. **The `self`** reference
6. **Methods**, including the **`__init__`** constructor
7. **Data Abstraction**, **Encapsulation**, **Information Hiding**
8. **Properties** vs. plain attributes; Pythonic getters/setters
9. **Special methods**:
   - `__str__` vs. `__repr__` (differences and use cases)
   - `__del__` (destructor)
10. **Class attributes** vs. **instance attributes**
11. **`@classmethod`** and **`@staticmethod`**
12. **Dynamic attribute creation** on classes and instances
13. **Attribute binding** and the **`__dict__`** of classes/instances
14. **Lookup order** for attributes in Python’s MRO
15. **Using `getattr(obj, "name")`** for dynamic access

---

## ✅ Tasks Completed

We incrementally built and tested a fully featured `Rectangle` class, including:

- **0-rectangle.py**: Empty class scaffold
- **1-rectangle.py**: Private `size` attribute with validation
- **2-rectangle.py**: `area()` method
- **3-rectangle.py**: `__str__` and `__repr__` implementations
- **4-rectangle.py**: `my_print()` and `__del__()` with goodbye message
- **5-rectangle.py**: `number_of_instances` counter
- **6-rectangle.py**: Custom `print_symbol` for drawing
- **7-rectangle.py**: `bigger_or_equal(rect_1, rect_2)` static method
- **8-rectangle.py**: `square(cls, size=0)` class-method factory

Each version reinforced OOP principles, special methods, properties, and class/static methods.

---

✍️ **Author**
**Josniel Ramos** • Student at Holberton School
GitHub: [@jota009](https://github.com/jota009)
