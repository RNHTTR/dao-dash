# dao-dash
## TODOs
* Use cron to automatically refresh on some cadence that the user can set
    * eventually create some kind of interface for manual database refresh
* Dockerize deployment
    * Hijack superset's docker-compose.yml?
    * test in a few systems
        * Localhost
        * Some cloud(s)
## Setup
> TODO: Eventually this should just all be done in a docker container

### Pre-Requisites
* Install Docker, Docker Compose, Python 3.9+ (pyenv), SQLAlchemy
### Postgres
> NOTE: Changed port from default 5432 to 5433 because the docker compose yaml for superset has a database deployed to 5432. This change probably isn't necessary -- I was trying to connect to localhost from Docker. Updating the connection string to use `host.docker.internal` instead of `localhost` fixed the connection issue.
### Superset
```bash
git clone https://github.com/apache/superset.git && cd superset
docker-compose -f docker-compose-non-dev.yml up
```

Navigate to localhost:8088
> TODO: Organize the following, update with user/pw created from postgres step

Data -> Databases -> + Database -> PostgreSQL -> Connect this database with a SQLAlchemy URI string instead -> postgresql+psycopg2://user:password@host.docker.internal:5433/dao-dashboard 

### Covalent
Get API key