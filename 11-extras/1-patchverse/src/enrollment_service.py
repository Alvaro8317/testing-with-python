from src import dependencies


class EnrollmentService:
    """
    Orquesta la inscripción completa de un estudiante en un curso de Udemy.
    Crea sus propias dependencias internamente (alto acoplamiento).
    """

    def enroll_student(
        self,
        student_email: str,
        course_id: str,
        course_name: str,
        price: float,
    ) -> dict:
        db = dependencies.DatabaseService()
        payment = dependencies.PaymentService()
        email = dependencies.EmailService()
        certificate = dependencies.CertificateService()

        student = db.get_student(student_email)
        if student is None:
            raise ValueError(f"Estudiante {student_email} no encontrado")

        charge_result = payment.charge(student_email, price)
        if charge_result.get("status") != "approved":
            raise RuntimeError("El pago fue rechazado")

        enrollment_id = db.save_enrollment(student_email, course_id)
        email.send_welcome_email(student_email, course_name)
        cert_url = certificate.generate(student["name"], course_name)

        return {
            "enrollment_id": enrollment_id,
            "transaction_id": charge_result["transaction_id"],
            "certificate_url": cert_url,
            "status": "enrolled",
        }
