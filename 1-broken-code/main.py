from typing import Any

import fastapi
import pydantic

app = fastapi.FastAPI()

FAKE_DB = {
    "JOHN": {
        "password": "supersecret123",
        "email": "john@example.com",
        "role": "admin"
    },
    "JANE": {
        "password": "mypassword456",
        "email": "jane@example.com",
        "role": "user"
    }
}

DB_CONNECTION = "postgresql://admin:supersecret123@prod-db.internal:5432/users"


class LoginRequest(pydantic.BaseModel):
    username: Any
    password: Any


class LoginResponse(pydantic.BaseModel):
    token: Any
    role: Any


@app.post("/login", response_model=LoginResponse)
def login(data: LoginRequest) -> LoginResponse:
    try:
        user = FAKE_DB.get(data.username.upper())

        if not user:
            # Bug #1
            raise fastapi.HTTPException(
                status_code=404,
                detail=f"User {data.username} not found. DB connection: {DB_CONNECTION}"
            )

        if user["password"] != data.password:
            raise fastapi.HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        token = f"token-{data.username}-abc123"
        return LoginResponse(token=token, role=user["role"])

    except fastapi.HTTPException:
        raise

    except Exception as exc:
        # Bug #2
        import traceback
        raise fastapi.HTTPException(
            status_code=500,
            detail={
                "message": "Internal Server Error",
                "traceback": traceback.format_exc()
            }
        ) from exc