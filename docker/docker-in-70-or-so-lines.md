# Docker in 70 or so lines

## What is docker?

> Docker containers are like VMs but faster!

A tool that can package software into containers that can run reliably in any environment!

## What is a Container?

Let's say you built an app with COBOL that runs on some weird flavour of linux. You want to share 
this app with your friend but he has an entirely different system, so the problem becomes, how do we
replicate the environment ourselves our software needs, on any machine?

One way to package this app is to use a Virtual Machine (VM), where the hardware is simulated, then 
installed with the required os and dependencies. 

This allows us to run multiple apps on the same infrastructure. However, since each VM is running is
running iits own OS, they tend to be bulky and slow!

Now, a docker container is conceptually very similar to a VM with one key difference. Instead of 
virtualizing hardware, containers only virtualize the OS, or in other words, all apps or containers 
are run a single kernel. And this makes almost everything BLAZINGLY faster and more efficient!

## Fundamentals to know

There are three fundamental things to know about Docker: 
- Dockerfile
- Image
- Container

The Dockerfile is like DNA, it's just code tells docker how to build an image, which itself is a 
snapshot of your software along with all of its dependencies down to the OS level. 

Each Image is immutable, and it can be used to spin up multiple containers, which is your actual 
software running in the real world. Layer-wise caching done to get the image built faster!

## Basic code
We can use FROM syntax to download from an existing template like ubuntu. The base image gets pulled down from the cloud.
You can also  upload your own images to a variety of docker registries (like [docker hub](https://hub.docker.com/)).
```docker
FROM ubuntu:20.04
```
Use RUN command to run simple terminal commands that installs dependencies into your image
```docker
RUN apt-get install sl 
```
You can set environment variables and do all kinds of other stuff
```docker
ENV PORT=8080
```
You can also execute a default command, that executes when you start up the container
```docker
CMD ["echo", "Docker is easy 🐳"] 
```

Now, after this, we can build our own image, using

```shell
docker build -t myapp path/todirectory/of/dockerfile
```
> `-t` is name tag used to name the docker image

We can bring this image to life as a container by running 
```shell
docker run myapp
```

> `-v` tag to mount volume