SELECT USERS.FIRST_NAME, USERS.LAST_NAME
FROM USERS
INNER JOIN STORES S  ON S.CITY_ID=USERS.CITY_ID
INNER JOIN DRUGS_STOREDRUGS D ON D.STORE_ID=S.ID
INNER JOIN DRUGS ON DRUGS.ID=D.DRUG_ID
WHERE USERS.CITY_ID=(SELECT ID FROM RYADOMTEKA_CITIES WHERE NAME='Алматы') AND DRUGS.NAME='Траумель С';
