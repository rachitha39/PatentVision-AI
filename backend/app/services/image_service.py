import os
import shutil
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.image import Image


UPLOAD_FOLDER = "uploads"


def upload_image(
    db: Session,
    project_id: int,
    file: UploadFile
):
    # Create uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Generate a unique filename
    unique_filename = f"{uuid4().hex}_{file.filename}"

    file_path = os.path.join(
        UPLOAD_FOLDER,
        unique_filename
    )

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save image information in the database
    image = Image(
        filename=file.filename,
        filepath=file_path,
        project_id=project_id
    )

    db.add(image)
    db.commit()
    db.refresh(image)

    return image