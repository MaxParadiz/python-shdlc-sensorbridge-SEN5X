One way of logging data is to store the data into a postgresql database. 


(1) Install postgresql 

```
sudo pacman -S postgresql
```

(2) Enable the postgresql service 

```
sudo systemctl enable postgresql
```

(3) Start the postgresql service 

```
sudo systemctl start postgresql
```


(4) Log into the postgres database 

```
psql -U postgres
```

From within the postgresql console, execute the following:

We create a postgresql user to manage our sensor database:
```
CREATE ROLE sensors WITH LOGIN PASSWORD 'your_password';

CREATE DATABASE sensors;

ALTER DATABASE sensors OWNER TO sensors;

GRANT ALL PRIVILEGES ON DATABASE sensors TO sensors;
```
Connect to the database
```
\c sensors
```
We now need to create a table in which to store the data. 

```
CREATE TABLE sen55 (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
    temperature DECIMAL(6, 3), 
    humidity DECIMAL(5, 2),      
	pm1 DECIMAL(5, 1),   
    pm2_5 DECIMAL(5, 1),  
    pm4 DECIMAL(5, 1),  
    pm10 DECIMAL(5, 1),  
    voc DECIMAL(5, 1),  
    nox DECIMAL(5, 1)
);
```


You may now type "quit" to exit the database.

This database will be used to hold our sensor's measurements.

------

psycopg2
