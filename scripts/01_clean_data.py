import pandas as pd
import numpy as np
from pathlib import Path
# ---------------------------------------------------------
# 1. Define project paths
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA_FOLDER = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_FOLDER = PROJECT_ROOT / "data" / "processed"

PROCESSED_DATA_FOLDER.mkdir(parents=True, exist_ok=True)
# ---------------------------------------------------------
# 2. Find the raw Excel dataset
# ---------------------------------------------------------

possible_file_names = [
    "Dataset_for_Data_Analytics.xlsx",
    "Dataset for Data Analytics.xlsx"
]

raw_data_path = None

for file_name in possible_file_names:
    file_path = RAW_DATA_FOLDER / file_name
    if file_path.exists():
        raw_data_path = file_path
        break

if raw_data_path is None:
    raise FileNotFoundError(
        "Raw dataset not found. Please place the Excel file inside data/raw/"
    )


print("Loading raw dataset...")
print(f"File used: {raw_data_path}")
# ---------------------------------------------------------
# 3. Load dataset
# ---------------------------------------------------------

df = pd.read_excel(raw_data_path)

print(f"Raw dataset shape: {df.shape}")


# ---------------------------------------------------------
# 4. Clean column names
# ---------------------------------------------------------

df.columns = df.columns.str.strip()

print("Column names cleaned.")


# ---------------------------------------------------------
# 5. Remove duplicate rows
# ---------------------------------------------------------

duplicate_rows_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicate_rows_after = df.duplicated().sum()

print(f"Duplicate rows before cleaning: {duplicate_rows_before}")
print(f"Duplicate rows after cleaning: {duplicate_rows_after}")


# ---------------------------------------------------------
# 6. Remove duplicate OrderID records
# ---------------------------------------------------------

duplicate_order_ids_before = df["OrderID"].duplicated().sum()

df = df.drop_duplicates(subset="OrderID", keep="first")

duplicate_order_ids_after = df["OrderID"].duplicated().sum()

print(f"Duplicate OrderID before cleaning: {duplicate_order_ids_before}")
print(f"Duplicate OrderID after cleaning: {duplicate_order_ids_after}")


# ---------------------------------------------------------
# 7. Clean Date column
# ---------------------------------------------------------

if pd.api.types.is_numeric_dtype(df["Date"]):
    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce",
        unit="D",
        origin="1899-12-30"
    )
else:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

invalid_dates_after = df["Date"].isnull().sum()

# Save date in standard format
df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

print(f"Invalid dates after cleaning: {invalid_dates_after}")


# ---------------------------------------------------------
# 8. Handle missing CouponCode values
# ---------------------------------------------------------

missing_coupon_before = df["CouponCode"].isnull().sum()

df["CouponCode"] = df["CouponCode"].fillna("NO_COUPON")

missing_coupon_after = df["CouponCode"].isnull().sum()

print(f"Missing CouponCode before cleaning: {missing_coupon_before}")
print(f"Missing CouponCode after cleaning: {missing_coupon_after}")


# ---------------------------------------------------------
# 9. Standardize text columns
# ---------------------------------------------------------

text_columns = [
    "Product",
    "ShippingAddress",
    "PaymentMethod",
    "OrderStatus",
    "TrackingNumber",
    "CouponCode",
    "ReferralSource"
]

for col in text_columns:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
        )

# Standardize important category columns
df["PaymentMethod"] = df["PaymentMethod"].str.title()
df["OrderStatus"] = df["OrderStatus"].str.title()
df["ReferralSource"] = df["ReferralSource"].str.title()
df["CouponCode"] = df["CouponCode"].str.upper()

print("Text columns standardized.")


# ---------------------------------------------------------
# 10. Clean numeric columns
# ---------------------------------------------------------

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Quantity"] = df["Quantity"].astype("Int64")
df["ItemsInCart"] = df["ItemsInCart"].astype("Int64")

df["UnitPrice"] = df["UnitPrice"].round(2)
df["TotalPrice"] = df["TotalPrice"].round(2)

print("Numeric columns cleaned.")


# ---------------------------------------------------------
# 11. Validate and correct TotalPrice
# ---------------------------------------------------------

expected_total_price = (df["Quantity"] * df["UnitPrice"]).round(2)

incorrect_total_price_before = (
    df["TotalPrice"].round(2) != expected_total_price
).sum()

df["TotalPrice"] = expected_total_price

incorrect_total_price_after = (
    df["TotalPrice"].round(2) != expected_total_price
).sum()

print(f"Incorrect TotalPrice rows before cleaning: {incorrect_total_price_before}")
print(f"Incorrect TotalPrice rows after cleaning: {incorrect_total_price_after}")


# ---------------------------------------------------------
# 12. Final quality checks
# ---------------------------------------------------------

final_missing_values = df.isnull().sum().sum()
final_duplicate_rows = df.duplicated().sum()
final_duplicate_order_ids = df["OrderID"].duplicated().sum()
final_invalid_dates = pd.to_datetime(df["Date"], errors="coerce").isnull().sum()

print("\nFinal Quality Check")
print("-------------------")
print(f"Final missing values: {final_missing_values}")
print(f"Final duplicate rows: {final_duplicate_rows}")
print(f"Final duplicate OrderID: {final_duplicate_order_ids}")
print(f"Final invalid dates: {final_invalid_dates}")
print(f"Final incorrect TotalPrice rows: {incorrect_total_price_after}")


# ---------------------------------------------------------
# 13. Save cleaned dataset
# ---------------------------------------------------------

cleaned_csv_path = PROCESSED_DATA_FOLDER / "orders_cleaned.csv"
cleaned_excel_path = PROCESSED_DATA_FOLDER / "orders_cleaned.xlsx"

df.to_csv(cleaned_csv_path, index=False)
df.to_excel(cleaned_excel_path, index=False)

print("\nCleaned files saved successfully:")
print(f"CSV file: {cleaned_csv_path}")
print(f"Excel file: {cleaned_excel_path}")