# 🚀 Projet 4 — *Classifiez automatiquement des informations*  
### _(Formation Ingénieur Intelligence Artificielle – Projet HR Analytics)_

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=Python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-green?logo=scikitlearn)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-purple)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Category](https://img.shields.io/badge/Category-HR%20Analytics-grey)

---

## 📌 Résumé Professionnel du Projet

Ce projet s’inscrit dans un cas réel d’**analyse RH** au sein de l’ESN *TechNova Partners*, confrontée à une hausse significative de son **taux d’attrition**.  
En tant que **Consultant Data Scientist**, l’objectif est d’identifier les *causes racines des démissions* et de développer un **modèle de classification** prédictif du risque de départ.

L’analyse repose sur trois sources principales de données fournies par le département SIRH :

- **Extrait du SIRH** : âge, fonction, ancienneté, salaire, données sociodémographiques.
- **Évaluations annuelles** : notes de performance, feedback, satisfaction.
- **Sondage interne** : perception du bien-être, environnement de travail, intention de départ.

Le travail comprend :  
🔍 *Analyse exploratoire* – 🧹 *Préparation de la donnée* – 🤖 *Modélisation* – 🚀 *Optimisation* – 🧠 *Interprétation SHAP*.  
L’objectif final : fournir aux RH une **vision objective, chiffrée et actionnable** sur les facteurs expliquant les départs.

---

# 📂 Structure du Projet

## 🔧 Étape préalable — Préparez l’environnement de travail
- Mise en place de l’environnement Python (Pandas, Scikit-Learn, SHAP).
- Import des trois fichiers sources.
- Vérification de l’intégrité des colonnes et formats.
- Mise en place du versionnement Git/GitHub.

---

## 🔍 Étape 1 — Analyse exploratoire des fichiers de données
- Comparaison employés *actifs* vs *démissionnaires*.
- Analyse univariée & multivariée :
  - salaire, ancienneté, notes de satisfaction, charge de travail.
- Recherche de patterns discriminants :
  - anomalies, valeurs extrêmes, variables à forte corrélation.
- Visualisations pour formuler les premières hypothèses de causes d’attrition.

---

## 🧹 Étape 2 — Préparation de la donnée pour la modélisation
- Fusion des sources via un ID unique.
- Nettoyage des valeurs manquantes et harmonisation des formats.
- Encodage des variables catégorielles.
- Standardisation / normalisation selon les modèles.
- Gestion du déséquilibre de classes : `class_weight` ou SMOTE.
- Création d’un dataset final prêt pour la modélisation.

---

## 🤖 Étape 3 — Réalisation d’un premier modèle de classification
- Split Train/Test (stratifié).
- Baseline via `DummyClassifier` pour mesurer le gain réel.
- Premiers modèles :
  - Régression Logistique  
  - Random Forest  
  - XGBoost
- Évaluation selon :
  - Accuracy  
  - Recall  
  - F1-score  
  - AUC ROC

---

## 🚀 Étape 4 — Amélioration de l’approche de classification
- Optimisation des hyperparamètres : GridSearch / RandomizedSearch.
- Comparaison de plusieurs pipelines.
- Sélection d’attributs importants (feature selection).
- Réduction du sur-apprentissage + stabilisation des performances.

---

## 🧠 Étape 5 — Optimisation et interprétation du modèle (SHAP)
- Feature importance **globale** :
  - Satisfaction  
  - Note de performance  
  - Ancienneté  
  - Salaire  
  - Charge de travail  
- Analyse **locale** via waterfall plots pour expliquer chaque prédiction.  
- Identification de **leviers RH actionnables** :
  - Amélioration du management  
  - Ajustements sur la charge de travail  
  - Programmes de reconnaissance  
  - Actions sur les salaires / promotions

---

# 🧭 Roadmap — Améliorations Futures & TODO

### 🔄 Modèle & Performance
- [ ] Intégrer LightGBM et CatBoost pour comparaison.  
- [ ] Ajouter un modèle de stacking pour améliorer l’AUC.  
- [ ] Mettre en place une calibration des probabilités (Platt / Isotonic).

### 📊 Analyse & Reporting
- [ ] Ajouter un rapport automatique (ydata-profiling / Sweetviz).  
- [ ] Créer un dashboard RH interactif (Streamlit / Dash).  
- [ ] Ajouter une analyse temporelle si l’historique est disponible.

### 🧱 Pipeline & Qualité
- [ ] Industrialiser l’ensemble via `Pipeline()` + `ColumnTransformer`.  
- [ ] Ajouter des tests unitaires (PyTest) pour le preprocessing.  
- [ ] Traquer les expériences et les modèles via MLflow.

### 🧩 Exploitation RH
- [ ] Construire une matrice “Facteur → Action recommandée”.  
- [ ] Définir des personas d’employés à risque.  
- [ ] Automatiser un scoring mensuel des collaborateurs.

---

# 📎 Données utilisées
- `Extrait_SIRH.csv`  
- `Evaluations_performance.csv`  
- `Sondage_employes.csv`

---

Projet réalisé dans le cadre du parcours **Ingénieur en Intelligence Artificielle** – Mission HR Analytics (Projet 4).

---

**Auteur :** *[Raymond Francius]*   
**Rôle :** *[Apprenant - Promotion Sept-2025]* — **Engineer AI** — **Openclassrooms**    
**Date de mise à jour :** *[04-11-2025]*   
**Client fictif :** *TechNova Partners*      
**Projet :** Projet4 — Mission HR Analytics  
