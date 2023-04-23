# ECE568 Final Project - Amazon

## Authors: Oliver Chen (yc557), Yifan Jiang (yj193) 

## Notes to create local postgres database
```bash
sudo service postgresql start
psql
CREATE user yc557;
ALTER USER yc557 WITH PASSWORD 'Oliver666';
CREATE DATABASE "projectDB";
GRANT ALL PRIVILEGES ON DATABASE "projectDB" TO yc557;
```
Quit postgresql, then connect to the db as the corresponding user
```bash
psql -d projectDB -U yc557
\dt
```
To stop postgres,
```bash
sudo service postgresql stop
```