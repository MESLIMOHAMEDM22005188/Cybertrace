from pydantic import BaseModel

class Vulnerability(BaseModel):
    """
    Modèle représentant une vulnérabilité du CERT-FR.
    Utilisé pour la sérialisation JSON dans l'API et la CLI.
    """
    title: str       # Titre de la vulnérabilité
    link: str        # Lien vers l'avis complet sur le site du CERT-FR
    published: str   # Date de publication
    summary: str     # Résumé ou description courte
