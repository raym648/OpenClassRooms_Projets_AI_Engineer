# 📊 Mission - *Concevez une stratégie d’extraction de données multimodales pour entraîner un détecteur de fake news*

*Projet-12 --- Extraction de données multimodales (Texte + Image)*

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Airflow](https://img.shields.io/badge/Orchestration-Airflow-orange)
![ETL](https://img.shields.io/badge/Pipeline-ETL-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

------------------------------------------------------------------------

## 🎯 1. Contexte et Objectif  

Ce projet s'inscrit dans une problématique de détection de fake news portée par une entreprise spécialisée en intelligence artificielle. L'objectif consiste à concevoir un pipeline automatisé capable de collecter, traiter et structurer des données multimodales issues de sources web.  

-   🔍 Extraction de contenus (texte + images)
-   🌐 Sources multiples (API, scraping web)
-   🧠 Préparation des données pour un modèle IA

------------------------------------------------------------------------

## 🧩 2. Démarche Méthodologique  

Le projet suit une approche structurée de type pipeline data engineering, intégrant extraction, transformation et orchestration.  

-   📌 Identification des sources pertinentes
-   ⚙️ Automatisation de l'extraction
-   🔄 Transformation et normalisation des données
-   ⏱️ Orchestration avec Airflow

------------------------------------------------------------------------

## 🛠️ 3. Étapes de Réalisation  

### 3.1 Exploration et Qualification des Sources  

Analyse des sources disponibles afin de garantir la qualité et la diversité des données collectées. Cette phase permet d'évaluer la pertinence des contenus en fonction du cas d'usage.  

-   📊 Fiabilité des sources
-   📷 Disponibilité des images
-   📝 Richesse textuelle

------------------------------------------------------------------------

### 3.2 Développement des Scripts d'Extraction  

Mise en place de scripts automatisés pour récupérer les données depuis différentes plateformes. L'objectif est de garantir une collecte robuste et reproductible.  

-   🐍 Scripts Python
-   🌍 Scraping web / API
-   🔁 Automatisation des requêtes

------------------------------------------------------------------------

### 3.3 Pipeline de Transformation  

Transformation des données brutes en un format exploitable pour des modèles de machine learning. Cette étape inclut le nettoyage et la structuration des données.  

-   🧹 Nettoyage des données
-   🏷️ Structuration (JSON, CSV...)
-   🔗 Association texte-image

------------------------------------------------------------------------

### 3.4 Orchestration avec Airflow  

Automatisation complète du pipeline via un orchestrateur permettant la planification et le monitoring des tâches.  

-   ⏰ Planification des workflows
-   📈 Suivi des exécutions
-   ⚠️ Gestion des erreurs

------------------------------------------------------------------------

### 3.5 Évaluation et Visualisation  

Analyse des performances du pipeline afin d'identifier les axes d'amélioration et garantir la qualité des données produites.  

-   📊 Indicateurs de performance
-   📉 Visualisation des résultats
-   🧪 Tests de robustesse

------------------------------------------------------------------------

## 🎓 4. Objectifs Pédagogiques  

Ce projet permet de consolider des compétences clés en data engineering appliqué à l'IA.  

-   📦 Chargement et stockage de données
-   📏 Définition de KPI pertinents
-   🔄 Extraction multi-sources
-   🔧 Transformation de données

------------------------------------------------------------------------

## 🚀 5. Roadmap (Améliorations Futures)  

### 🔮 Évolutions prévues  

Améliorations envisagées pour renforcer la scalabilité et la performance du pipeline.  

-   ⚡ Intégration de streaming (Kafka)
-   ☁️ Déploiement cloud (AWS / GCP)
-   🤖 Ajout de classification automatique

------------------------------------------------------------------------

### ✅ TODO List  

Liste des tâches à implémenter ou améliorer à court terme.

-   [ ] Ajouter gestion avancée des erreurs
-   [ ] Optimiser les temps d'exécution
-   [ ] Enrichir les métadonnées
-   [ ] Ajouter tests unitaires
-   [ ] Mettre en place CI/CD

------------------------------------------------------------------------

## 📌 6. Conclusion  

Ce projet illustre la conception complète d'un pipeline de données multimodales dans un contexte industriel. Il met en évidence
l'importance de la qualité des données pour entraîner des modèles de détection de fake news.  

-   🧠 Approche orientée IA
-   🔄 Pipeline industrialisable
-   📊 Données exploitables

------------------------------------------------------------------------

## ✅ 7. Procédure d'installation et de configuration en locale (Ubuntu) d’Apache Airflow avec SQLite

Ce guide décrit **pas à pas** l’installation, la configuration et l’exécution locale d’un pipeline Airflow en utilisant SQLite (mode test), avec vos fichiers :

- `e04_etl_pipeline_v01.py`
- `e03_final_pipeline_dataset.csv`
- `e03_final_pipeline_dataset.jsonl`

---

### *1. Pré-requis système*

#### *1.1 Vérifier la version de Python*

```bash
python3 --version
```

✔️ Attendu : Python 3.8 à 3.11

---

#### *1.2 Installer les dépendances système*

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv sqlite3
```

##### *Vérification*

```bash
pip3 --version
sqlite3 --version
```

------------------------------------------------------------------------

### *2. Création d’un environnement virtuel*

```bash
python3 -m venv airflow_env
source airflow_env/bin/activate
```

#### *Vérification*

```bash
which python
```

------------------------------------------------------------------------

### *3. Installation d’Apache Airflow*

```bash
export AIRFLOW_VERSION=2.8.1
export PYTHON_VERSION=$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```

#### *Vérification*

```bash
airflow version
```

------------------------------------------------------------------------

### *4. Initialisation du projet*

```bash
export AIRFLOW_HOME=~/airflow
mkdir -p $AIRFLOW_HOME
airflow db init
```

#### *Vérification*

```bash
ls $AIRFLOW_HOME
```

------------------------------------------------------------------------

### *5. Création d’un utilisateur*

```bash
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin
```

------------------------------------------------------------------------

### *6. Intégration du DAG*

```bash
cp e04_etl_pipeline_v01.py $AIRFLOW_HOME/dags/
ls $AIRFLOW_HOME/dags/
```

------------------------------------------------------------------------

### *7. Ajout des données*

```bash
mkdir -p $AIRFLOW_HOME/data
cp e03_final_pipeline_dataset.csv $AIRFLOW_HOME/data/
cp e03_final_pipeline_dataset.jsonl $AIRFLOW_HOME/data/
ls $AIRFLOW_HOME/data/
```

------------------------------------------------------------------------

### *8. Lancement*

*Terminal 1 :*

```bash
airflow scheduler
```

*Terminal 2 :*

```bash
airflow webserver --port 8080
```

*Accès :*

http://localhost:8080

------------------------------------------------------------------------

### *9. Vérifications*

```bash
airflow dags list
airflow tasks list e04_etl_pipeline_v01
airflow dags test e04_etl_pipeline_v01 2024-01-01
```

------------------------------------------------------------------------

### *10. Logs*

```bash
cd $AIRFLOW_HOME/logs
```

------------------------------------------------------------------------

### *11. Structure finale*

```
~/airflow/
├── airflow.db
├── dags/
├── data/
├── logs/
```

------------------------------------------------------------------------

**Auteur :** *[Raymond Francius]*   
**Rôle :** *[Apprenant - Promotion Sept-2025]* — **Engineer AI** — **Openclassrooms**    
**Date de mise à jour :** *[30-03-2026]*   
**Client fictif :** **CheckItAI** conçoit des solutions d’intelligence artificielle pour lutter contre les fake news.    
**Projet :** Projet-12 - Extrayez des données multimodales de sites web 
