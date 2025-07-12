# 🚀 JavaScript Warm Up

Welcome to the **JavaScript Warm Up** project!
This set of exercises introduces the foundations of JavaScript programming using Node.js. You’ll practice variables, functions, loops, modules, argument parsing, and more—all with best practices and modern syntax.

---

## 📚 What You’ll Learn

* Declaring variables with `const` and `let`
* Printing output with `console.log`
* Parsing and validating command‑line arguments
* Using loops (`for`, `while`) and arrays
* Creating and updating objects
* Writing functions and exporting them as modules
* Basic input validation and error handling

---

## 🖥️ Getting Started

### Prerequisites

* **Ubuntu 20.04 LTS**
* **Node.js v14.x**
* **semistandard** code linter

### Setup Instructions

```bash
# Install Node.js 14
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install semistandard globally
sudo npm install semistandard --global
```

---

## 📂 Project Structure

```
javascript-warm_up/
├── 0-javascript_is_amazing.js
├── 1-multi_languages.js
├── 2-arguments.js
├── 3-value_argument.js
├── 4-concat.js
├── 5-to_integer.js
├── 6-multi_languages_loop.js
├── 7-multi_c.js
├── 8-square.js
├── 9-add.js
├── 10-factorial.js
├── 11-second_biggest.js
├── 12-object.js
├── 13-add.js
└── README.md
```

---

## 📝 Usage Examples

Each script is **executable** and starts with the shebang `#!/usr/bin/node`.
Run them from your terminal like this:

```bash
./0-javascript_is_amazing.js
./2-arguments.js Hello World
./7-multi_c.js 3
./8-square.js 4
./10-factorial.js 5
./11-second_biggest.js 1 2 3 4 5
```

---

## ✨ Highlights & Best Practices

* **No `var`** – only `const` and `let` are used.
* **Command‑line arguments** – accessed with `process.argv` and parsed as needed.
* **Code Style** – all scripts pass `semistandard` linter checks.
* **Input Validation** – scripts handle missing or invalid inputs gracefully.
* **Reusable Code** – functions and modules improve clarity and maintainability.

---

## 👨‍💻 Author

**Josniel Ramos**
Holberton School
[GitHub @jota009](https://github.com/jota009)

---
