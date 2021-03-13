select s.name
from drugs 
inner join drugs_storedrugs d on d.drug_id=drugs.ID
inner join stores s ON s.id=d.store_id
inner join drugs_boughtdrugs db on db.drug_id=drugs.id
where drugs.price>1000 and drugs.recipe=0 and 
    drugs.category_id=(select id from drugs_drugcategory where name='Дерматологические средства » Ранозаживляющие препараты' )
