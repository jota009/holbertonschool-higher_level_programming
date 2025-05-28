# Python - Inheritance 🔗🐍

## 📚 Resources

- Official Python tutorial on [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- Real Python guide on [Multiple Inheritance](https://realpython.com/python3-object-oriented-programming/#multiple-inheritance)
- Holberton School’s **Learn to Program 10: Inheritance & Magic Methods**

## 🎯 Learning Objectives

- **Superclass / Base class / Parent class** vs **Subclass**
- How to inspect all attributes and methods of a class or instance
- When and how an instance can receive new attributes dynamically
- How to declare a class that inherits from one or multiple base classes
- The default parent of all Python classes (`object`)
- How to override inherited methods or attributes
- Which members are available to subclasses by default
- The purpose and benefits of inheritance
- When and how to use `isinstance`, `issubclass`, `type` and `super()`

## ⚙️ Requirements

- **Editors**: `vi`, `vim`, or `emacs`
- **Interpreter**: Ubuntu 20.04 LTS with Python 3.8.5
- All files must:
  - End with a single newline
  - Start with `#!/usr/bin/python3`
  - Be PEP8‐compliant (tested with `pycodestyle` v2.7.*)
  - Be executable and have their length verified by `wc`

## 🛠️ Examples

### 1. Exact class check (`is_same_class`)

```python
>>> from is_same_class import is_same_class
>>> class A: pass
>>> class B(A): pass

>>> is_same_class(A(), A)
True
>>> is_same_class(B(), A)    # subclasses don’t match exactly
False
