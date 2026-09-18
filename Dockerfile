from python:3.12-slim
WORKDIR/code
COPY requirements.txt.
Run pip install --no-cache-dir -r requirements.txt
COPY ./app./app
CMD ["uvicorn","app.main:app","--host","0.0.0.0","port","1000"]
