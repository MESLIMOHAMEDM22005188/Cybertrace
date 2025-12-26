from fastapi import APIRouter
from typing import List
from rss_parser import fetch_vulnerabilities
from models import Vulnerability

router = APIRouter()

@router.get("/vulnerabilities", response_model=List[Vulnerability])
def get_vulnerabilities():
    """
    Retourne la liste des vulnérabilités publiées par le CERT-FR au format JSON.
    """
    return fetch_vulnerabilities()
