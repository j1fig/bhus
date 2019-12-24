"""
The models package offers persistence logic encapsulation.

As much as possible, each datastore's methods will be "dumb pipes"
and any domain-specific logic should be kept well out of this package.


For now only a PostgreSQL client library is provided, but benchmarking may unveil
that other datatores may need to come in to complement or replace PG.
"""
