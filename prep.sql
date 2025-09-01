-----
SELECT TOP(5) names as top_products from products
WHERE product_date > CURRENT_DATE - INTERVAL '30 days'
SORT BY revenue DESC;

-----
SELECT 
    p.product_id,
    p.product_name,
    SUM(o.quantity * o.unit_price) AS total_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.order_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY p.product_id, p.product_name
ORDER BY total_revenue DESC
LIMIT 5;

--- without window function
select Department, AVG(Salary) from Employees
group by Department;

-- SELECT column_name1, 
--        window_function(column_name2) 
--        OVER ([PARTITION BY column_name3] [ORDER BY column_name4]) AS new_column
-- FROM table_name;

---- window function
select Department, Salary,
AVG(Salary) OVER (partition by Department) as Avg_Salary
from Employees;

--- without window function
select Name, Department, Salary from Employees
order by Department desc, Salary desc;

--- window function
select Name, Department, Salary
RANK() over (partition by Department order by Salary desc) as Top_Salary
from Employees;

select id, region, sales,
SUM(sales) over (partition by region order by id asc rows between unbound preceding and current row) as cumulative_sales
from sales_table;

select id, region, sales from (
    select id, region, sales
    RANK() over (partition by region order by sales desc ) as Region_Rank
    from sales_table ) ranked
where Region_Rank <= 2;