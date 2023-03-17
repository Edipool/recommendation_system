## What is this project about

Hello, world!

This project implements a recommendation system based on classical machine learning.

In the file `app.py` contains the logic of the microservice operation based on the recommendation of messages.

In the `get_model.py` contains the logic of loading the `catboost_model` file with the prediction of the CatBoostClassifier model.

In the file `load_table.py` contains logic for loading a table with already processed objects.

In the `schema.py` file contains the logic of a scheme based on pydantic.

In the Experiments_with_the_recommendation system.app file, you can view all the logic of data processing and experiments with various models.

The best metric is `hitrate@5` for the `CatBoot` model and it is 0.450.

This solution does not process the text of posts (TF-IDF). The text of the posts will be processed in the following solution with the use of deep learning methods.

## Main libraries used
![Pyhon](https://img.shields.io/badge/-Python_3.10.6-090909?style=for-the-badge&logo=python) ![Fastapi](https://img.shields.io/badge/-Fastapi_v0.75.1-090909?style=for-the-badge&logo=Fastapi) ![Catboost](https://img.shields.io/badge/-Catboost_v1.0.6-090909?style=for-the-badge&logo=Catboost) ![Scikit_learn](https://img.shields.io/badge/-Scikit_learn_v1.1.1-090909?style=for-the-badge&logo=Scikit_learn) ![Pandas](https://img.shields.io/badge/-pandas_v1.4.2-090909?style=for-the-badge&logo=pandas) ![Numpy](https://img.shields.io/badge/-Numpy-090909?style=for-the-badge&logo=Numpy) ![Xgboost](https://img.shields.io/badge/-Xgboost_v1.6.1-090909?style=for-the-badge&logo=xgboost) ![Pydantic](https://img.shields.io/badge/-pydantic_v1.9.1-090909?style=for-the-badge&logo=pydantic) ![mlflow](https://img.shields.io/badge/-mlflow_v1.19.0-090909?style=for-the-badge&logo=mlflow)

## Running the code

For obvious reasons, I can't upload the `.env` file and grant access to the database. A docker container will be implemented soon, where you can run the code.

Thank you for your attention!
