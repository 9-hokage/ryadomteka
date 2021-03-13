select name,price  from (
    select sum(d.price) price, s.name name from drugs d 
        inner join drugs_storedrugs dd on d.id=dd.drug_id
        inner join stores s on s.id=dd.store_id
        inner join drugs_boughtdrugs db on d.id=db.drug_id
        inner join users u on u.id=db.user_id
    where u.date_joined>SYSDATE-7 and d.category_id=(select id from DRUGS_DRUGCATEGORY where name='Дерматологические средства » Ранозаживляющие препараты') and d.form_drug='Таблетки, покрытые оболочкой'
    group by s.name order by price desc
  ) where price is not null Fetch first 1 rows only;
