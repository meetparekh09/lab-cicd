# Lab Docker

This repository contains a sample source code for creating a sample flask server that prints out "Hello World". Also, corresponding libraries or packages required to run this flask server are provided in requirements.txt file which can be installed with command `pip install -r requirements.txt`

Your assignment for Docker is to create a docker image with these libraries setup and then run this app within a docker container and call it via web browser to see "hello world" output

# Solution

Your solution may vary from what we have done. In this solution we have created a `Dockerfile` which copies file from application directory to docker and then runs `pip install -r requirements.txt` to install dependencies.

And then in the next step to run the application we have created a `run` command in makefile which executes the following command. `docker run -dp 5000:5000 -v ${PWD}:/lab-docker flask-basic python hello.py`

So, to see the output, one can:
1. execute `$docker build -t flask-basic .`
2. execute `$make run`
3. go to web browser and hit localhost:5000 to see the output