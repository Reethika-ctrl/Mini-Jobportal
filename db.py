import mysql.connector

def get_connection():
    """
    This function creates and returns a new connection
    to the MySQL database 'job_portal'.

    Every time your code wants to talk to the database,
    it will call get_connection().
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="reethika",     # Your MySQL password
        database="job_portal"    # Your database name
    )
    return connection


# OPTIONAL: Run this file alone to test your DB connection
if __name__ == "__main__":
    try:
        conn = get_connection()   # Try connecting
        cur = conn.cursor()
        cur.execute("SHOW TABLES;")   # Show all tables
        print("Connection OK. Tables present:")
        for (name,) in cur.fetchall():
            print("-", name)
    except Exception as e:
        print("Connection error:", e)
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass
