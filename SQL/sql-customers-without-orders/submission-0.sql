-- Write your query below
select name from customers u
left join orders o on u.id = o.customer_id
where o.id is null;