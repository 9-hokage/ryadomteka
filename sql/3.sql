select drugs.price 
from drugs 
inner join drugs_storedrugs d on d.drug_id=drugs.ID
inner join stores s ON s.id=d.store_id
where s.city_id=(select id from ryadomteka_cities where name='Алматы');
