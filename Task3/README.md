# Task 3: College Club Membership Management System

**Student:** Aayush Kadel (Student ID: 250573)  
**Module:** ST4015CMD — Foundation of Computer Science  
**College:** Softwarica College of IT & E-Commerce (in collaboration with Coventry University)  
**Submitted To:** Rupak Rajbanshi  

---

## Overview

This task demonstrates the full database design process for a College Club Membership Management System. A poorly structured flat table was analysed, normalised through 1NF, 2NF and 3NF, modelled using an ER diagram, and implemented using MySQL with SQL queries.

---

## Files in This Folder

| File | Description |
|------|-------------|
| `schema.sql` | Creates the three normalised tables: Student, Club, Membership |
| `insert.sql` | Seeds all student, club and membership data from the report |
| `queries.sql` | SELECT and INNER JOIN queries for Task 4 and Task 5 |
| `image/ER Diagram - College Club Membership Database (3NF).png` | Entity Relationship Diagram in Chen notation (Task 3) |

---

## Database Schema (3NF)

Three tables were produced after normalisation:

**Student**
| Column | Type | Constraint |
|--------|------|------------|
| StudentID | INT | PRIMARY KEY |
| StudentName | VARCHAR(100) | NOT NULL |
| Email | VARCHAR(150) | UNIQUE, NOT NULL |

**Club**
| Column | Type | Constraint |
|--------|------|------------|
| ClubID | VARCHAR(10) | PRIMARY KEY |
| ClubName | VARCHAR(100) | NOT NULL |
| ClubRoom | VARCHAR(50) | |
| ClubMentor | VARCHAR(100) | |

**Membership**
| Column | Type | Constraint |
|--------|------|------------|
| MembershipID | VARCHAR(10) | PRIMARY KEY |
| StudentID | INT | FOREIGN KEY → Student |
| ClubID | VARCHAR(10) | FOREIGN KEY → Club |
| JoinDate | DATE | |

---

## How to Run

Make sure you have **MySQL 8.0** installed. Run the files in this exact order:

**Step 1 — Create the tables:**
```bash
mysql -u root -p < schema.sql
```

**Step 2 — Insert the data:**
```bash
mysql -u root -p < insert.sql
```

**Step 3 — Run the queries:**
```bash
mysql -u root -p < queries.sql
```

Or open each file inside **MySQL Workbench** and execute them one by one in the same order.

---

## Expected Output

### Display all students
| StudentID | StudentName | Email |
|-----------|-------------|-------|
| 1 | Asha | asha@email.com |
| 2 | Bikash | bikash@email.com |
| 3 | Nisha | nisha@email.com |
| 4 | Rohan | rohan@email.com |
| 5 | Suman | suman@email.com |
| 6 | Pooja | pooja@email.com |
| 7 | Aman | aman@email.com |

### Display all clubs
| ClubID | ClubName | ClubRoom | ClubMentor |
|--------|----------|----------|------------|
| C1 | Music Club | R101 | Mr. Raman |
| C2 | Sports Club | R202 | Ms. Sita |
| C3 | Drama Club | R303 | Mr. Kiran |
| C4 | Coding Club | Lab1 | Mr. Anil |

### JOIN query (StudentName, ClubName, JoinDate)
| StudentName | ClubName | JoinDate |
|-------------|----------|----------|
| Aman | Coding Club | 2024-01-30 |
| Asha | Music Club | 2024-01-10 |
| Asha | Sports Club | 2024-01-15 |
| Bikash | Sports Club | 2024-01-12 |
| Bikash | Drama Club | 2024-01-25 |
| Nisha | Music Club | 2024-01-20 |
| Nisha | Coding Club | 2024-01-28 |
| Pooja | Sports Club | 2024-01-27 |
| Rohan | Drama Club | 2024-01-18 |
| Suman | Music Club | 2024-01-22 |

---

## Normalisation Summary

| Stage | What Was Done |
|-------|---------------|
| 1NF | Introduced MembershipID as a surrogate primary key to ensure each row is uniquely identifiable |
| 2NF | Separated student data and club data into their own tables, removing partial dependencies |
| 3NF | Replaced ClubName as a foreign key with a surrogate ClubID, removing transitive dependencies |

---

## ER Diagram

The ER diagram below uses Chen notation and shows the three entities (Student, Membership, Club) and their relationships.

![ER Diagram](image/ER%20Diagram%20-%20College%20Club%20Membership%20Database%20(3NF).png)

- One **Student** can enrol in many **Memberships**
- One **Club** can have many **Memberships**
- **Membership** acts as a bridge table resolving the many-to-many relationship
