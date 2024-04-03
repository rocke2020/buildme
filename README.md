# Build with Docker

This repository contains an example Go application, used in the
[Build with Docker guide](https://docs.docker.com/build/guide).

This goal of this guide is to illustrate Docker Build features and best
practices.


## Python
### quick start
```
# first run
sudo docker run hello-world

docker build --tag hello-py .
docker run -d -v /mnt/nas1/dong-qichang/tmp:/src/output hello-py
docker run -d --rm -v /mnt/nas1/dong-qichang/tmp:/src/output -v /home/qcdong/codes/peptide-deploy/alphafold_design/args:/src/app/args hello-py python app/run.py --args_file app/args/PRL.yml

# debug
docker run -it --rm -v /mnt/nas1/dong-qichang/tmp:/src/output hello-py /bin/bash

# check gpu
docker run --gpus all --rm nvidia/cuda:11.8.0-base-ubi8 nvidia-smi
# debug
docker run -it --rm pytorch/pytorch:2.2.0-cuda11.8-cudnn8-devel /bin/bash
```
