from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from db.database import get_session 
from api.deps import get_current_user, check_teacher_role, moderate_comment

from exceptions.course import CourseNotFoundError
from exceptions.auth import AuthenticationError
from schemas.course import CourseShortSchema, CourseDetailSchema, CourseCreateSchema
from schemas.comment import CommentResponseSchema, CommentCreateSchema

from services import course_service
from services import comment_service

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/", response_model=list[CourseShortSchema])
def get_all_courses(db: Session = Depends(get_session)  ):
    try:
        return course_service.get_all_courses(db = db)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error when getting all courses"
    )


@router.get("/{id}", response_model=CourseDetailSchema)
def get_course(
    id: int, 
    db: Session = Depends(get_session),
    current_user = Depends(get_current_user)
):
    try:
        return course_service.get_course_by_id(course_id = id, user_id = current_user.id, db = db)
    except CourseNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error when getting course"
        )


@router.post("/", response_model=CourseDetailSchema, status_code=status.HTTP_201_CREATED)
def create_course(
    course_data: CourseCreateSchema,
    teacher = Depends(check_teacher_role),
    db: Session = Depends(get_session)
):
    
    try:
        return course_service.create_course(course_data = course_data, author_id = teacher.id, db = db)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error when creating course"
        )


@router.get("/{id}/comments", response_model=list[CommentResponseSchema])
def get_course_comments(
    id: int,
    db: Session = Depends(get_session),
):
    
    try:
        return comment_service.get_comments_for_course(course_id = id, db = db)
    except CourseNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error when getting course comments"
        )


@router.post("/{id}/comments", response_model=CommentResponseSchema, status_code=status.HTTP_201_CREATED)
def add_comment_to_course(
    id: int,
    comment_data: CommentCreateSchema = Depends(moderate_comment),
    current_user = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    
    try:
        return comment_service.add_comment(course_id = id, user_id = current_user.id, comment_data = comment_data, db = db)
    except CourseNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error when adding comment"
        )

@router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(
    course_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    try:
        course_service.delete_course(course_id=course_id, user_id=current_user.id, db=db)
    except CourseNotFoundError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
    except AuthenticationError as e:
        raise HTTPException(
            status_code=403,
            detail=str(e)
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error when deleting course"
        )