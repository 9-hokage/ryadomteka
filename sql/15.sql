SELECT * FROM stores S 
INNER JOIN drugs_storedrugs  D ON D.store_id=S.ID
INNER JOIN drugs  ON drugs.ID=D.drug_id
WHERE  drugs.country_id=(SELECT ID FROM ryadomteka_countries WHERE NAME='Switzerland') AND S.city_id=(SELECT ID FROM ryadomteka_cities WHERE NAME='Павлодар') AND substr(S.work_time_weekdays, 22, 5)='20:00' ; 
