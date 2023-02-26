# The Luggage

The Luggage is a secure file-sharing web application built with [Django](https://www.djangoproject.com/) and
[tus](https://tus.io/) protocol. The project is named after the magical trunk in Terry Pratchett's Discworld series,
which is known for being fiercely protective of its owner and capable of carrying just about anything.

Inspired by the concept of The Luggage, this application aims to provide a reliable and secure way to share files with
your friends over the internet. It provides an easy-to-use interface for both uploading and downloading files and
allows you to set expiration dates and passwords to protect your files.

## Features

### Processes

- Uploading files: Authorized users can upload files to The Luggage.
- Sharing files: Authorized users can send a link to anybody to share files. They can also set a password to protect
the file and ensure only the intended recipient can access it.
- Receiving files: Authorized users can create an invitation link and send it to the person from whom they want to
receive a file. Once the person uploads the file, the authorized user can download it.

### Properties

- File expiration: Files uploaded to The Luggage can be set to expire after a certain amount of time or a certain number
of downloads to ensure they are not available indefinitely. This helps to keep the platform secure and prevents the
misuse of shared files.
- Access control: Only authorized users can upload and receive files on The Luggage. If you are not an authorized user,
you need an invitation from an authorized user to upload or receive files. Invitations to upload are one-time use to
prevent misuse of the platform and ensure the security of shared files.

The Luggage is designed to be a secure and user-friendly file-sharing platform that provides the necessary features
for sharing files securely and conveniently.

## Install

Application use these environments variables:

| Variable                 | Description                    | Default                        | Example                       |
|--------------------------|--------------------------------|--------------------------------|-------------------------------|
| `BASE_URL`               | Base URL of the application    | -                              | `https://luggage.example.com` |
| `ALLOWED_HOSTS`          | Allowed hosts (Django Setting) | -                              | `luggage.example.com`         |
| `DATABASE_HOST`          | Database server location       | -                              | `docker.for.mac.localhost`    |
| `DATABASE_NAME`          | Database name                  | -                              | `tester`                      |
| `DATABASE_PASSWORD`      | Database user password         | `super-secure-password`        |                               |
| `DATABASE_PORT`          | Database port                  | `5432`                         | `5432`                        |
| `DATABASE_USER`          | Database user                  | -                              | `luggage`                     |
| `DJANGO_SETTINGS_MODULE` | Django Settings Module         | `luggage.settings.development` | `luggage.settings.production` |
| `SECRET_KEY`             | Django secret                  | -                              | `ghp_asdqwjdsncvsdv`          |

### Docker

Pre-build Docker image is available on GitHub Container registry as ghcr.io/sibyx/the-luggage:master

To run the image as a container you can use command bellow (keep in mind that you have to specify the environment
variables accordingly). The logs from container are present in the `/var/log` so you have to create a volume to access
them (present in the example).

The container requires access to the Docker environment that's why you have to create volume, which maps a path to the
Docker socket.

```shell
docker run -p 9000:9000 -v ./logs:/var/log/ --env BASE_URL= --env ALLOWED_HOSTS= --env DATABASE_HOST= --env DATABASE_NAME= --env DATABASE_PASSWORD= --env DATABASE_PORT= --env DATABASE_USER= --env DJANGO_SETTINGS_MODULE=luggage.settings.production --env SECRET_KEY= --name the-luggage  --add-host=host.docker.internal:host-gateway ghcr.io/sibyx/the-luggage:master
```

Server started on port 9000.

### From source

We use [poetry](https://python-poetry.org/) for dependency management and [PostgreSQL](https://www.postgresql.org/) 15
(10+ should be compatible) as a data storage (acquisition files are stored on the filesystem, not in the database).
To set up instance with demo database follow these simple steps:

1. Create python virtual environment (`python -m venv venv`)
2. Enter environment (`source venv/bin/activate`)
3. Install dependencies `poetry install`
4. Create `.env` file according `.env.example`
5. Execute migrations `python manage.py migrate`
6. Create superuser using `python manage.py createsuperuser` or setup LDAP in `auth_sources` table

---
Made with ❤️ and ☕️ Jakub Dubec (c) 2023
