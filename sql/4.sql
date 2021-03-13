select stores.work_time_sun
from stores 
inner join drugs_storedrugs d on d.store_id=stores.ID
inner join drugs on drugs.id=d.drug_id
where drugs.name='Рабемак';
