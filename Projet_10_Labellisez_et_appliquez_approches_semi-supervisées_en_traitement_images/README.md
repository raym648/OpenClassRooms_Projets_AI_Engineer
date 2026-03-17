# 🧠 BrainScanAI --- Détection de tumeurs cérébrales par apprentissage semi‑supervisé

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Computer
Vision](https://img.shields.io/badge/Computer%20Vision-Deep%20Learning-green)
![Framework](https://img.shields.io/badge/Framework-PyTorch%20%7C%20TensorFlow-orange)
![Status](https://img.shields.io/badge/Project-Research%20Prototype-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Contexte du projet

Ce projet s'inscrit dans le cadre d'une mission d'exploration et de modélisation menée au sein de **Curelytics IA**, une startup spécialisée dans les solutions d'intelligence artificielle appliquées à la **e‑santé**.  

L'objectif est d'explorer l'utilisation de techniques de **Computer Vision** et **d'apprentissage semi‑supervisé** afin d'assister les radiologues dans la **détection automatisée de tumeurs cérébrales à partir d'IRM**.  

Le défi principal du projet repose sur la **faible disponibilité de données annotées** :  

-   un **grand volume d'images non étiquetées**  
-   un **petit sous‑ensemble annoté par des experts médicaux**  

L'approche consiste donc à exploiter ces labels partiels afin d'améliorer la qualité de la classification.  

------------------------------------------------------------------------

# 🎯 Objectifs du projet  

Les objectifs techniques sont les suivants :  

-   Explorer un jeu de données d'IRM cérébrales  
-   Extraire des **features visuelles** à l'aide d'un modèle **pré‑entraîné**  
-   Identifier des **structures naturelles dans les données**  
-   Implémenter une approche **semi‑supervisée**  
-   Évaluer les performances à l'aide de **métriques adaptées**  
-   Produire des **recommandations techniques pour un passage à l'échelle**  

------------------------------------------------------------------------

# 🧪 Données  

Le dataset fourni contient :  

-   Des **radiographies cérébrales (PNG)**  
-   Des **métadonnées anonymisées**  
-   Un **sous‑ensemble d'images annotées** :  
    -   `Normal`  
    -   `Cancéreux`  

La majorité des images **ne possède pas de label**, ce qui rend nécessaire l'utilisation de méthodes semi‑supervisées.  

------------------------------------------------------------------------

# ⚙️ Pipeline du projet  

Le projet suit une démarche progressive combinant **apprentissage non supervisé** et **semi‑supervisé**.  

## 1️⃣ Import et exploration des données  

-   Chargement des images  
-   Analyse exploratoire du dataset  
-   Visualisation d'échantillons  
-   Vérification de la qualité des données  

------------------------------------------------------------------------

## 2️⃣ Prétraitement et extraction des features  

Les images sont normalisées et redimensionnées avant extraction des caractéristiques.  

Méthodologie :  
-   Redimensionnement des images  
-   Normalisation  
-   Extraction des embeddings avec **ResNet pré‑entraîné**  
-   Génération d'un vecteur de features par image  

Objectif : transformer les images en **représentations vectorielles exploitables par les algorithmes de clustering**.  

------------------------------------------------------------------------

## 3️⃣ Analyse non supervisée  

Une analyse exploratoire est réalisée afin d'identifier la structure des données.  

Techniques utilisées :  
-   **PCA** (réduction de dimension)  
-   **t‑SNE** (visualisation)  
-   **K‑Means**  
-   **DBSCAN**  

Objectifs :  
-   Identifier des regroupements naturels  
-   Détecter d'éventuels patterns dans les images  

------------------------------------------------------------------------

## 4️⃣ Apprentissage semi‑supervisé  

Une approche semi‑supervisée permet d'exploiter les **labels partiels** disponibles.  

Stratégie :  
-   utilisation des embeddings extraits  
-   propagation des labels  
-   entraînement d'un **MLP classifier**  

Cette méthode permet de **prédire les labels manquants** pour les images non annotées.  

------------------------------------------------------------------------

# 📊 Métriques d'évaluation  

Les performances du modèle sont évaluées avec :  
-   **Accuracy**  
-   **Precision**  
-   **Recall**  
-   **F1‑Score**  

Dans le contexte médical, une attention particulière est portée au :  

**Recall (sensibilité)** afin de limiter les **faux négatifs**, critiques dans la détection de tumeurs.  

------------------------------------------------------------------------

## 🔗 Liens & ressources du projet

### ⚙️ Exécution & Notebook Colab

Je fournis un **Notebook Colab** prêt à l’emploi.   

**Ouvrez directement le notebook dans Colab (aucune installation locale nécessaire) :**  
- ***Notebook01 Analysez images médicales avec méthodes semi-supervisées*** 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raym648/OpenClassRooms_Projets_AI_Engineer/blob/main/Projet_10_Labellisez_et_appliquez_approches_semi-supervisées_en_traitement_images/2026-02-24_Notebook01_Analysez_images_médicales_avec_méthodes_semi_supervisées.ipynb)

------------------------------------------------------------------------

# 🚀 Passage à l'échelle  

Objectif cible :  
**4 millions d'images à labelliser** avec un budget de **5000 €**.  

Recommandations techniques :  
-   Extraction des embeddings via **GPU cloud**  
-   Stockage optimisé (formats compressés)  
-   Clustering distribué  
-   Utilisation de **pseudo‑labelling**  
-   Pipeline de traitement **batch + parallélisation**  

Conditions de faisabilité :  
-   Infrastructure GPU  
-   Pipeline automatisé  
-   gestion efficace des embeddings  

------------------------------------------------------------------------

# 📈 Résultats attendus  

Le projet vise à démontrer que :  
-   les **features extraites par un modèle pré‑entraîné** capturent correctement l'information médicale  
-   le **clustering permet de structurer les données**  
-   les **méthodes semi‑supervisées améliorent les performances malgré peu de labels**  

------------------------------------------------------------------------

# 🧭 Roadmap  

## 🔧 Améliorations futures  
-   Fine‑tuning du modèle CNN  
-   Test de modèles plus récents (EfficientNet, Vision Transformers)  
-   Intégration d'AutoML  
-   Amélioration du pipeline de pseudo‑labellisation  

## 📋 TODO  

-   [ ] Optimisation du preprocessing  
-   [ ] Benchmark de plusieurs architectures CNN  
-   [ ] Ajout de validation croisée  
-   [ ] Ajout d'un pipeline ML reproductible  
-   [ ] Déploiement d'un prototype d'API  
-   [ ] Visualisation interactive des clusters  

------------------------------------------------------------------------

**Auteur :** *[Raymond Francius]*   
**Rôle :** *[Apprenant - Promotion Sept-2025]* — **Engineer AI** — **Openclassrooms**    
**Date de mise à jour :** *[17-03-2026]*   
**Client fictif :** Curelytics IA "**spécialisé en Computer Vision**"    
**Projet :** Projet-10 - Labellisez et appliquez des approches semi-supervisées en traitement d'images  
