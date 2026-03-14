from connections import connection_snowflake
from dummy_user import generate_random_name_and_surname

#Here, name, surname & email address will be generated in order to 
#Complete the random data population for doctors & patients
cursor = connection_snowflake.conn.cursor()

record_count_query = f"""
    SELECT COUNT(*) FROM DUMMY_DATASETS.SCHEMA_FOR_DUMMY_DATA.DUMMY_DOCTOR_INFORMATION
"""

cursor.execute(record_count_query)

try:
    for result in cursor:
        number_of_records = result[0]
except:
    number_of_records = 0
    print('Error with database connection.')

doctor_identification_information = []

for item in range(number_of_records):
    get_doctor_identification_information = generate_random_name_and_surname.generate_random_name_and_surname()
    
    first_name = get_doctor_identification_information[0]
    last_name = get_doctor_identification_information[1]
    email = get_doctor_identification_information[2]

    doctor_identification_information.append((first_name, last_name, email))


insert_name_surname_and_email_address = f"""
    INSERT INTO DUMMY_DATASETS.SCHEMA_FOR_DUMMY_DATA.DUMMY_DOCTOR_INFORMATION (first_name, last_name, email)
    VALUES (%s,%s,%s)
"""

cursor.executemany(insert_name_surname_and_email_address, doctor_identification_information)

connection_snowflake.conn.commit()

cursor.close()