FROM python:3.11-slim
WORKDIR /app
COPY ../requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY api_server.py ./
CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8080"]
