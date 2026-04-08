create database if not exists SuperStoreOrders;
use SuperStoreOrders;
select * from store limit 10;
desc store;

-- total revenue, total profit, total orders
select sum(sales) as total_revenue,
sum(profit) as total_profit,
count(distinct(order_id)) as total_orders
from store;

-- How do you analyze sales and profit performance across different regions ?
select region, sum(sales) as revenue,
sum(profit) as profit from store group by region order by profit,revenue;

-- How can you identify the top 10 revenue-generating products
select product_id, sum(sales) as revenue from store group by product_id order by revenue desc limit 10;

-- How do you evaluate performance across different product categories in terms of sales and profit
select category,  sum(sales) as revenue,
sum(profit) as profit from store group by category order by revenue desc;

-- How do you identify products that are generating losses
SELECT product_name, round(SUM(Profit),2) AS total_loss
FROM store GROUP BY product_name HAVING Total_Loss < 0 ORDER BY Total_Loss ASC;


-- How can you analyze monthly sales trends over time
select year,month_name, sum(sales) as monthly_sales from store group by year, month_name order by year, month_name;

-- How do you identify high-value customers based on their total spending 
SELECT customer_name,
    SUM(sales) AS total_spending FROM store
GROUP BY customer_name ORDER BY total_spending DESC LIMIT 10;