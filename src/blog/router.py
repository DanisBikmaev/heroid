from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from blog.models import Post
from database import AsyncSession, get_async_session
from blog.schemas import CreatePost

router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)


@router.get("/")
async def get_all_posts(session: AsyncSession = Depends(get_async_session)):
    query = select(Post)
    res = await session.scalars(query)
    return res.all()


@router.get("/{id}")
async def get_post_by_id(id: int, sesion: AsyncSession = Depends(get_async_session)):
    query = select(Post).where(Post.id == id)
    res = await sesion.scalars(query)
    return res.first()


@router.post("/")
async def create_post(new_post: CreatePost, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Post).values(**new_post.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success", "data": new_post}

# @router.patch("/{id}")
# async def update_post(new_post: )
