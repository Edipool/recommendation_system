FROM python:3.9.12

WORKDIR /recommendation_system

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY datasets /recommendation_system/datasets
COPY models /recommendation_system/models
COPY src /recommendation_system/src

WORKDIR /recommendation_system/src

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

