db_name = "mariaI.db"
table_name = 'file_to_trigger_word_mapping'

def init_db():
    from sqlite3 import connect
    conn = connect(db_name)
    cursor = conn.cursor()
    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_name}(
        file_id varchar(100) NOT NULL PRIMARY KEY,
        trigger_word varchar(200) NOT NULL
        );"""
    )
    conn.commit()
    conn.close()

