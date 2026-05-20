# Data Cleaning Log

## Project

Retail Orders Data Cleaning Project

## Objective

The objective of this project is to clean and prepare a raw retail orders dataset for analysis by handling missing values, duplicate records, incorrect date formats, inconsistent text values, and numeric validation issues.

## Raw Dataset Summary

| Check | Result |
|---|---:|
| Total Rows | 1200 |
| Total Columns | 14 |
| Duplicate Rows | 0 |
| Duplicate OrderID Values | 0 |
| Missing Values | 309 |
| Incorrect TotalPrice Rows | 0 |

## Main Data Quality Issue Found

The main issue found in the raw dataset was missing values in the `CouponCode` column.

This was not treated as a serious error because a missing coupon code usually means the customer did not use a coupon during the order.

## Cleaning Actions Performed

| Issue | Cleaning Action | Reason |
|---|---|---|
| Missing CouponCode values | Replaced with `NO_COUPON` | Missing coupon means no coupon was used |
| Duplicate rows | Checked and removed if found | Prevent repeated records |
| Duplicate OrderID values | Checked and removed if found | Each order must have one unique ID |
| Date values | Converted to `YYYY-MM-DD` format | Standard date format for analysis |
| Text columns | Removed extra spaces and standardized case | Keep categories consistent |
| Numeric columns | Converted to numeric format and rounded prices | Ensure calculations are correct |
| TotalPrice | Validated using `Quantity × UnitPrice` | Ensure order totals are accurate |

## Final Cleaned Dataset Summary

| Quality Check | Result |
|---|---:|
| Total Rows | 1200 |
| Total Columns | 14 |
| Total Missing Values | 0 |
| Duplicate Rows | 0 |
| Duplicate OrderID Values | 0 |
| Invalid Dates | 0 |
| Incorrect Date Formats | 0 |
| Incorrect TotalPrice Rows | 0 |

## Final Status

The cleaned dataset passed all quality checks and is ready for database loading, SQL analysis, and Power BI visualization.