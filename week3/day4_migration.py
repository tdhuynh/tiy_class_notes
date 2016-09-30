import psycopg2

connection = psycopg2.connect("dbname=my_first_user user=my_first_user")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS person_data;")

create_table_command = """
CREATE TABLE person_data (
    id serial PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    password VARCHAR(20),
    birthyear NUMERIC(4),
    bestie VARCHAR(20)
);
"""
cursor.execute(create_table_command)
cursor.execute("INSERT INTO person_data VALUES (1, 'tommy', 'safety', '1993', 'big m')")
cursor.execute("INSERT INTO person_data VALUES (2, 'michael', 'safety', '1990', 'big t')")

connection.commit()


cursor.close()
connection.close()
