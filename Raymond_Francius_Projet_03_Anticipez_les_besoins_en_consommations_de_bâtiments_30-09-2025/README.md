# 🏙️ Projet 3 – Anticipez les besoins en consommations de bâtiments

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow?logo=pandas)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Modeling-orange?logo=scikitlearn)
![Google Colab](https://img.shields.io/badge/Notebook-Google%20Colab-brightgreen?logo=googlecolab)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🎯 **Mission**

Je travaille en tant que **Data Scientist pour la ville de Seattle**, engagée dans une démarche ambitieuse : **atteindre la neutralité carbone d’ici 2050**.  
Pour y parvenir, mon équipe se concentre sur la **consommation énergétique** et les **émissions de CO₂** des **bâtiments non résidentiels**.

Des relevés précis ont été effectués en **2016**. Ces données, coûteuses à obtenir, servent aujourd’hui de base pour **entraîner des modèles de prédiction** capables d’estimer les émissions et la consommation totale d’énergie pour d’autres bâtiments similaires dont les mesures n’ont pas encore été réalisées.

Mon objectif est donc de :
- Explorer et comprendre les données existantes ;  
- Construire et comparer plusieurs modèles de prédiction supervisés ;  
- Identifier les **facteurs clés influençant la consommation énergétique** des bâtiments ;  
- Fournir à la ville un outil d’aide à la décision pour prioriser les futurs relevés.

---

## 🧠 **Objectifs pédagogiques**

Ce projet m’a permis de renforcer mes compétences fondamentales en **Data Science appliquée** :

1. 🔍 Appliquer des analyses statistiques descriptives et naviguer visuellement dans les données.  
2. 🧹 Automatiser le processus de nettoyage avec Python.  
3. 🧩 Choisir un algorithme adapté aux objectifs visés.  
4. ⚙️ Configurer un environnement de travail reproductible.  
5. 🤖 Définir la procédure d'entraînement et entraîner le modèle sur les jeux de données.  
6. 📊 Mettre les variables sous une échelle commune et préparer les données à la modélisation.  
7. 🗣️ Synthétiser, simplifier et communiquer les résultats de manière claire et exploitable.

---

## 🧾 **Structure du projet**

Ce dépôt est organisé autour de **notebooks Google Colab**, correspondant à chacune des étapes clés du projet.  

| Étape | Description | Notebook |
|-------|--------------|-----------|
| **Étape 1 – Analyse exploratoire** | Compréhension des données, étude de la distribution des variables, détection des valeurs aberrantes et corrélations clés. | `01_EDA.ipynb` |
| **Étape 2 – Feature Engineering** | Transformation et enrichissement des variables : traitement des valeurs manquantes, encodage, création de nouvelles features pertinentes. | `02_Feature_Engineering.ipynb` |
| **Étape 3 – Préparation des données** | Normalisation et séparation des jeux de données (train/test). Constitution du pipeline de preprocessing. | `03_Preprocessing.ipynb` |
| **Étape 4 – Comparaison de modèles** | Évaluation de plusieurs modèles supervisés (Régression Linéaire, Random Forest, XGBoost, etc.) à l’aide de métriques adaptées. | `04_Model_Comparison.ipynb` |
| **Étape 5 – Optimisation & Interprétation** | Sélection du meilleur modèle via **GridSearchCV**, interprétation des résultats et importance des features. | `05_Model_Optimization.ipynb` |

---

## 📂 **Données**

Les données utilisées proviennent des relevés officiels de la **ville de Seattle (2016)**.  
Elles décrivent la structure, l’usage et les performances énergétiques des bâtiments non résidentiels.  

**Exemples de variables :**
- Surface du bâtiment (en m²)  
- Année de construction  
- Type d’usage (bureaux, écoles, hôpitaux, etc.)  
- Localisation géographique  
- Consommation totale d’énergie  
- Émissions de CO₂  

---

## 🧩 **Technologies et Librairies utilisées**

- **Python 3.10+**
- **NumPy / Pandas / Matplotlib / Seaborn** – pour la manipulation et la visualisation des données  
- **Scikit-learn** – pour la modélisation, le pipeline, et la validation croisée  
- **XGBoost / RandomForestRegressor / LinearRegression** – pour la comparaison des performances  
- **Google Colab** – pour l’exécution et la collaboration sur les notebooks  

---

## 📈 **Résultats principaux**

- Identification des variables ayant le plus d’impact sur la consommation énergétique.  
- Sélection d’un modèle final offrant un **bon compromis entre performance et interprétabilité**.  
- Création d’un pipeline complet et réplicable du nettoyage des données jusqu’à la prédiction.  
- Production de visualisations claires facilitant la communication des insights aux décideurs.

---

## 🚀 **Roadmap – Améliorations futures**

| Statut | Tâche | Description |
|:--:|:--|:--|
| 🟢 | **Version initiale du modèle** | Nettoyage, entraînement, sélection et interprétation du modèle final. |
| 🟡 | **Améliorer la robustesse du modèle** | Intégrer des méthodes d’optimisation plus avancées (Bayesian Optimization, AutoML). |
| 🟡 | **Mise en production simplifiée** | Créer une API Flask ou FastAPI pour exposer le modèle prédictif. |
| 🔵 | **Dashboard interactif** | Développer un tableau de bord Streamlit pour visualiser les prédictions en temps réel. |
| 🔵 | **Analyse temporelle** | Étudier l’évolution des consommations sur plusieurs années pour enrichir la prédiction. |
| 🔴 | **Documentation complète** | Rédiger une doc utilisateur et technique pour faciliter la réutilisation du projet. |

---

## 👨‍💻 **À propos**

Je suis actuellement **apprenant en formation d’Ingénierie en Intelligence Artificielle**.  
À travers ce projet, j’ai mis en pratique des compétences clés en **analyse de données, modélisation et interprétation de modèles de Machine Learning**, dans un contexte concret de **transition énergétique urbaine**.

> 💡 *Ce projet incarne ma capacité à transformer des données brutes en leviers d’action concrets au service du développement durable.*

---

## 📜 **Licence**

Ce projet est distribué sous licence **MIT** – vous êtes libre de le réutiliser, le modifier et le partager avec attribution.

---

**✍️ Auteur :** Raymond Francius    
📚 *Apprenant - Promotion 09-2025 :* **Engineering Intelligence Artificielle (AI)** — **Openclassrooms**   
📧 *Contact :* [raymond.francius@gmail.com]    
🔗 *GitHub :* [https://github.com/raym648/OpenClassRooms_Projets_AI_Engineer](https://github.com/raym648/OpenClassRooms_Projets_AI_Engineer)  

---
