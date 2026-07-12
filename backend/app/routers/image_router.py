from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.schemas.image import ImageResponse
from app.services.image_service import upload_image

router = APIRouter(
    prefix="/projects",
    tags=["Images"]
)


@router.post(
    "/{project_id}/images",
    response_model=ImageResponse
)
def upload_project_image(
    project_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return upload_image(
        db=db,
        project_id=project_id,
        file=file
    )