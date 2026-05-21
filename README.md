### **# Retail Orders Data Cleaning \& Sales Analysis Project**

# 

#### **## Project Overview**

# 

This project focuses on cleaning, preparing, storing, analyzing, and visualizing a retail orders dataset.



The main objective of the project is to transform a raw dataset into a clean, reliable, and analysis-ready dataset by handling missing values, duplicate records, incorrect date formats, inconsistent text values, and numeric validation issues.



After cleaning the dataset, the cleaned data was stored in a SQLite database, analyzed using SQL queries, and visualized using Power BI.



\---

# 

#### **## Project Goal**

# 

The goal of this project is to prove that the dataset is ready for business analysis by completing the following tasks:



\- Identify missing or null values

\- Remove duplicate records

\- Validate unique OrderID values

\- Correct and standardize date formats

\- Standardize text/category columns

\- Validate numeric columns

\- Check TotalPrice using Quantity × UnitPrice

\- Store cleaned data in a database

\- Perform SQL-based business analysis

\- Build a Power BI dashboard



\---

# 

#### **## Tools Used**

# 

\- Python

\- Pandas

\- JupyterLab

\- SQLite

\- SQL

\- Power BI

\- GitHub

\- GitHub Desktop



\---

# 

#### **## Dataset Description**

# 

The dataset contains retail order records with customer, product, payment, coupon, referral, and order status details.



Main columns include:



| Column | Description |

|---|---|

| OrderID | Unique order identifier |

| Date | Order date |

| CustomerID | Unique customer identifier |

| Product | Product ordered |

| Quantity | Number of units ordered |

| UnitPrice | Price per unit |

| ShippingAddress | Shipping location |

| PaymentMethod | Payment method used |

| OrderStatus | Current order status |

| TrackingNumber | Order tracking number |

| ItemsInCart | Number of items in cart |

| CouponCode | Coupon used for the order |

| ReferralSource | Customer referral source |

| TotalPrice | Final order total |



\---

# 

#### **## Project Workflow**

# 

```text

Raw Dataset

&#x20;    ↓

Data Audit

&#x20;    ↓

Data Cleaning

&#x20;    ↓

Quality Check Proof

&#x20;    ↓

SQLite Database

&#x20;    ↓

SQL Analysis

&#x20;    ↓

Power BI Dashboard

