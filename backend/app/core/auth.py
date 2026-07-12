from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.core.jwt import verify_token
from app.models.user import User

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    # Get JWT token from Authorization header
    token = credentials.credentials

    print("\n==============================")
    print("Received Token:")
    print(token)

    # Decode JWT token
    payload = verify_token(token)

    print("\nDecoded Payload:")
    print(payload)
    print("==============================\n")

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    # Extract email from token
    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Token missing email"
        )

    # Find user in database
    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user