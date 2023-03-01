import psycopg2

host = '127.0.0.1'
user = 'postgres'
password = 'postgres'
db_name = 'postgres'
table_name = 'file_to_trigger_word_mapping'

conn = psycopg2.connect(database=db_name, user=user, password=password)
with conn.cursor() as cursor:
    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_name}(
            file_id varchar(100) NOT NULL PRIMARY KEY,
            trigger_word varchar(200) NOT NULL,
            description text
            );"""
    )
    conn.commit()