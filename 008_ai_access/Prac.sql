-- select count(*) as specific_number 
-- FROM martlist
-- 3. 이 데이터에서 여자가 구입한 수를 알고싶을 때
-- where genders = '여';
-- 4. 탈퇴한 회원이 구입한 개수
-- where mem_level = '탈퇴';
-- 5. 마트 총 매출
-- select sum(sale_pays) as pay_total from martlist;
-- select * from martlist limit 5;
-- select dates, sale_times, mem_numer, mem_level, mart_info
-- from martlist limit 10;
select dates, item_cate1, item_cate2, item_cate3, sale_pays
from martlist
where 0 < sale_pays and sale_pays < 2000
order by dates desc;