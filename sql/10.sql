select * from ryadomteka_cities 
inner join stores s on s.city_id=ryadomteka_cities.id 
inner join drugs_storedrugs dd on dd.store_id=s.ID
inner join drugs d on d.id=dd.drug_id
where d.price<4000 and s.name='Аптека' and d.category_id=(select id from drugs_drugcategory where name='Заболевания органов ЖКТ и печени » Препараты от диареи') 
