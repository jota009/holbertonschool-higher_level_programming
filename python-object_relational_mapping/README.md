PYTHON ORM
# 🐍 Python & ORM with MySQL

## 🌟 Introduction

In this module, you’ll learn how to bridge Python applications and MySQL databases using both raw connectors and Object-Relational Mapping (ORM). You’ll see how to perform basic CRUD operations from Python scripts and how ORMs simplify database interactions by mapping classes to tables.

---

## 📚 Learning Objectives

* **Connecting to MySQL from Python:** Use MySQLdb or mysql-connector to establish a database connection.
* **Selecting Rows via Python:** Execute `SELECT` queries and fetch results.
* **Inserting Rows via Python:** Perform `INSERT` operations programmatically.
* **What is ORM?** Understand Object-Relational Mapping and its benefits.
* **Mapping Classes to Tables:** Define Python classes that represent database tables using an ORM (e.g., SQLAlchemy).

---

## 🔌 Connecting & CRUD with Python

### 1. Connect to MySQL

```python
import MySQLdb

# Establish connection
db = MySQLdb.connect(
    host="localhost", user="username",
    passwd="password", db="hbnb_clone"
)
cursor = db.cursor()
```

### 2. SELECT Rows

```python
cursor.execute("SELECT id, name FROM users WHERE active=1;")
rows = cursor.fetchall()
for row in rows:
    print(f"User {row[0]}: {row[1]}")
```

### 3. INSERT Rows

```python
cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s)",
    ("Alice", "alice@example.com")
)
db.commit()
```

---

## 🔄 Object-Relational Mapping (ORM)

* **Definition:** A technique that lets you interact with your database using Python objects instead of SQL strings.
* **Benefits:** Cleaner code, automated SQL generation, easier migrations, and model reuse.

---

## 🧩 Mapping Python Classes to Tables

### SQLAlchemy Example

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True)

# Engine & Session
engine = create_engine('mysql+mysqldb://username:password@localhost/hbnb_clone')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables\ nBase.metadata.create_all(engine)

# Create & add a user
new_user = User(name='Bob', email='bob@example.com')
session.add(new_user)
session.commit()

# Query users
for user in session.query(User).filter_by(active=True):
    print(user.name)
```

---

## 🚀 What I Learned

* Establishing database connections in Python
* Executing raw SQL queries for SELECT and INSERT
* Understanding the ORM pattern and its advantages
* Defining Python classes mapped to database tables
* Using an ORM’s session for object CRUD operations

---

## 📖 Resources

* [MySQLdb Documentation](https://mysqlclient.readthedocs.io/)
* [SQLAlchemy Official Docs](https://docs.sqlalchemy.org/)
* Real Python: [Intro to Python ORMs](https://realpython.com/python-orms/)

---

✍️ **Author**
**Josniel Ramos**
GitHub: [@jota009](https://github.com/jota009)
