select users.first_name, users.last_name
from users 
inner join stores s on s.city_id=users.city_id
inner join  drugs_storedrugs d on d.store_id=s.ID
inner join drugs on drugs.id=d.drug_id
where users.city_id=(select id from ryadomteka_cities where name='Алматы') 
and s.name='Аптека';
