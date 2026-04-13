import sqlite3


class DatabaseConnection:
    """Realiza una conexión real a una base de datos."""

    def __init__(self) -> None:
        # En producción, esto abriría una conexión real
        self.connection = sqlite3.connect("prod_database.db")
        print("[DB] Conexión establecida con prod_database.db")

    def find_by_email(self, email: str) -> dict | None:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        return {"email": row[0], "name": row[1]} if row else None

    def save(self, user: dict) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO users (email, name) VALUES (?, ?)", (user["email"], user["name"])
        )
        self.connection.commit()
        print(f"[DB] Usuario guardado: {user['email']}")
