# syntax=docker/dockerfile:1.7-labs
FROM python:3.10
WORKDIR /src
# RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple

# RUN mkdir docker_builder
# COPY docker_builder/alphafold_design/jaxlib-0.4.23+cuda11.cudnn86-cp310-cp310-manylinux2014_x86_64.whl ./docker_builder
# RUN pip install "jax[cuda11_pip]==0.4.23" -f docker_builder/alphafold_design/jaxlib-0.4.23+cuda11.cudnn86-cp310-cp310-manylinux2014_x86_64.whl

# COPY alphafold_design/requirements.txt .
# RUN pip install -r requirements.txt

COPY --exclude=docker_builder . .
CMD []
# ENTRYPOINT ["python", "app/run.py"]
