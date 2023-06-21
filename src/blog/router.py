from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from blog.models import Post
from database import AsyncSession, get_async_session
from blog.schemas import CreatePost, UpdatePost

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
async def create_post(payload: CreatePost, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Post).values(**payload.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success", "data": payload}


@router.patch("/{id}")
async def update_post(id: int, payload: UpdatePost, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Post).where(Post.id == id).values(**payload.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success", "data": payload}


@router.delete("/{id}")
async def delete_post(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Post).where(Post.id == id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
