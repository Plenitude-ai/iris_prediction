#!bin/bash
cd /mnt/c/Users/axeld/JUPYTER--TPs/github_projects/iris_prediction
docker run -p 80:5000 -v $(pwd):/app iris_prediction