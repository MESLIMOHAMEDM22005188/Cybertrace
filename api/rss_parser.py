import feedparser
from config import CERT_RSS_URL
from models import Vulnerability

def fetch_vulnerabilities():
    """
    Récupère les vulnérabilités depuis le flux RSS du CERT-FR
    et retourne une liste de Vulnerability (JSON-friendly).
    """
    # Parser le flux RSS
    feed = feedparser.parse(CERT_RSS_URL)
    vulnerabilities = []

    # Parcourir chaque entrée du flux RSS
    for entry in feed.entries:
        vulnerabilities.append(
            Vulnerability(
                title=entry.title,
                link=entry.link,
                published=entry.published,
                summary=entry.summary
            )
        )

    return vulnerabilities
