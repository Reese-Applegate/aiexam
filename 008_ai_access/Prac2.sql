-- select *
-- from martlist
-- where sale_pays = (select max(sale_pays) from martlist);
select *, (select min(sale_pays) from martlist) as minpay
from martlist
order by sale_pays desc
limit 10;