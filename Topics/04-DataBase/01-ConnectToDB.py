# --- Creating Db & Connect to it using Python with SQLite ---
# 1- import sqlite module 
# 2- craete ur db using this command: db = sqlite.connect("db_name")
# 3- execute ur queries using this command: db.execute("Sql query")
# 4- close the connection 
# ------------------------------------------------------------

# 1- import sqlite module 
import sqlite3 as sl

# 2- craete ur db
db = sl.connect("app.db")

# 3- execute ur queries
db.execute("""
        create table if not exists`user_skills` (
        name text,
        progress integer,
        user_id integer
    )""")

# 4- close the connection 
db.close()