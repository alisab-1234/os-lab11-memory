FROM python:3.12-slim 
WORKDIR /app 
COPY src/ ./src/ 
CMD ["python", "src/memory_lab.py"]
