import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="S1o2b3h4a5@"   # Replace with your password
    )

    cursor = conn.cursor()

    cursor.execute("SHOW DATABASES")

    for db in cursor:
        print(db)

    conn.close()

except Exception as e:
    print(e)