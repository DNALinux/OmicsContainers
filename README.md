# Omics Containers

This is a curated collection of containers for bioinformatics, developed as part of the [DNALinux](https://dnalinux.com/) project. It is based on the [BioContainers project](https://github.com/BioContainers/containers). All containers are hosted at [Docker Hub](https://hub.docker.com/repositories/dnalinux).


## FAQ

#### Why another biocontainer project?

The original BioContainers project contains many containers that are over five years old, with outdated bioinformatics software and based on older Linux versions. The goal of Omics Containers is to provide up-to-date software whenever possible, both at the operating system level and for bioinformatics tools. Additionally, it aims to make the containers compatible with multiple architectures when available.

#### How do I use a container? 

You can use it from source and build a docker image. If you don't want to build the image yourself, you can pull it from [Docker Hub](https://hub.docker.com/repositories/dnalinux).
Once you have the image, you can run it to instanciate a container.

#### How do I build a docker image?

Go to the directory where the Dockerfile is, and run:

```
docker build -t name .
```

#### How do I pull a docker image?

Search for the docker image you want in [Docker Hub](https://hub.docker.com/repositories/dnalinux), select the version and run:

```
docker pull dnalinux/bwa
```

#### How do I run a docker image?

Each docker image has its own way to run it, see the **overview** section in DockerHub or the Dockerfile.

#### How do I request a new container?

Open an issue in this repo telling which program you need.

#### Who is behind Omics Containers?

Omics Containers is supported by [DNALinux](), [Toyoko](), and a dedicated bioinformatics community.

#### Is it free?

Yes, every file in this repository is un the [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0) license, unless noted (some files comes with their own license). If you run these container in a cloud provider, they may charge you for the computer time needed to run the containers. 

## Authors

- [Sebastian Bassi](https://www.github.com/sbassi)
- [Virginia Gonazalez](https://www.github.com/virmax)
- [Gretta Yagudayev](https://www.github.com/gyagu98)
- [Facundo Mercado](https://www.github.com/Facundo1224)

## License

[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)


## Feedback

If you have any feedback, please reach out to us at dnalinux@toyoko.io

