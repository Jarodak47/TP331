from fastapi import APIRouter

from .user_controller import router as user
from .authentication_controller import router as authentication
from .migration_controller import router as migration
from .storage_controller import router as storage
from .role_controller import router as role

api_router = APIRouter()

api_router.include_router(authentication)
api_router.include_router(user)
api_router.include_router(migration)
api_router.include_router(storage)
api_router.include_router(role)