-- Retail Orders Data Cleaning Project
-- SQLite database schema

DROP TABLE IF EXISTS cleaned_orders;

CREATE TABLE cleaned_orders (
    OrderID TEXT PRIMARY KEY,
    Date TEXT,
    CustomerID TEXT,
    Product TEXT,
    Quantity INTEGER,
    UnitPrice REAL,
    ShippingAddress TEXT,
    PaymentMethod TEXT,
    OrderStatus TEXT,
    TrackingNumber TEXT,
    ItemsInCart INTEGER,
    CouponCode TEXT,
    ReferralSource TEXT,
    TotalPrice REAL
);