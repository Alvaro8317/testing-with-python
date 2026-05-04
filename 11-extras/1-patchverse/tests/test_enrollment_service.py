import uuid
from unittest import mock

import pytest
from src import enrollment_service

_SRC = "src.enrollment_service.dependencies"


@pytest.mark.enrollment
@mock.patch(f"{_SRC}.DatabaseService")  # A
@mock.patch(f"{_SRC}.PaymentService")  # B
@mock.patch(f"{_SRC}.EmailService")  # C
@mock.patch(f"{_SRC}.CertificateService")  # D
def test_should_enroll_student(
    mock_certificate_service: mock.MagicMock,  # D
    mock_email_service: mock.MagicMock,  # C
    mock_payment_service: mock.MagicMock,  # B
    mock_database_service: mock.MagicMock,  # A
) -> None:
    # Arrange
    mock_instance_database = mock_database_service.return_value
    mock_instance_database.get_student.return_value = {
        "email": "row[0]",
        "name": "row[1]",
        "plan": "row[2]",
    }
    mock_instance_database.save_enrollment.return_value = 1

    mock_instance_payment = mock_payment_service.return_value
    mock_instance_payment.charge.return_value = {
        "status": "approved",
        "transaction_id": str(uuid.uuid4()),
    }

    mock_instance_email = mock_email_service.return_value
    mock_instance_email.send_welcome_email.return_value = True

    mock_instance_certificate = mock_certificate_service.return_value
    mock_instance_certificate.generate.return_value = "https://www.udemy-fake-url.com"

    # Act
    service = enrollment_service.EnrollmentService()
    result = service.enroll_student(
        student_email="fake@email.com", course_id="3", course_name="Testing with python", price=10
    )

    # Assert
    assert result
    assert result["enrollment_id"] == 1
