import sqlite3


class HeroRepository:
    def __init__(self, db_path: str = "heroes.db"):
        self.db_path = db_path
        self._init_db()

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS heroes (
                    id        INTEGER PRIMARY KEY AUTOINCREMENT,
                    name      TEXT    NOT NULL UNIQUE,
                    strength  INTEGER NOT NULL,
                    city      TEXT    NOT NULL
                )
            """)

    def save(self, name: str, strength: int, city: str) -> dict:
        with self._connect() as conn:
            cursor = conn.execute(
                "INSERT INTO heroes (name, strength, city) VALUES (?, ?, ?)",
                (name, strength, city),
            )
            return {"id": cursor.lastrowid, "name": name, "strength": strength, "city": city}

    def get_by_id(self, hero_id: int) -> dict | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT id, name, strength, city FROM heroes WHERE id = ?",
                (hero_id,),
            ).fetchone()
        if row is None:
            return None
        return {"id": row[0], "name": row[1], "strength": row[2], "city": row[3]}

    def get_by_city(self, city: str) -> list[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT id, name, strength, city FROM heroes WHERE city = ?",
                (city,),
            ).fetchall()
        return [{"id": r[0], "name": r[1], "strength": r[2], "city": r[3]} for r in rows]

    def delete(self, hero_id: int) -> bool:
        with self._connect() as conn:
            cursor = conn.execute(
                "DELETE FROM heroes WHERE id = ?",
                (hero_id,),
            )
        return cursor.rowcount > 0

    def update_strength(self, hero_id: int, strength: int) -> dict | None:
        with self._connect() as conn:
            conn.execute(
                "UPDATE heroes SET strength = ? WHERE id = ?",
                (strength, hero_id),
            )
        return self.get_by_id(hero_id)
