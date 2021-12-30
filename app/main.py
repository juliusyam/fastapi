from fastapi import FastAPI

from . import models
from .config import settings
from .database import engine
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


print(settings.secret_key)


app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)
