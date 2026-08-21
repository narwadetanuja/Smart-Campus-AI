import sqlite3


def create_database():

    conn = sqlite3.connect("complaints.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            complaint TEXT,
            category TEXT,
            priority TEXT,
            department TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_complaint(
    name,
    complaint,
    category,
    priority,
    department
):

    conn = sqlite3.connect("complaints.db")

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO complaints
        (name, complaint, category, priority, department)
        VALUES (?, ?, ?, ?, ?)
    """, (
        name,
        complaint,
        category,
        priority,
        department
    ))

    conn.commit()
    conn.close()


def get_complaints():

    conn = sqlite3.connect("complaints.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM complaints
    """)

    data = cursor.fetchall()

    conn.close()

    return data