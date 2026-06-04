import sqlite3

DATABASE = "cheap_eats.db"

def run_sql_file(cursor, filename):
    with open(filename, "r", encoding="utf-8") as file:
        cursor.executescript(file.read())

def main():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    run_sql_file(cursor, "schema.sql")
    run_sql_file(cursor, "seed.sql")

    connection.commit()
    connection.close()

    print("Database initialized.")

if __name__ == "__main__":
    main()