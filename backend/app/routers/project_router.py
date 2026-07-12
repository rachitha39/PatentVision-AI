from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.core.auth import get_current_user

from app.models.user import User
from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectResponse
)

from app.services.project_service import (
    create_project,
    get_projects,
    get_project,
    update_project,
    delete_project
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


# ==========================
# Create Project
# ==========================
@router.post(
    "",
    response_model=ProjectResponse
)
def create_new_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return create_project(
        db=db,
        project=project,
        owner_id=current_user.id
    )


# ==========================
# Get All Projects
# ==========================
@router.get(
    "",
    response_model=list[ProjectResponse]
)
def list_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_projects(
        db=db,
        owner_id=current_user.id
    )


# ==========================
# Get One Project
# ==========================
@router.get(
    "/{project_id}",
    response_model=ProjectResponse
)
def get_single_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    project = get_project(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


# ==========================
# Update Project
# ==========================
@router.put(
    "/{project_id}",
    response_model=ProjectResponse
)
def update_single_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db_project = get_project(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )

    if db_project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return update_project(
        db=db,
        db_project=db_project,
        project=project
    )


# ==========================
# Delete Project
# ==========================
@router.delete("/{project_id}")
def remove_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db_project = get_project(
        db=db,
        project_id=project_id,
        owner_id=current_user.id
    )

    if db_project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    delete_project(
        db=db,
        db_project=db_project
    )

    return {
        "message": "Project deleted successfully"
    }