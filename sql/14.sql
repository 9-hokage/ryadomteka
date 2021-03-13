select buy_date,price  from (
    select sum(d.price) price,db.buy_date buy_date from drugs d 
        inner join drugs_storedrugs dd on d.id=dd.drug_id
        inner join stores s on s.id=dd.store_id
        inner join drugs_boughtdrugs db on d.id=db.drug_id 
    where s.name='PHARMA PLUS'
    group by db.buy_date order by price desc
  )  Fetch first 1 rows only;
