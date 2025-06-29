# 🗄️ SQL & Relational Databases

## 🌟 Introduction

Welcome to the SQL project for HBnB! In this module, you’ll learn how to design, manipulate, and query relational databases using MySQL. Databases power every web application—like HBnB—by storing users, listings, bookings, and more in organized tables you can efficiently search and modify.

---

## 📚 Learning Objectives

* **What’s a database?**
  A structured collection of related information (think of a spreadsheet: rows = records, columns = fields).

* **What’s a relational database?**
  A database that splits data into multiple tables linked by relationships (e.g., linking a `users` table to a `bookings` table via `user_id`).

* **What does SQL stand for?**
  **Structured Query Language**, the standard language for interacting with relational databases.

* **What’s MySQL?**
  A popular open-source relational database management system (RDBMS) that implements SQL.

* **How to create a database in MySQL:**

  ```sql
  CREATE DATABASE hbnb_clone;
  USE hbnb_clone;
  ```

* **What do DDL and DML stand for?**

  * **DDL (Data Definition Language):** Commands for defining or modifying database structure (`CREATE`, `ALTER`, `DROP`).
  * **DML (Data Manipulation Language):** Commands for manipulating data within tables (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).

* **How to CREATE or ALTER a table:**

  ```sql
  -- Create a table
  CREATE TABLE properties (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    title    VARCHAR(100) NOT NULL,
    price    DECIMAL(10,2) NOT NULL
  );

  -- Add a new column later
  ALTER TABLE properties
    ADD COLUMN bedrooms INT DEFAULT 1;
  ```

* **How to SELECT data from a table:**

  ```sql
  SELECT id, title, price
  FROM properties
  WHERE price < 100
  ORDER BY price ASC;
  ```

* **How to INSERT, UPDATE, or DELETE data:**

  ```sql
  -- Insert
  INSERT INTO properties (title, price, bedrooms)
  VALUES ('Cozy Cottage', 75.00, 2);

  -- Update
  UPDATE properties
  SET price = 80.00
  WHERE id = 1;

  -- Delete
  DELETE FROM properties
  WHERE id = 1;
  ```

* **What are subqueries?**
  Queries nested inside another query to filter or compute based on intermediate results.

  ```sql
  -- Find users with more than 5 bookings
  SELECT *
  FROM users
  WHERE id IN (
    SELECT user_id
    FROM bookings
    GROUP BY user_id
    HAVING COUNT(*) > 5
  );
  ```

* **How to use MySQL functions:**
  Built-in tools to transform or compute on data, e.g.:

  * `NOW()` → current timestamp
  * `COUNT(*)` → total row count
  * `CONCAT(first_name, ' ', last_name)` → string concatenation

---

## 🔄 Typical SQL Workflow

1. **Define schema** (DDL): `CREATE TABLE`, `ALTER TABLE`
2. **Insert data** (DML): `INSERT INTO`
3. **Query data:** `SELECT … FROM … WHERE …`
4. **Update/Delete:** `UPDATE … SET …`, `DELETE FROM …`
5. **Advanced queries:** JOINs, subqueries, aggregate functions

---

## 🚀 What I Learned

* Designing normalized schemas to avoid data duplication
* Differentiating DDL vs. DML commands
* Crafting basic and complex `SELECT` queries with filtering, sorting, and joining
* Managing data using `INSERT`, `UPDATE`, `DELETE`
* Nesting queries with subqueries for advanced filtering
* Utilizing MySQL functions for data transformation and aggregation

---

## 📖 Resources

* [MySQL Official Documentation](https://dev.mysql.com/doc/)
* MDN: [Introduction to SQL](https://developer.mozilla.org/en-US/docs/Glossary/SQL)
* W3Schools: [SQL Tutorial](https://www.w3schools.com/sql/)
* SQLBolt: [Interactive SQL Exercises](https://sqlbolt.com/)

---

✍️ **Author**
**Josniel Ramos**
GitHub: [@jota009](https://github.com/jota009)
