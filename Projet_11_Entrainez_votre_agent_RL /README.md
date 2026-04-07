# 🚀 Projet-11 — Entraînement d’un Agent en Apprentissage par Renforcement (RL)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![RL](https://img.shields.io/badge/Reinforcement-Learning-green.svg)
![Stable-Baselines3](https://img.shields.io/badge/Stable--Baselines3-RL-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📌 1. Contexte du projet

Ce projet s’inscrit dans une démarche de montée en compétence en **apprentissage par renforcement (Reinforcement Learning)**.  
Il vise à concevoir des agents capables de prendre des décisions optimales en interagissant avec un environnement dynamique.

- Apprentissage par interaction avec un environnement  
- Maximisation d’une récompense cumulative (reward)  
- Gestion d’environnements incertains et non déterministes  

---

## 🎯 2. Objectifs pédagogiques

Le projet permet de structurer une approche complète autour de la conception, l'entraînement et le déploiement d’agents intelligents.

- Construire des tableaux de bord interactifs pour visualiser les performances  
- Définir des flux de données et intégrer des APIs  
- Structurer et formater les données pour exploitation  
- Mettre en place des systèmes d’exposition des résultats (API / UI)  

---

## 🧠 3. Concepts clés abordés

Le projet couvre les fondamentaux du Reinforcement Learning :

- **État (State / Observation)** : représentation de l’environnement  
- **Action (Action Space)** : décisions possibles de l’agent  
- **Politique (Policy)** : stratégie de décision  
- **Fonction de valeur (Value Function)** : estimation des récompenses futures  
- **Modèle (Model-based vs Model-free)**  

---

## 🧪 4. Structure du projet

### 🔹 Exercice 1 — Découverte des bases du RL

Approche progressive visant à comprendre les mécanismes fondamentaux.  
L’accent est mis sur l’exploration et l’interaction simple avec l’environnement.

- Création et exploration d’un environnement  
- Implémentation d’une politique aléatoire  

---

### 🔹 Exercice 2 — Q-Learning avec Q-Table

Introduction à un algorithme classique d’apprentissage par renforcement.  
L’agent apprend à partir d’une table de valeurs mise à jour itérativement.

- Initialisation de l’environnement et de la Q-Table  
- Implémentation de la boucle d’apprentissage  
- Évaluation des performances de l’agent  

---

### 🔹 Exercice 3 — Deep Q-Network (DQN)

Transition vers une approche basée sur le Deep Learning.  
Remplacement de la Q-Table par un réseau de neurones pour gérer des espaces complexes.

- Définition du réseau de neurones  
- Mise en place du Replay Buffer  
- Entraînement avec Stable-Baselines3  

---

### 🌕 Mission — Pilotage de l’atterrisseur Eagle-1

Cas pratique avancé simulant un problème réel.  
Optimisation et déploiement d’un agent dans un environnement complexe.

- Exploration de l’environnement et baseline  
- Optimisation des hyperparamètres  
- Déploiement (API, interface graphique, dashboard)  

---

## ⚙️ 5. Technologies utilisées

- Python  
- Stable-Baselines3  
- OpenAI Gym / Gymnasium  
- NumPy / Pandas  
- Matplotlib / outils de visualisation  

---

## 📊 6. Cas d’usage

Les compétences développées sont directement applicables à plusieurs domaines :

- Robotique autonome  
- Véhicules autonomes  
- Jeux vidéo (agents intelligents)  
- Optimisation industrielle  

---

## 🔗 7. Liens & ressources du projet

### ⚙️ Exécution & Notebook Colab

Je fournis un **Notebook Colab** prêt à l’emploi.   

**Ouvrez directement le notebook dans Colab (aucune installation locale nécessaire) :**  
| ***Notebook01 mission pilotez atterrisseur lunaire eagle-1***  |[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/raym648/OpenClassRooms_Projets_AI_Engineer/blob/main/Projet_11_Entrainez_votre_agent_RL/2026-03-18_Notebook01_mission_pilotez_atterrisseur_lunaire_eagle-1.ipynb)|


## 🗺️ 8. Roadmap — Améliorations futures

### 🔧 Améliorations techniques

- Implémentation d’algorithmes avancés (PPO, A2C, SAC)  
- Optimisation automatique des hyperparamètres (Optuna)  
- Ajout de monitoring avancé (TensorBoard)  

### 📈 Expérimentations

- Tests sur environnements plus complexes  
- Benchmark de plusieurs algorithmes RL  
- Analyse comparative des performances  

### 🌐 Déploiement

- Création d’une API REST complète  
- Développement d’une interface utilisateur interactive  
- Intégration cloud (Docker / CI-CD)  

### ✅ TODO

- [ ] Ajouter documentation technique détaillée  
- [ ] Ajouter tests unitaires  
- [ ] Optimiser les temps d’entraînement  
- [ ] Ajouter des visualisations avancées  

---

## 📎 9. Conclusion

Ce projet constitue une base solide pour la compréhension et l’implémentation d’agents en apprentissage par renforcement.  
Il met en évidence la transition entre approches tabulaires et méthodes basées sur le Deep Learning.

- Acquisition de compétences en RL moderne  
- Capacité à concevoir des agents autonomes  
- Mise en production et valorisation des résultats  

---

**Auteur :** *[Raymond Francius]*   
**Rôle :** *[Apprenant - Promotion Sept-2025]* — **Engineer AI** — **Openclassrooms**    
**Date de mise à jour :** *[29-03-2026]*   
**Client fictif :** AstroDynamics "**leader dans le développement de systèmes autonomes pour l'exploration spatiale**"    
**Projet :** Projet-11 — Entraînement d’un Agent en Apprentissage par Renforcement (RL) 
