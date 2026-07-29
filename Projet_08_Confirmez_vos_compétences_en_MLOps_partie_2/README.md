
# 🚀 Projet 8 – Confirmez vos compétences en MLOps (Partie 2)  
### *Système de Scoring Crédit pour la société « Prêt à dépenser »*

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-orange)
![Monitoring](https://img.shields.io/badge/Monitoring-Data%20Drift-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🎯 Contexte métier

Je suis **Engineer AI chez "Prêt à Dépenser"**, en charge de la mise en production d’un modèle de scoring crédit destiné au département **Crédit Express**.

Suite au développement et au versioning du modèle (Projet précédent – Initiation MLOps), l’objectif est désormais de :

- Déployer une **API robuste et conteneurisée (Docker Ready)**  
- Mettre en place un **monitoring proactif en production**  
- Automatiser le déploiement via un pipeline **CI/CD**  
- Garantir la performance, la fiabilité et la traçabilité du modèle dans le temps  

---

# 🧱 Architecture Globale

```
Client → API FastAPI → Modèle ML (Scoring)  
                         ↓  
                 Logs & Monitoring  
                         ↓  
            Dashboard (Streamlit / Rapport)  
                         ↓  
                CI/CD (GitHub Actions)
```

---

# 📌 Livrables du Projet

## 1️⃣ Contrôle de version & Historique Git

- Dépôt GitHub structuré
- Historique des commits retraçant toutes les étapes
- Messages de commits alignés standards MLOps
- Versioning clair des artefacts

---

## 2️⃣ API de Scoring

### 🔹 FastAPI Production Ready

- Endpoint `/predict`
- Entrée : données client
- Sortie : probabilité de défaut + décision crédit

Règle métier implémentée :

```
SI proba_defaut < seuil  → Crédit accordé  
SINON                    → Crédit refusé
```

### 🔹 Tests unitaires

- Pytest
- Validation du schéma d’entrée
- Tests de cohérence des prédictions
- Vérification des statuts HTTP

---

## 3️⃣ Conteneurisation

- Dockerfile optimisé
- Image reproductible
- Compatible déploiement Cloud / Local
- Isolation complète des dépendances

---

## 4️⃣ Monitoring & Data Drift

### 📊 Dashboard de monitoring

- Distribution des scores prédits
- Latence API
- Temps d’inférence
- Suivi volumétrie des requêtes
- Analyse du Data Drift (Evidently)

### 📂 Stockage des données de production

- Logs structurés
- Fichiers JSON normalisés
- Artefacts versionnés
- Screenshots de la solution de stockage

---

## 5️⃣ Pipeline CI/CD

GitHub Actions :

- Lancement automatique des tests
- Analyse de drift en CI
- Génération de rapports
- Validation avant merge sur `main`
- Déploiement automatisé (si applicable)

---

# 📚 Structure du Projet

```
.
├── app/                    # API FastAPI
├── monitoring/             # Drift + dashboard
├── tests/                  # Tests unitaires
├── .github/workflows/      # CI/CD
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ⚙️ Lancer le projet en local

## 1️⃣ Installation

```bash
pip install -r requirements.txt
```

## 2️⃣ Lancer l’API

```bash
uvicorn app.main:app --reload
```

## 3️⃣ Docker

```bash
docker build -t scoring-api .
docker run -p 8000:8000 scoring-api
```

---

# 📈 Étapes du Projet

## ✅ Étape 1 – Contrôle de version & dépôt
- Structuration Git
- Historique propre
- Versioning

## ✅ Étape 2 – API + CI/CD
- Déploiement FastAPI
- Tests automatisés
- Pipeline GitHub Actions

## ✅ Étape 3 – Stockage & Analyse production
- Logs production
- Rapports Drift
- Dashboard monitoring

## ✅ Étape 4 – Analyse & Optimisation
- Analyse latence
- Optimisation temps d’inférence
- Ajustement seuil métier
- Interprétation métriques

---

## 🚀 Démo & Accès

### 🔗 Dashboard (Hugging Face Spaces)  
👉 **Démo live**  
👉 [https://remdev-ai-pret-a-depenser-scoring-dashboard.hf.space/](https://remdev-ai-pret-a-depenser-scoring-dashboard.hf.space/)

### 💻 Dépôt GitHub  
👉 **Code source complet** :  
👉 [https://github.com/RemDev-AI/pret-a-depenser-scoring-deployment-monitoring](https://github.com/RemDev-AI/pret-a-depenser-scoring-deployment-monitoring)

---

# 🛣 Roadmap – Améliorations futures

## 🔜 Court terme

- [ ] Ajout monitoring Prometheus
- [ ] Intégration Grafana
- [ ] Logging structuré centralisé (OpenSearch)
- [ ] Authentification API (JWT)

## 🔜 Moyen terme

- [ ] Déploiement Kubernetes
- [ ] Canary deployment
- [ ] MLflow Model Registry complet
- [ ] Monitoring performance business (ROI crédit)

## 🔜 Long terme

- [ ] Feature Store
- [ ] Auto-retraining déclenché par drift
- [ ] Observabilité complète ML (ML Observability Stack)
- [ ] Architecture serverless scalable

---

# 🏆 Compétences démontrées

- ✅ MLOps end-to-end
- ✅ Déploiement API ML
- ✅ Docker & Conteneurisation
- ✅ CI/CD industriel
- ✅ Monitoring & Data Drift
- ✅ Analyse performance modèle
- ✅ Gouvernance & traçabilité

---

**Auteur :** *[Raymond Francius]*   
**Rôle :** *[Apprenant - Promotion Sept-2025]* — **Engineer AI** — **Openclassrooms**    
**Date de mise à jour :** *[11-02-2026]*   
**Client fictif :** Société Financière, nommée "**Prêt à dépenser**"    
**Projet :** Projet-8 - Confirmez vos compétences en MLOps (Partie 2)  

---

⭐ Si ce projet vous intéresse, n'hésitez pas à explorer le code et les pipelines CI/CD !
