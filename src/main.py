from fastapi import FastAPI
from blog.router import router as blog_router

app = FastAPI()


app.include_router(blog_router)
