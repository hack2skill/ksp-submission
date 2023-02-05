# Enolahomes
Enolahomes is an extensive suite built on top of the Django Python framework with scheduled multithreaded submodules like spiders, web crawler with sock proxy, OSINT modules for scraping information like social media account and other publicly available data including darkweb. This tool has an intelligent dashboard to monitor job queue and case investigate report portal.

## Installation

### Docker Setup
Installation is required, Please do follow the guide [docker-install](https://github.com/docker/docker-install). Also Make sure install docker-compose if not follow this [docker-compose](https://docs.docker.com/compose/install/).

```bash
$ docker-compose up -d
```

### Virtual Environment
It is recommended to use a virtual environment to install the dependencies. This can be done by running the following commands:

1. Linux/MacOS:
    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
2. Windows:
    ```ps1
    > python -m venv venv
    > venv\Scripts\activate
    ```

### Dependencies
The dependencies can be installed by running the following command:

```bash
$ pip install -r requirements.txt

$ python manage.py makemigrations
$ python manage.py migrate
```

## Running the program
The program can be run by running the following command:

```bash
$ python manage.py runserver 0.0.0.0:8000
```
visit [http://localhost:8000/](http://localhost:8000/)
