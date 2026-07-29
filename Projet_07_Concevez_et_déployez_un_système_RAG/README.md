# 🎭 Projet-7 — Concevez et déployez un système RAG  
### Assistant intelligent de recommandation d’évènements culturels

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green.svg)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange.svg)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-lightgrey.svg)
![Mistral](https://img.shields.io/badge/LLM-Mistral-purple.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![Status](https://img.shields.io/badge/Status-POC%20fonctionnel-success.svg)

---

## 📌 Contexte & Mission

Dans le cadre de ce **Projet-7**, je joue le rôle d’un **Engineer Intelligence Artificielle freelance**, spécialisé en **NLP** et en **systèmes RAG (Retrieval-Augmented Generation)**.

Je suis missionné par **Puls-Events**, une entreprise technologique développant une plateforme de **recommandations culturelles personnalisées**, afin de concevoir un **assistant conversationnel intelligent** capable de répondre aux questions des utilisateurs sur les **événements culturels à venir**.

🎯 **Objectif principal**  
Livrer un **POC complet et démontrable** prouvant la faisabilité technique, la pertinence métier et la performance d’un chatbot RAG exploitant les données publiques **Open Agenda**.

---

## 🧠 Description du POC

Le système repose sur une architecture **RAG moderne**, combinant :

- 🔎 **Recherche vectorielle** (FAISS) sur des événements culturels récents (< 1 an)
- 🤖 **Génération de réponses augmentées** via un LLM **Mistral**
- 🔗 **Orchestration RAG avec LangChain**
- 🚀 **Exposition via une API REST FastAPI**
- 📦 **Conteneurisation Docker** pour une démonstration locale

Les données sources proviennent de l’API Open Agenda :  
👉 https://public.opendatasoft.com/explore/dataset/evenements-publics-openagenda

---

## 🏗️ Architecture technique (vue d’ensemble)
```bash
Open Agenda API
↓
Pré-processing & nettoyage
↓
Vectorisation (embeddings)
↓
FAISS (base vectorielle)
↓
LangChain (Retriever + LLM Mistral)
↓
FastAPI (endpoint REST)
↓
Client / Dashboard / Démo live
```

---

## 📂 Organisation du dépôt
```bash
├── data/ # Données brutes et pré-processées
├── ingestion/ # Scripts d'extraction & nettoyage Open Agenda
├── vectorstore/ # Construction et reconstruction de l’index FAISS
├── rag/ # Chaînes LangChain & logique RAG
├── api/ # API FastAPI (endpoints REST)
├── tests/ # Tests unitaires & jeux de tests annotés
├── evaluation/ # Scripts de métriques (qualité & performance)
├── docker/ # Dockerfile & configurations
├── slides/ # Support de présentation (démo)
└── README.md # Documentation technique (ce fichier)
```

---

## 🧪 Fonctionnalités livrées

✔ Système RAG fonctionnel (LangChain + Mistral + FAISS)  
✔ Reconstruction automatisée de l’index vectoriel  
✔ API REST FastAPI (question → réponse augmentée)  
✔ Jeu de tests annoté (Q/R de référence)  
✔ Tests unitaires & métriques d’évaluation  
✔ Conteneur Docker prêt pour démo locale  
✔ Documentation technique complète  

---

## 🧭 Étapes du projet

### Étape 1 — Configuration de l’environnement
- Environnement Python
- Dépendances NLP & RAG
- Paramétrage des variables et modèles

### Étape 2 — Pré-processing des données Open Agenda
- Filtrage géographique
- Nettoyage et normalisation
- Structuration des événements

### Étape 3 — Base de données vectorielle (FAISS)
- Génération d’embeddings
- Indexation vectorielle
- Scripts de reconstruction

### Étape 4 — Intégration LangChain (RAG)
- Retriever FAISS
- Prompting métier
- Chaîne RAG complète

### Étape 5 — API REST (FastAPI)
- Endpoint `/ask`
- Schémas d’entrée/sortie
- Gestion des erreurs

### Étape 6 — Conteneurisation & démonstration
- Dockerisation du endpoint
- Lancement local
- Préparation de la démo live

---

## 🎯 Objectifs pédagogiques couverts

- ✅ Création de **processus de test et d’évaluation**
- ✅ Exposition des résultats via une **API exploitable**
- ✅ Intégration d’une **API externe (Open Agenda)**
- ✅ Sélection et intégration d’un **modèle adapté aux contraintes métier**

---

## 🚀 Démo & Accès

### 🔗 Dashboard & API (Hugging Face Spaces)  
👉 **Démo live & accès API**  
👉 [https://remdev-ai-rag-dashboard.hf.space](https://remdev-ai-rag-dashboard.hf.space)

### 💻 Dépôt GitHub  
👉 **Code source complet** :  
👉 [https://github.com/RemDev-AI/puls-events-chatbot-intelligent-rag](https://github.com/RemDev-AI/puls-events-chatbot-intelligent-rag)

---

## 🗺️ Roadmap & Perspectives

### 🔮 Améliorations futures
- [ ] Ajout de la **recherche multi-critères** (date, type, budget)
- [ ] Support **multi-zones géographiques**
- [ ] Amélioration du **prompt engineering**
- [ ] Intégration d’un **re-ranking sémantique**
- [ ] Mémoire conversationnelle utilisateur
- [ ] Monitoring qualité (logs & feedback utilisateur)
- [ ] Déploiement cloud (CI/CD)

### 🧩 TODO techniques
- [ ] Tests de charge API
- [ ] Benchmark multi-modèles LLM
- [ ] Cache des requêtes fréquentes
- [ ] Authentification API
- [ ] Versioning des index FAISS

---

✨ *Ce projet illustre une approche end-to-end, prête pour un passage à l’échelle produit.*  
Projet réalisé dans le cadre d’un parcours orienté **MLOps, NLP & systèmes RAG**  

---

**Auteur :** *[Raymond Francius]*   
**Rôle :** *[Apprenant - Promotion Sept-2025]* — **Engineer AI** — **Openclassrooms**    
**Date de mise à jour :** *[21-01-2026]*   
**Client fictif :** *Puls-Events*    
**Projet :** *Projet-7 - Concevez et déployez un système RAG*  
