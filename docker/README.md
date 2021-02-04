### Docker cheatsheet
Docker is a container that makes it easy to run and distribute applications across different operating environments. A container image is a package format that includes your application and all dependencies and runtime information required to run it. A docker is used to create, distribute, and run container images on your own server. 

#### Useful Commands
* install docker:
`sudo apt-get install docker.io`
* list docker images:
`sudo docker images`
* download an image from a repository: 
`sudo docker pull nginx:1.10.0`
* run an image:
`sudo docker run -d nginx:1.10.0`
* check whether the image is running:
`sudo docker ps`
* find out more information about a specific container:
`sudo docker inspect container_id`
* hit the instance running inside a container: 
`curl IPAddress`
* stop docker instances:
`sudo docker stop container_id`
* remove the docker container from the system and any file they might leave behind:
`sudo docker rm container_id`
* remove all docker containers from the system:
`sudo docker rm ^C`
* print all the images: `docker image ls`
* remove a docker image: `docker rmi -f f3445sf4fsf245` (f34... is the image id)

#### Creating your own images --- Dockerfile( a txt file that contains step-by-step instructions for creating Docker images) 
* example Dockerfile:
```
FROM alpine: 3.1 # base image to build on top of
MAINTAINER Kelsey Hightower
ADD hello /usr/bin/hello
ENTRYPOINT ["hello"]
```



