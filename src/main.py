from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.endpoints import router as v1_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers for versions
app.include_router(v1_router, prefix='/v1')

@app.get('/')
def read_root():
    return {'message': 'Welcome to Matrino :)'}
