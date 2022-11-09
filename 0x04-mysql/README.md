# PROJECT: 0x04. MySQL
### AUTHOR: Matthew Allen

## TASKS:
### 0. Install MySQL
Install MySQL on both servers, 4925-web-01 and 4925-web-02.

### 1. Let us in!
Create a username and password for both MySQL databases which will allow the checker to access them.
* Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host name set to `localhost` and the password `projectcorrection280hbtn`.
* Ensure that `holberton_user` has permission to check the primary/replica status of the databases.

### 2. If only you could see what I've seen with your eyes
* Create a database named `tyrell_corp`.
* Within `tyrell_corp`, create a table named `nexus6` and add at least one entry to it.
* Ensure that `holberton_user` has `SELECT` permissions on the table.

### 3. Quite an experience to live in fear, isn't it?
On your primary MySQL server (`web-01`), create a new user for the replica server.
* The name of the new user should be `replica_user`, with the host name set to `%`.
* `replica_user` must have the appropriate permissions to replicate your primary MySQL server.
* `holberton_user` will need SELECT privileges on the `mysql.user` table in order to check that `replica_user` was created with the correct permissions.

### 4. Setup a Primary-Replica infrastructure using MySQL - `4-mysql_configuration_primary`, `4-mysql_configuration_replica`
* MySQL primary must be hosted on `web-01` - do not use the `bind-address`, just comment out this parameter.
* MySQL replica must be hosted on `web-02`.
* Setup replication for the MySQL database named `tyrell_corp`.
* Provide the MySQL primary configuration as answer file.
* Provide the MySQL replica configuration as answer file.

### 5. MySQL backup - `5-mysql_backup`
Bash script that generates a MySQL dump and creates a compressed archive out of it.
* Must contain all the MySQL databases
* Named `backup.sql`
* Has to be compressed to a `tar.gz` archive
* Must have following name format: `day-month-year.tar.gz`
* User to connect to the MySQL database must be `root`.
* Bash script accepts one argument that is the password used to connect to the MySQL database.
