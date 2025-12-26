import requests
from rich.console import Console
from rich.table import Table

# URL de l'API Cybertrace
API_URL = "http://127.0.0.1:8000/vulnerabilities"

# Console Rich pour affichage coloré
console = Console()

def main():
    console.print("\n[bold cyan]Cybertrace[/bold cyan] — CERT-FR Monitor\n")

    try:
        # Requête GET vers l'API
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        vulns = response.json()
    except Exception as e:
        console.print(f"[red]Erreur API : {e}[/red]")
        return

    # Création du tableau pour affichage
    table = Table(title="Vulnérabilités CERT-FR")

    table.add_column("Date", style="dim", width=25)
    table.add_column("Titre", style="bold")
    table.add_column("Lien", style="blue")

    # Limiter à 10 vulnérabilités pour lisibilité
    for v in vulns[:10]:
        table.add_row(
            v["published"],
            v["title"],
            v["link"]
        )

    # Affichage
    console.print(table)

if __name__ == "__main__":
    main()
