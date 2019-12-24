bhus
====

Irish for bus.
API to interact with Dublin's operators, vehicles and stops.


## Setup

### Dependencies

1. [docker-compose](https://docs.docker.com/compose/install/)
2. [PostgreSQL client](https://wiki.postgresql.org/wiki/PostgreSQL_Clients) - I recommend [pgcli](https://www.pgcli.com/install).
3. [wrk2](https://github.com/giltene/wrk2) - if you want to run the benchmarks.


### Starting the local environment

	./run.sh

This will start a docker-compose environment, pulling in the necessary base images and initializing your database and the service automatically.


### Connecting to the local database

The credentials to connect to the Postgres server are exposed in the `.env` file in the root of the repo.
To save some time, here's the raw connection URL you might want to use to connect to the database with `pgcli`.

	pgcli postgres://bhus:bhus@localhost/bhus

> Note: to connect via a port other than the default Postgres 5432 port edit the `.env` file and set the new port from there.
>       This is useful for when you already have a PG server running on your host machine and there's a port conflict.
> TODO: Make the above instruction Just Work by just using a different port.


### Running the benchmarks

First ensure the service is up and running

	./run.sh

Then simply run

	./benchmark.sh http://localhost:8000

> Note: This will likely changed, as well as the `wrk2` dependency removed, pending on doing benchmarks via [Gatling](https://gatling.io/docs/current/).

## Roadmap

1. make packages speak "spec" to each other and do serialization in a separate module, called at the view level.
1. build the service API.
2. benchmark via Gatling.
3. add API documentation.
   best if autogenerated, accessible via a webpage that the service provides.
   OpenAPI 3.0+, Swagger.
4. add documentation to launch the service if needed.
5. add mypy step for some type safety assurances.
