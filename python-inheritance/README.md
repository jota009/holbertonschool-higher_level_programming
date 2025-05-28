<!-- Project badge: 100% -->

# Python - Inheritance 🔗🐍

## 📚 Resources

- Official Python tutorial on [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- Real Python guide on [Multiple Inheritance](https://realpython.com/python3-object-oriented-programming/#multiple-inheritance)
- Holberton School’s **Learn to Program 10 – Inheritance & Magic Methods**

---

## 🎯 Learning Objectives

By the end of this project, you’ll be able to explain to anyone—without Google:

- **Superclass / Base class / Parent class** vs **Subclass**
- How to list all attributes and methods of a class or instance
- When and how an instance can receive new attributes at runtime
- How to inherit a class from one or more base classes
- The default base of every Python class (`object`)
- How to override an inherited method or attribute
- Which members (attributes/methods) subclasses inherit by default
- The purpose and benefits of inheritance in OOP
- When and how to use the built-ins: `isinstance()`, `issubclass()`, `type()` and `super()`

---

## ⚙️ Requirements

- **Editors**: `vi`, `vim`, or `emacs`
- **Interpreter**: Ubuntu 20.04 LTS with Python 3.8.5
- All your files must:
  - End with a single newline
  - Start with the shebang `#!/usr/bin/python3`
  - Be executable (`chmod +x`)
  - Follow PEP8 styling (checked with `pycodestyle` v2.7.*)
  - Be measured by file-length checks via `wc`

---

## 🛠️ Quick Example

```python
#!/usr/bin/python3
class Animal:
    """Base class for all animals."""
    def speak(self):
        return "…sound…"

class Dog(Animal):
    """Dog subclass overrides speak()."""
    def speak(self):
        return "Woof!"

# Usage
d = Dog()
print(d.speak())  # → Woof!

---

✍️ **Author**
**Josniel Ramos** • Student at Holberton School
GitHub: [@jota009](https://github.com/jota009)
