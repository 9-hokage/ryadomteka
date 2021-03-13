select count(drugs.name) 
from drugs 
inner join drugs_storedrugs d on d.drug_id=drugs.ID
inner join stores s ON s.id=d.store_id
where drugs.country_id=(select id from ryadomteka_countries where name='Kazakhstan') and
s.city_id=(select id from ryadomteka_cities where name='Алматы') and 
s.name='Аптека';
