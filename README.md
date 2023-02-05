# ksp-submission
This repository is created for Karnataka State Police Hackathon 2023 - submission collection. 
## Team Information

### Team Name - Datazip

### Problem Statement - Unified Data Verification

### Inspiration

Datazip started out as a end-to-end no-code data unification and analytics product. This problem was already existing in the current world, we wanted to take it head on and work on a solution which would be suitable for the police department too along with serving the main purpose of data unification and its verification.

### Contents

- [Frontend Application](./Frontend)
- [Machine Learning Service](./MLS)


### What it does

1. Datazip has ingestion tool which supports more than 150 data sources which includes all the popular databases like MySQL, PostgreSQL, MongoDB, files like .csv, .parquet, and more.

2. We injest the data into centralized data warehouse or a search engine

3. We have also created a feature for running face and fingerprint recognition.

4. We are combining all the results from the above steps therefore unifying the results from various data sources and help the Police Department access it from one place.

5. We calculate features on the datasets from the databases by running the FacialRecogDataPreparation.py file. This outputs .csv and .npy files which are used in FingerDataPreparation.py file.

### Tech Stack

1. Microsoft Azure
2. ImageNet
3. Azure ML Notebooks
4. Azure App Services - For Deploying the Frontend
5. ReactJS - UI Library
6. Node/NPM
7. MaterialUI - UI Components
8. JavaScript - Frontend
9. Firebase - Authentication
10. Python - Backend
11. Airbyte
12. ElasticSearch - To Power the Search

### What's next for Datazip

1. We would want to offer a full fledged lake house architecture with natural extension for machine learning use cases.
2. We would also add easier data transformations
3. We would also want to make the whole product end to end auto-scalable

<br />



<img src="./Datazip.png" width="450" height="250" alt="Architecture"/>


