import psycopg2

host = '127.0.0.1'
user = 'postgres'
password = 'olejasin'
db_name = 'content_dist_db'
table_name = 'file_to_trigger_word_mapping'

conn = psycopg2.connect(database=db_name, user=user, password=password)
with conn.cursor() as cursor:
    cursor.execute(
        f"""DROP TABLE {table_name};"""
    )
    conn.commit()