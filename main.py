from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import engine
from backend.models import Base
from backend.api.api_ai import router as ai_router
from backend.api.api_products import router as products_router
from backend.api.api_youtube import router as youtube_router
from backend.api.api_classify import router as classify_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(engine)

# Include routers
app.include_router(ai_router)
app.include_router(products_router)
app.include_router(youtube_router)
app.include_router(classify_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 