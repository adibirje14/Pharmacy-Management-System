**💊 Pharmacy Management System**
**📌 Overview**

This is a Pharmacy Management System built with Python (Tkinter) and MySQL.
The application provides modules for:

- User Authentication (Login, Register, Forgot Password)
- Pharmacy Inventory Management (add, update, delete, search medicines)
- Billing System (generate, save, print, and search bills)
- It’s designed to help small/medium pharmacies manage medicines, track stock, and handle customer billing.

**🛠️ Tech Stack**

- Frontend/UI: Tkinter (Python GUI library), Pillow (image handling)
- Backend: Python
- Database: MySQL (with tables like register, pharma, pharmacy, bill)
- Other: Random, OS, Tempfile, Datetime

**🚀 Features**
1. 🔑 User Module
- Login with email & password
- Register new users
- Reset password via security questions

2. 💊 Pharmacy Module
- Add new medicines
- Update and delete medicine records
- Search medicines by reference, lot number, or name
- Manage inventory (stock levels, expiry, dosage, etc.)

3. 🧾 Billing Module

- Add medicines to cart
- Generate bills with subtotal, tax, and total amount
- Save bills locally as .txt files
- Print bills directly
- Search old bills by bill number

**⚙️ Setup Instructions**

1. Install Dependencies

pip install pillow mysql-connector-python


2. Setup Database

- Create a MySQL database named project.
- Create the following tables:
  a) register (for user login/registration)
  b) pharma (medicine references)
  c) pharmacy (medicine details & stock)
  d) bill (billing records)

Example (simplified):

CREATE DATABASE project;

CREATE TABLE register (
    fname VARCHAR(50),
    lname VARCHAR(50),
    contact VARCHAR(15),
    email VARCHAR(50) PRIMARY KEY,
    securityQ VARCHAR(50),
    securityA VARCHAR(50),
    password VARCHAR(50)
);

CREATE TABLE pharma (
    ref VARCHAR(50) PRIMARY KEY,
    medname VARCHAR(100)
);

CREATE TABLE pharmacy (
    reg VARCHAR(50),
    companyname VARCHAR(100),
    type VARCHAR(50),
    tabletname VARCHAR(100),
    lotno INT,
    issuedate DATE,
    expdate DATE,
    uses TEXT,
    sideeffect TEXT,
    dosage VARCHAR(50),
    price FLOAT,
    productqt INT
);

CREATE TABLE bill (
    date DATE,
    billno VARCHAR(50),
    cname VARCHAR(100),
    cemail VARCHAR(100),
    cphone VARCHAR(15),
    subtotal VARCHAR(20),
    tax VARCHAR(20),
    total VARCHAR(20)
);


3. Run the Application

python main.py


**Made by Aditya Birje**
