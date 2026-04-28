import smtplib
import sqlite3
from datetime import datetime

import requests


class DatabaseService:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("udemy_students.db")

    def save_enrollment(self, student_email: str, course_id: str) -> int | None:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO enrollments (email, course_id, enrolled_at) VALUES (?, ?, ?)",
            (student_email, course_id, datetime.now().isoformat()),
        )
        self.connection.commit()
        return cursor.lastrowid

    def get_student(self, email: str) -> dict | None:
        cursor = self.connection.cursor()
        row = cursor.execute("SELECT * FROM students WHERE email = ?", (email,)).fetchone()
        if row:
            return {"email": row[0], "name": row[1], "plan": row[2]}
        return None


class EmailService:
    def __init__(self) -> None:
        self.smtp_client = smtplib.SMTP("smtp.udemy.com", 587)

    def send_welcome_email(self, student_email: str, course_name: str) -> bool:
        message = (
            f"Subject: Bienvenido al curso {course_name}\n\n"
            f"Hola, ya tienes acceso al curso {course_name}."
        )
        self.smtp_client.sendmail("no-reply@udemy.com", student_email, message)
        return True


class PaymentService:
    def __init__(self) -> None:
        self.api_url = "https://payments.udemy.com/api/v1"

    def charge(self, student_email: str, amount: float, currency: str = "USD") -> dict:
        response = requests.post(
            f"{self.api_url}/charge",
            json={"email": student_email, "amount": amount, "currency": currency},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def refund(self, transaction_id: str) -> dict:
        response = requests.post(
            f"{self.api_url}/refund",
            json={"transaction_id": transaction_id},
            timeout=10,
        )
        response.raise_for_status()
        return response.json()


class CertificateService:
    def __init__(self) -> None:
        self.generator_url = "https://certificates.udemy.com/generate"

    def generate(self, student_name: str, course_name: str) -> str:
        response = requests.post(
            self.generator_url,
            json={"student": student_name, "course": course_name},
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
        return data["certificate_url"]
