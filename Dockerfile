# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /src
COPY . .
# RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["python", "app/run.py"]
