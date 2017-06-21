CREATE USER infoelecciones WITH PASSWORD 'foobar';
CREATE DATABASE infoelectoral WITH OWNER infoelecciones;
GRANT ALL PRIVILEGES ON DATABASE infoelectoral TO infoelecciones;
ALTER USER username WITH SUPERUSER;

-- And once you are done issuing COPY commands...
ALTER USER username WITH NOSUPERUSER;
