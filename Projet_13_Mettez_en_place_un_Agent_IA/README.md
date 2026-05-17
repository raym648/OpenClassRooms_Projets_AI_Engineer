# ♟️ Projet-13 — Mettez en place un Agent IA  
## Agent IA d’apprentissage des ouvertures d’échecs — Fédération Française des Échecs (FFE)

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Angular](https://img.shields.io/badge/Angular-Frontend-DD0031?logo=angular)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Orchestration-black)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb)
![Milvus](https://img.shields.io/badge/Milvus-Vector%20Database-00BFA5)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker)
![Stockfish](https://img.shields.io/badge/Stockfish-Chess%20Engine-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

# 📌 Contexte du projet

Dans le cadre d’une mission réalisée pour la Fédération Française des Échecs (FFE), ce projet consiste à concevoir un Proof of Concept (POC) d’un Agent IA capable d’accompagner les jeunes joueurs dans l’apprentissage des ouvertures aux échecs.

L’objectif principal est de démontrer la faisabilité technique d’un système intelligent capable d’analyser une position d’échecs, de proposer des recommandations pertinentes et d’enrichir l’expérience pédagogique grâce à plusieurs sources de connaissances externes.

Le projet a été développé dans une logique orientée IA appliquée, orchestration d’agents, recherche vectorielle et intégration de moteurs spécialisés.

---

# 🎯 Objectifs de la mission

L’Agent IA doit être capable de :

- ♟️ Identifier une position via la notation FEN
- 📚 Reconnaître les ouvertures d’échecs
- 🧠 Proposer les meilleurs coups théoriques
- 📈 Évaluer une position avec Stockfish
- 🎥 Afficher des vidéos YouTube pertinentes
- 🔎 Interroger une base vectorielle Milvus (RAG)
- 🌐 Exploiter les APIs Lichess
- 🖥️ Fournir une interface utilisateur Angular interactive
- 🐳 Être exécutable localement avec Docker Compose

---

# 🏗️ Architecture Technique

Le projet repose sur une architecture modulaire orientée IA et micro-services.

## Backend IA

Le backend est construit avec FastAPI et LangGraph afin d’orchestrer les différents composants de l’agent intelligent :

- Détection d’ouverture
- Analyse de position
- Recherche vectorielle
- Génération de recommandations
- Intégration des APIs externes

## Frontend Angular

L’interface utilisateur repose sur Angular et ngx-chessground afin de proposer :

- Un échiquier interactif
- Une visualisation dynamique des coups
- Une expérience d’apprentissage intuitive
- Une communication temps réel avec l’agent IA

## Base Vectorielle (RAG)

Milvus est utilisé pour indexer et rechercher des connaissances échiquéennes provenant de Wikichess et d’autres ressources spécialisées.

Cette approche permet :

- La recherche sémantique
- L’enrichissement contextuel
- La récupération de variantes d’ouvertures
- L’assistance IA contextualisée

---

# ⚙️ Stack Technique

|-------------------|--------------------------------------|
| Domaine           | Technologies                         |
|-------------------|--------------------------------------|
| Frontend          | Angular, TypeScript, ngx-chessground |
| Backend           | FastAPI, Python                      |
| Orchestration IA  | LangGraph                            |
| Moteur d’échecs   | Stockfish                            |
| Base vectorielle  | Milvus                               |
| Base documentaire | MongoDB                              |
| APIs externes     | Lichess API, YouTube API             |
| Conteneurisation  | Docker, Docker Compose               |

---

# 🧩 Fonctionnalités principales

## 1 — Analyse intelligente des ouvertures

L’agent IA identifie automatiquement les ouvertures d’échecs à partir de la position courante.

Chaque position est enrichie grâce :

- aux bases théoriques,
- aux parties historiques,
- aux analyses moteurs,
- aux ressources pédagogiques externes.

---

## 2 — Évaluation de position avec Stockfish

Lorsque la partie sort des lignes théoriques connues, l’agent interroge Stockfish afin de :

- calculer les meilleurs coups,
- fournir une évaluation de la position,
- détecter les erreurs stratégiques,
- guider l’apprentissage du joueur.

---

## 3 — Recherche augmentée (RAG)

Le système utilise Milvus pour effectuer une recherche vectorielle sur des contenus spécialisés liés aux ouvertures d’échecs.

Cette couche RAG permet :

- une meilleure contextualisation,
- des réponses enrichies,
- une assistance plus pertinente,
- une meilleure expérience utilisateur.

---

## 4 — Intégration YouTube intelligente

L’application récupère automatiquement des vidéos pédagogiques pertinentes selon la position ou l’ouverture détectée.

L’objectif est d’améliorer l’apprentissage via :

- des analyses visuelles,
- des explications stratégiques,
- des démonstrations pratiques,
- des contenus spécialisés.

---

## 5 — Analyse vidéo avancée

Le projet prévoit également une pipeline IA orientée Computer Vision permettant :

- le stockage des vidéos,
- l’extraction automatique des frames,
- la détection d’échiquiers,
- la conversion des positions détectées en notation FEN.

Cette approche ouvre la voie à des fonctionnalités avancées d’analyse automatique de contenu échiquéen.

---

# 📂 Structure du projet

```bash
project/
│
├── backend/
│   ├── app/
│   ├── agents/
│   ├── rag/
│   ├── api/
│   └── services/
│
├── frontend/
│   ├── src/
│   └── app/
│
├── docker/
├── data/
├── notebooks/
└── docker-compose.yml
```

---

# 🚀 Étapes du projet

## Étape 1 — Préparation de l’environnement

Mise en place du socle technique :

- Docker Compose
- FastAPI
- Angular
- MongoDB
- Milvus
- dépendances IA

---

## Étape 2 — Développement de l’Agent LangGraph

Construction des nœuds LangGraph :

- détection d’ouverture,
- récupération de contexte,
- orchestration IA,
- analyse moteur,
- génération des réponses.

---

## Étape 3 — Intégration Milvus (RAG)

Création du pipeline vectoriel :

- ingestion de données,
- embeddings,
- indexation,
- recherche sémantique.

---

## Étape 4 — Intégration de l’API YouTube

Développement du système de récupération vidéo :

- recherche contextuelle,
- affichage dynamique,
- enrichissement pédagogique.

---

## Étape 5 — Développement Frontend Angular

Création de l’interface utilisateur :

- échiquier interactif,
- visualisation des coups,
- affichage des analyses IA,
- intégration des vidéos.

---

## Étape 6 — Packaging & Déploiement

Industrialisation du projet :

- Dockerisation,
- orchestration multi-services,
- exécution locale,
- démonstration client.

---

# ▶️ Lancement du projet

## 1 — Cloner le dépôt

```bash
git clone <repo-url>
cd project
```

## 2 — Construire les conteneurs

```bash
docker compose up --build
```

## 3 — Accéder aux services

|------------------|----------------------------|
| Service          | URL                        |
|------------------|----------------------------|
| Frontend Angular | http://localhost:4200      |
| Backend FastAPI  | http://localhost:8000      |
| Swagger API      | http://localhost:8000/docs |

---

# 🧪 Exemple de workflow utilisateur

1. L’utilisateur joue des coups sur l’échiquier.
2. La position FEN est générée automatiquement.
3. L’agent IA identifie l’ouverture.
4. Les meilleurs coups théoriques sont proposés.
5. Stockfish évalue la position.
6. Des vidéos YouTube pertinentes sont affichées.
7. Les connaissances RAG enrichissent les recommandations.

---

# 📈 Perspectives d’évolution

Le projet peut évoluer vers une plateforme IA complète d’apprentissage des échecs avec :

- analyse temps réel,
- entraînement personnalisé,
- recommandations adaptatives,
- agents multi-modèles,
- analyse comportementale des joueurs,
- pipeline Computer Vision avancée,
- déploiement cloud scalable.

---

# 🛣️ Roadmap

## Phase 1 — Stabilisation du POC

- [ ] Finaliser les pipelines LangGraph
- [ ] Optimiser les appels APIs externes
- [ ] Ajouter une gestion avancée des erreurs
- [ ] Améliorer la qualité des réponses IA
- [ ] Renforcer la couverture des ouvertures

---

## Phase 2 — Industrialisation

- [ ] Mise en place CI/CD GitHub Actions
- [ ] Monitoring et observabilité
- [ ] Logging centralisé
- [ ] Gestion des secrets sécurisée
- [ ] Tests automatisés backend/frontend

---

## Phase 3 — IA avancée

- [ ] Fine-tuning de modèles spécialisés échecs
- [ ] Multi-agent orchestration
- [ ] Analyse automatique de parties vidéo
- [ ] Détection IA des erreurs stratégiques
- [ ] Génération automatique d’exercices

---

## Phase 4 — Production & Scalabilité

- [ ] Déploiement Kubernetes
- [ ] Scalabilité horizontale
- [ ] Cache intelligent
- [ ] Streaming temps réel
- [ ] API publique sécurisée

---

# 🚀 Démo & Accès

## 💻 Dépôt GitHub  
👉 **Code source complet** :  
👉 [https://github.com/raym648/POC-Agent-AI-ouvertures-echecs-FFE.git](https://github.com/raym648/POC-Agent-AI-ouvertures-echecs-FFE.git)

---

# 📚 Ressources utiles

- FEN Chess Notation  
  https://www.chess.com/terms/fen-chess

- Lichess API  
  https://lichess.org/api

- Stockfish  
  https://pypi.org/project/stockfish/

- Milvus  
  https://milvus.io/

- LangGraph  
  https://www.langchain.com/langgraph

- YouTube API  
  https://developers.google.com/youtube/v3

---

**Auteur :** *[Raymond Francius]*   
**Rôle :** *[Apprenant - Promotion Sept-2025]* — **Engineer AI** — **Openclassrooms**    
**Date de mise à jour :** *[20-04-2026]*   
**Client fictif :** "**Fédération Française des Échecs (FFE)**"   
**Projet :** Projet-13 — Mettez en place un Agent IA  
