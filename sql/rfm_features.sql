WITH revenue AS (
    SELECT 
        customer_id,
        SUM(quantity * price) AS total_revenue
    FROM transactions
    GROUP BY customer_id
),

frequency AS (
    SELECT
        customer_id,
        COUNT(DISTINCT invoice) AS total_orders
    FROM transactions
    GROUP BY customer_id
),

recency AS (
    SELECT customer_id,
	max(invoicedate) as last_transaction_date,(select max(invoicedate) from transactions) - max(invoicedate) as last_purchase
from transactions 
group by customer_id
        
)

SELECT 
    r.customer_id,
    r.total_revenue,
    f.total_orders,
    rec.last_purchase
FROM revenue r
JOIN frequency f ON r.customer_id = f.customer_id
JOIN recency rec ON r.customer_id = rec.customer_id;

CREATE TABLE customer_features AS
WITH revenue AS (
    SELECT 
        customer_id,
        SUM(quantity * price) AS monetary
    FROM transactions
    GROUP BY customer_id
),

frequency AS (
    SELECT
        customer_id,
        COUNT(DISTINCT invoice) AS frequency
    FROM transactions
    GROUP BY customer_id
),

recency AS (
    SELECT 
        customer_id,
        DATE_PART('day',
            (SELECT MAX(invoicedate) FROM transactions) - MAX(invoicedate)
        ) AS recency
    FROM transactions
    GROUP BY customer_id
),

lifetime_days AS(
	SELECT 
		customer_id,
		date_part('day',max(invoicedate)-min(invoicedate)) AS lifetime_days
		FROM transactions
		GROUP BY customer_id
)

SELECT 
    r.customer_id,
    rec.recency,
    f.frequency,
    r.monetary,
	(r.monetary/f.frequency) AS avg_order_value,
	l.lifetime_days
FROM revenue r
JOIN frequency f ON r.customer_id = f.customer_id
JOIN recency rec ON r.customer_id = rec.customer_id
JOIN lifetime_days l ON r.customer_id = l.customer_id;

SELECT count(*) from customer_features;