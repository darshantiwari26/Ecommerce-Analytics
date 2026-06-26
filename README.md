# 🛒 E-Commerce Sales Analytics Dashboard

An end-to-end **Data Analytics Project** built using **Python, MySQL, and Power BI**. This project demonstrates the complete data analytics workflow—from synthetic data generation and database management to interactive business intelligence dashboards.

---

## 📌 Project Overview

This project simulates an e-commerce business by generating realistic sales data, storing it in a MySQL database, and visualizing key business insights using Power BI.

The dashboard enables users to analyze:

- 📈 Revenue and Profit
- 🛍️ Category-wise Sales
- 📦 Product Performance
- 👥 Customer Insights
- 💳 Payment Method Distribution
- 📅 Revenue Trends Over Time

---

## 🚀 Technologies Used

- **Python**
  - Pandas
  - Faker
  - MySQL Connector
- **MySQL**
- **Power BI**
- **Git & GitHub**

---

## 📂 Project Structure

```text
Ecommerce-Sales-Analytics/
│
├── dashboard/
│   └── Ecommerce_Sales_Analytics_Dashboard.pbix
│
├── database/
│   └── ecommerce.sql
│
├── dataset/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── python/
│   ├── generate_data.py
│   └── import_mysql.py
│
├── screenshots/
│   ├── dashboard.png
│   └── model.png
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset was generated using Python and Faker.

| Table | Records |
|--------|---------|
| Customers | 1,000 |
| Products | 100 |
| Orders | 5,000 |
| Categories | 5 |

---

## 📈 Dashboard Features

✔ Total Revenue

✔ Total Profit

✔ Total Orders

✔ Total Customers

✔ Revenue by Category

✔ Monthly Revenue Trend

✔ Top Products by Revenue

✔ Payment Method Distribution

✔ Top Customers Analysis

✔ Interactive Filters (Category & Payment Method)

---

## 🗄 Database Schema

The project uses a relational database with the following tables:

- Categories
- Products
- Customers
- Orders

Relationships:

```
Categories (1) ───────< Products

Products (1) ─────────< Orders

Customers (1) ────────< Orders
```

---

## 📸 Dashboard Preview

### Dashboard

> Add your screenshot here

```
screenshots/dashboard.png
```

### Data Model

> Add your model screenshot here

```
screenshots/model.png
```

---

## ⚙ Installation

### 1. Clone Repository

```bash
git clone https://github.com/darshantiwari26/e-commerce-sales-analytics.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate Dataset

```bash
python python/generate_data.py
```

### 4. Import Data into MySQL

```bash
python python/import_mysql.py
```

### 5. Open Power BI Dashboard

Open

```
dashboard/Ecommerce_Sales_Analytics_Dashboard.pbix
```

---

## 📌 Key Business Insights

- Analyze category-wise revenue contribution
- Identify top-performing products
- Monitor monthly sales trends
- Compare payment method usage
- Identify valuable customers
- Track business KPIs

---

## 🎯 Skills Demonstrated

- Data Generation
- Data Cleaning
- SQL Database Design
- Data Import Automation
- Power BI Dashboard Development
- DAX Measures
- Data Modeling
- Business Intelligence
- Data Visualization

---

## 📷 Screenshots

### Dashboard

(Add `dashboard.png` here)

### Model View

(Add `model.png` here)

---

## 👨‍💻 Author

**Darshan Tiwari**

- 🎓 B.Tech Information Technology
- 📊 Aspiring Data Analyst
- 💼 Skilled in Python, SQL, Power BI & Data Analytics

### Connect with Me

- GitHub: https://github.com/darshantiwari26
- LinkedIn: https://www.linkedin.com/in/darshan-tiwari-72816734a

---

## ⭐ If you found this project useful, consider giving it a star!
