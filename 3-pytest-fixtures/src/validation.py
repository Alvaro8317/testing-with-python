def validate_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1] and len(email) > 0
