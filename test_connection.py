from src.database.connection import get_connection

try:
    conn = get_connection()

    cur = conn.cursor()

    cur.execute("SELECT version();")

    version = cur.fetchone()

    print("=" * 60)
    print("✅ Connected Successfully!")
    print(version[0])
    print("=" * 60)

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Connection Failed")
    print(e)