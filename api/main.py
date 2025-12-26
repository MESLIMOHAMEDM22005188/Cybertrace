from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import router  # api/api.py

app = FastAPI(
    title="Cybertrace API",
    description="Agrégateur de vulnérabilités CERT-FR",
    version="1.0.0"
)

# CORS (ouvert pour tests / CLI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes API
app.include_router(router)

@app.get("/")
def root():
    return {
        "app": "Cybertrace",
        "status": "running",
        "endpoint": "/vulnerabilities"
    }
