-- Retail Orders Data Cleaning Project
-- SQL Analysis Queries

-- 1. Total orders, revenue, and average order value
SELECT 
    COUNT(*) AS total_orders,
    ROUND(SUM(TotalPrice), 2) AS total_revenue,
    ROUND(AVG(TotalPrice), 2) AS average_order_value
FROM cleaned_orders;


-- 2. Orders by status
SELECT 
    OrderStatus,
    COUNT(*) AS order_count,
    ROUND(SUM(TotalPrice), 2) AS total_revenue
FROM cleaned_orders
GROUP BY OrderStatus
ORDER BY order_count DESC;


-- 3. Revenue by product
SELECT 
    Product,
    COUNT(*) AS total_orders,
    SUM(Quantity) AS total_quantity_sold,
    ROUND(SUM(TotalPrice), 2) AS total_revenue
FROM cleaned_orders
GROUP BY Product
ORDER BY total_revenue DESC;


-- 4. Payment method analysis
SELECT 
    PaymentMethod,
    COUNT(*) AS total_orders,
    ROUND(SUM(TotalPrice), 2) AS total_revenue,
    ROUND(AVG(TotalPrice), 2) AS average_order_value
FROM cleaned_orders
GROUP BY PaymentMethod
ORDER BY total_orders DESC;


-- 5. Referral source analysis
SELECT 
    ReferralSource,
    COUNT(*) AS total_orders,
    ROUND(SUM(TotalPrice), 2) AS total_revenue
FROM cleaned_orders
GROUP BY ReferralSource
ORDER BY total_orders DESC;


-- 6. Coupon usage analysis
SELECT 
    CASE 
        WHEN CouponCode = 'NO_COUPON' THEN 'No Coupon'
        ELSE 'Used Coupon'
    END AS coupon_status,
    COUNT(*) AS total_orders,
    ROUND(SUM(TotalPrice), 2) AS total_revenue
FROM cleaned_orders
GROUP BY coupon_status
ORDER BY total_orders DESC;


-- 7. Monthly revenue trend
SELECT 
    strftime('%Y-%m', Date) AS month,
    COUNT(*) AS total_orders,
    ROUND(SUM(TotalPrice), 2) AS total_revenue
FROM cleaned_orders
GROUP BY month
ORDER BY month;


-- 8. Top 10 customers by revenue
SELECT 
    CustomerID,
    COUNT(*) AS total_orders,
    ROUND(SUM(TotalPrice), 2) AS total_spent
FROM cleaned_orders
GROUP BY CustomerID
ORDER BY total_spent DESC
LIMIT 10;