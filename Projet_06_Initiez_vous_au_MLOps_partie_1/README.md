# 🧠 Projet-6 — Initiez-vous au **MLOps** (Partie 1/2)  
### *Système de Scoring Crédit pour la société « Prêt à dépenser »*

![Status](https://img.shields.io/badge/status-en%20cours-orange)
![MLOps](https://img.shields.io/badge/MLOps-pipeline-blue)
![MLflow](https://img.shields.io/badge/MLflow-tracking-informational)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML-green)
![Licence](https://img.shields.io/badge/licence-MIT-lightgrey)

---

## 📌 Contexte métier

Vous êtes **Data Scientist** au sein de la société financière **« Prêt à dépenser »**, spécialisée dans les **crédits à la consommation pour des clients avec peu ou pas d’historique bancaire**.

L’entreprise souhaite développer un **outil de scoring crédit** capable de :

- Estimer la **probabilité de défaut de paiement** d’un client  
- Décider automatiquement si un **crédit est accordé ou refusé**  
- Être **interprétable**, afin que les chargés d’étude puissent justifier les décisions auprès des clients et des régulateurs  

Les données proviennent de multiples sources :  
- Historique client  
- Comportement bancaire  
- Institutions financières externes  

---

## 🎯 Objectifs du projet

Ce projet vise à mettre en place un **pipeline MLOps complet**, allant de la préparation des données à la sélection d’un modèle prêt pour la pré-production.

### Objectifs principaux

1. **Construire un modèle de scoring crédit**  
   - Prédire la probabilité de défaut d’un client  
   - Optimiser la performance métier (coût de mauvais classement)  

2. **Assurer la transparence du modèle**  
   - Feature importance globale  
   - Feature importance locale (au niveau d’un client)  

3. **Mettre en place une approche MLOps**  
   - Tracking des expériences  
   - Versionnement des modèles  
   - Comparaison des runs  
   - Sélection du meilleur modèle prêt à être déployé   

---

## 🧱 Architecture MLOps

Ce projet met en œuvre une chaîne MLOps structurée :
```
Données brutes  
↓
Préprocessing & Feature Engineering  
↓
Entraînement multi-modèles  
↓
Tracking avec MLflow  
↓
Optimisation métier  
↓
Sélection du meilleur modèle  
```


---

## 🗂️ Contenu du projet

### 🧩 Étape préalable — Préparez l’environnement de travail  
- Installation des librairies (MLflow, scikit-learn, pandas, etc.)  
- Organisation du projet  
- Configuration du tracking MLflow  

---

### 🧹 Étape 1 — Préparez, nettoyez et enrichissez les données  
- Jointure des tables du dataset Home Credit  
- Gestion des valeurs manquantes  
- Encodage des variables catégorielles  
- Feature engineering  
- Construction du dataset d’entraînement  

---

### 📊 Étape 2 — Traquez les expérimentations avec MLflow  
- Tracking des métriques  
- Logging des hyperparamètres  
- Sauvegarde automatique des modèles  
- Comparaison des runs  

---

### 🤖 Étape 3 — Modélisez et expérimentez avec plusieurs algorithmes  
- Entraînement de plusieurs modèles :  
  - Logistic Regression  
  - Random Forest  
  - Gradient Boosting  
  - (autres modèles si pertinent)  
- Évaluation via :  
  - ROC-AUC  
  - Precision / Recall  
  - Business cost  

---

### 🎯 Étape 4 — Optimisez les hyperparamètres et le seuil métier  
- Recherche des meilleurs hyperparamètres  
- Optimisation du **seuil de décision**  
- Minimisation du **coût métier**  
  - Faux positifs (crédit refusé à tort)  
  - Faux négatifs (défaut non détecté)  

---

## 🔍 Interprétabilité du modèle  

Le projet inclut une analyse complète de l’explicabilité :  

- **Globale**  
  → Quelles variables influencent le plus les décisions du modèle ?  

- **Locale**  
  → Pourquoi un client précis a-t-il obtenu ce score ?  

Cela permet :  
- De respecter les exigences réglementaires  
- D’améliorer la confiance métier  
- De détecter des biais potentiels  

---

## 📦 Livrables  

- Pipeline MLOps reproductible  
- Modèles trackés dans MLflow  
- Dashboard de comparaison des runs  
- Modèle optimisé prêt pour la pré-production  
- Analyses d’explicabilité  

---

## 🛣️ Roadmap — Améliorations futures  

### 🔜 Court terme  
- [ ] Ajouter un pipeline de validation croisée  
- [ ] Ajouter un suivi de dérive des données (data drift)  
- [ ] Automatiser le préprocessing avec `sklearn.pipeline`  
- [ ] Exporter le modèle au format ONNX  

### 🚀 Moyen terme  
- [ ] Déployer le modèle via une API (FastAPI)  
- [ ] Ajouter un monitoring en production  
- [ ] Ajouter un dashboard de suivi des performances  

### 🧠 Long terme  
- [ ] Intégrer un Feature Store  
- [ ] Mettre en place du retraining automatique  
- [ ] Ajouter un système d’A/B testing des modèles  

---

## 🏁 Conclusion  

Ce projet met en œuvre une **démarche professionnelle MLOps**, orientée **performance métier, traçabilité, interprétabilité et déploiement futur**.  

Il constitue une base solide pour :  
- La mise en production d’un système de scoring crédit  
- La conformité réglementaire  
- L’industrialisation du Machine Learning en entreprise  

---

## 🔗 Liens & ressources du projet

### ⚙️ Exécution & Notebook Colab

Je fournis un **Notebook Colab** prêt à l’emploi.   

**Ouvrez directement le notebook dans Colab (aucune installation locale nécessaire) :**  
- ***Notebook 01 — Élaboration du modèle de scoring (Partie 1)*** 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raym648/OpenClassRooms_Projets_AI_Engineer/blob/main/Projet_06_Initiez_vous_au_MLOps_partie_1/2025-12-30_Notebook01_Élaborez_un_modèle_de_scoring_partie_1.ipynb)

---

> Contient l’intégralité du pipeline de préparation des données, de modélisation et d’expérimentation.

---

### 📊 Dashboard MLflow (Hugging Face Spaces)

Accédez au dashboard MLflow interactif pour :
- Visualiser les runs
- Comparer les modèles
- Explorer les hyperparamètres
- Analyser les métriques métier

🚀 **HF Space – Projet 06 MLOps MLflow**  
👉 https://remdev-ai-projet-06-mlops-mlflow.hf.space

> Ce Space expose l’interface MLflow utilisée pour le suivi MLOps du projet.

---

**Auteur :** *[Raymond Francius]*   
**Rôle :** *[Apprenant - Promotion Sept-2025]* — **Engineer AI** — **Openclassrooms**    
**Date de mise à jour :** *[14-01-2026]*   
**Client fictif :** Société Financière, nommée "**Prêt à dépenser**"    
**Projet :** Projet-6 — Initiez-vous au MLOps (partie 1/2)  
