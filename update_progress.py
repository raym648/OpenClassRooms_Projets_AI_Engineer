import re
import json

# Fichiers
README_FILE = "README.md"
PROGRESS_FILE = "progress.json"
TOTAL_PROJECTS = 15  # nombre total de projets attendus

def get_progress_from_readme(readme_file):
    """Compter le nombre de projets terminés [x] dans le README"""
    with open(readme_file, "r", encoding="utf-8") as f:
        content = f.read()

    completed = len(re.findall(r"- \[x\]", content, re.IGNORECASE))
    return completed

def calculate_percentage(completed, total):
    """Calculer le pourcentage d'avancement"""
    return int((completed / total) * 100) if total > 0 else 0

def get_color(percentage):
    """Choisir la couleur du badge selon la progression"""
    if percentage <= 30:
        return "red"
    elif percentage <= 60:
        return "orange"
    elif percentage <= 90:
        return "green"
    else:
        return "brightgreen"

def update_progress_json(completed, total, percentage, color, progress_file):
    """Mettre à jour le fichier progress.json"""
    data = {
        "schemaVersion": 1,
        "label": "Progression",
        "message": f"{percentage}%",
        "color": color
    }

    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Progression mise à jour : {completed}/{total} ({percentage}%) → Couleur = {color}")

if __name__ == "__main__":
    completed = get_progress_from_readme(README_FILE)
    percentage = calculate_percentage(completed, TOTAL_PROJECTS)
    color = get_color(percentage)

    update_progress_json(completed, TOTAL_PROJECTS, percentage, color, PROGRESS_FILE)
