select *
from covid_statistics
where country_id=(select id from ryadomteka_countries where name='Guyana')
