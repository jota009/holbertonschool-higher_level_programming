# 🔐 MySQL More Queries

## 🌟 Introduction

In this module, you’ll learn how to manage MySQL users, enforce data integrity with keys and constraints, and perform advanced queries that span multiple tables. Mastering these concepts ensures secure access control and powerful data retrieval for your HBnB application.

---

## 📚 Learning Objectives

* **Creating MySQL Users:** Add new users to your database with custom credentials.
* **Managing Privileges:** Grant or revoke permissions on databases and tables.
* **Primary & Foreign Keys:** Define unique identifiers and relationships between tables.
* **NOT NULL & UNIQUE Constraints:** Enforce mandatory fields and uniqueness.
* **Multi-Table Queries:** Retrieve data from related tables in a single request.
* **Subqueries:** Nest queries for intermediate filtering and calculations.
* **JOIN vs UNION:** Combine rows from multiple tables (JOIN) or stack results from separate queries (UNION).

---

## 🛠️ User & Privilege Management

### 1. Create a New MySQL User

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'strong_password';
```

*Example:* `CREATE USER 'hbnb_user'@'localhost' IDENTIFIED BY 'P@ssw0rd';`

### 2. Grant & Revoke Privileges

```sql
-- Grant all on a specific database\NGRANT ALL PRIVILEGES ON hbnb_clone.* TO 'hbnb_user'@'localhost';

-- Revoke UPDATE privilege on a table
REVOKE UPDATE ON hbnb_clone.properties FROM 'hbnb_user'@'localhost';
```

*Tip:* Use `FLUSH PRIVILEGES;` to apply changes immediately.

---

## 🔑 Keys & Constraints

### 3. PRIMARY KEY

Uniquely identifies each row in a table.

```sql
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  name VARCHAR(100),
  PRIMARY KEY (id)
);
```

### 4. FOREIGN KEY

Enforces referential integrity between tables.

```sql
CREATE TABLE bookings (
  id INT AUTO_INCREMENT,
  user_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 5. NOT NULL & UNIQUE Constraints

```sql
CREATE TABLE listings (
  id       INT AUTO_INCREMENT PRIMARY KEY,
  address  VARCHAR(255) NOT NULL,
  code     VARCHAR(50) UNIQUE
);
```

* **NOT NULL:** Prevents NULL values.
* **UNIQUE:** Ensures all values are distinct.

---

## 🔍 Advanced Query Techniques

### 6. Retrieving Data from Multiple Tables

* **JOIN**: Combine columns from related tables.

```sql
SELECT u.name, b.start_date, b.end_date
FROM bookings b
JOIN users u ON b.user_id = u.id;
```

* **UNION**: Stack results from separate `SELECT` queries (must have same column structure).

```sql
SELECT name AS entity, created_at FROM users
UNION
SELECT title AS entity, created_at FROM properties;
```

### 7. Subqueries

Use nested queries for filtering or aggregation.

```sql
-- Properties with bookings count > 3
SELECT *
FROM properties
WHERE id IN (
  SELECT property_id
  FROM bookings
  GROUP BY property_id
  HAVING COUNT(*) > 3
);
```

---

## 🚀 What I Learned

* How to create and secure MySQL users
* Granting fine-grained privileges
* Defining primary and foreign keys for data integrity
* Using constraints to enforce field rules
* Writing JOINs and UNIONs for complex data retrieval
* Employing subqueries to simplify multi-step logic

---

## 📖 Resources

* [MySQL User Account Management](https://dev.mysql.com/doc/refman/8.0/en/user-account-management.html)
* [MySQL JOIN Syntax](https://dev.mysql.com/doc/refman/8.0/en/join.html)
* [MySQL Subquery Optimization](https://dev.mysql.com/doc/refman/8.0/en/subquery-optimization.html)

---

✍️ **Author**
**Josniel Ramos**
GitHub: [@jota009](https://github.com/jota009)
