In this document we present the rationale for the design and architectural choices made.


## Approach

Focus on fast feedback loops.

Go with what you know first.

Benchmark and evolve if not meeting the requirements.

In the local environment we might be able to accurately ballpark the per k8s pod performance.

## Data store

### Requirements

* Loading a large static dataset into the datastore efficiently.
* The dataset itself is a timeseries.
* Read-only - no write requirements (for now).
* Provide high read throughput - think large number of simultaneous connections.
* Provide querying abilities such as
   * determining uniqueness of a given field.
   * ordering by a given field.
* No full text search abilities required (for now).
* Primary filtering will mostly be done by timestamp.

> Uncompressed, the raw CSV data for a year's worth of Dublin bus GPS data could be in the order of 60 Gb.

### PostgreSQL

Having seen PostgreSQL perform quite admirably, given the correct indexing (and `EXPLAIN ANALYZE` iterations) is setup, this was the first choice to benchmark through.

Seeing as basically we're using PostgreSQL as a read oriented time series database, we'll next look at


### TimescaleDB


### ElasticSearch


### MongoDB


## Application

### Requirements and considerations

1. I/O bound service - the data will require little massaging on the application layer in order to be served to clients.

### asyncio-based Python


## Production and deployment

The local setup tries to simplify the production environment and strike a compromise between parity and development speed.
The production setup will come under extra considerations and bottlenecks.


### Load balancing


