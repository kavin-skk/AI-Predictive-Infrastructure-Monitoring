import psycopg2


def get_connection():
    """
    Creates and returns a connection to the PostgreSQL database.
    """
    return psycopg2.connect(
        host="postgres",          # Docker Compose service name
        database="monitoringdb",  # Database name
        user="admin",             # Username
        password="admin123",      # Password
        port="5432"
    )


def test_connection():
    """
    Tests whether the database connection is successful.
    """
    try:
        conn = get_connection()
        conn.close()
        return True
    except Exception as e:
        return str(e)


def get_products():
    """
    Fetches all products from the products table.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, status
        FROM products
        ORDER BY id;
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    products = []

    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "status": row[2]
        })

    return products