select covid_statistics.cases
from covid_statistics
inner join ryadomteka_countries c on c.id=covid_statistics.country_id
where covid_statistics.case_date between TO_DATE('28-NOV-20','dd-mm-yy') 
and TO_DATE('28-OCT-20','dd-mm-yy') 
and c.name = 'Kazakhstan'
