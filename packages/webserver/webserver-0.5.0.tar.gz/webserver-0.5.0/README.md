# Docker-Webserver (nginx:mainline-alpine)

**NB!** Big change is in progress, consider this an **alpha** product!

## What is it?

Simple to use CLI for setting up nginx webserver in Docker Swarm
and adding websites' configs, proxies and static files

----

## Technology Stack

* **Docker Swarm** for orchestration
* **click** for CLI scripts

----

## Features

* **Run Highly-Available *nginx:mainline-alpine* stack** with attachable **nginx** network (*to use with others containers*) and **nginx-static** & **nginx-conf** mount volumes (*for static files and configs*) -> `webserver run`
* **Update stack images *without downtime*** -> `webserver update`
* **Generate HTTPS config** for website with examples -> `webserver genconf`

ROADMAP (v1.0.0)
----
* **Get LetsEncrypt SSL certificate** for website *with one command and no configuration* (*except DNS A record*)
* **Generate DH params** for website
* **Add configuration file(s)** for website
* **Reload configs *without downtime***
* **Add/Update static files** for website
* **See stats** of running stack
* **Stop** the stack
* **Restart** the stack

ROADMAP (v1.x.x)
----
* **Analyze logs with GoAccess**

----

Made by Igor Nehoroshev (https://neigor.me) for his own needs (if You find it useful - great!😎)