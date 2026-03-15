import sys
sys.path.insert(0, "../connections") 

import connection_snowflake
import generate_random_user

#Here, name, surname & email address will be generated in order to 
#Complete the random data population for doctors & patients
session = connection_snowflake.new_session

session.sql('CREATE TABLE IF NOT EXISTS dummy_user_data (first_name VARCHAR(30), last_name VARCHAR(30), email VARCHAR(50))').collect()

persons_data = generate_random_user.generate_random_name_and_surname(5000)
df = session.create_dataframe(persons_data, schema = ["FIRST_NAME", "LAST_NAME", "EMAIL"])
df.write.insert_into("dummy_user_data")
session.table("dummy_user_data").collect()

session.close()