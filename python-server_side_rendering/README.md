# Server‑Side Rendering with Flask & Jinja

## 🚀 Project Overview

Learn how to build **SEO‑friendly**, **efficient** web applications using **Server‑Side Rendering (SSR)** with Python’s Flask framework and the Jinja templating engine. Over **5 tasks**, you’ll:
• Generate files from templates,
• Render static and dynamic pages,
• Load data from JSON, CSV, and SQLite,
• Handle query parameters and errors—all with reusable components.

---

## 🎯 Learning Objectives

* Understand **SSR** vs. client‑side rendering
* Scaffold a **Flask** application with multiple routes
* Create **Jinja** templates and reusable includes
* Read and display data from **JSON**, **CSV**, and **SQLite** sources
* Use **query parameters** to filter content
* Implement robust **error handling** and user feedback

---

## 🗂️ Task Breakdown

|  Task | Goal                                      | Key Techniques                                           |
| :---: | :---------------------------------------- | :------------------------------------------------------- |
| **0** | **Invitation Generator**                  | Python string `.replace()`, file I/O, error checks       |
| **1** | **Basic Flask Templates**                 | `Flask` routes, `render_template`, `{% include %}`       |
| **2** | **Dynamic Lists with Loops & Conditions** | Jinja `{% for %}`, `{% if %}`                            |
| **3** | **JSON & CSV Data Display**               | Python `json`, `csv`, `request.args`, unified template   |
| **4** | **SQLite Integration**                    | `sqlite3` queries, multi‑source logic, DB error handling |

---

## 🛠️ Project Structure

```
python-server_side_rendering/
├─ create_db.py         # Creates & populates products.db
├─ products.db          # SQLite database
├─ products.json        # JSON data source
├─ products.csv         # CSV data source
├─ task_00_intro.py     # Invitation template generator
├─ task_01_jinja.py     # Flask app: static + reusable templates
├─ task_02_logic.py     # Flask: dynamic loops & conditions
├─ task_03_files.py     # Flask: JSON/CSV data + filtering
├─ task_04_db.py        # Flask: JSON/CSV/SQL multi-source
└─ templates/
   ├─ header.html
   ├─ footer.html
   ├─ index.html
   ├─ about.html
   ├─ contact.html
   ├─ items.html
   └─ product_display.html
```

---

## 💡 Key Concepts & Tips

* **Jinja Includes**: Use `{% include 'header.html' %}` to DRY up your layouts.
* **Template Logic**: `{% for %}` loops and `{% if %}` guard against empty data.
* **Error Feedback**: Pass an `error` var to templates to surface issues cleanly.
* **Multi‑Source Routing**: Branch on `request.args.get('source')` for flexibility.
* **Database Safety**: Always `finally: conn.close()` and catch `sqlite3.Error`.

---

## ▶ Quick Start

1. **Clone Repo**

   ```bash
   git clone https://github.com/yourusername/python-server_side_rendering.git
   cd python-server_side_rendering
   ```
2. **Install Flask**

   ```bash
   pip install Flask
   ```
3. **Prepare Database**

   ```bash
   python3 create_db.py
   ```
4. **Run App**

   ```bash
   python3 task_04_db.py
   ```
5. **Explore**

   * `/` → Home
   * `/about` → About Us
   * `/contact` → Contact Us
   * `/items` → Items List
   * `/products?source=json`
   * `/products?source=csv&id=2`
   * `/products?source=sql`

---

## 🙋‍♂️ Author

**Josniel Ramos**
