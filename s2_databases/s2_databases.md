# Section 2: Databases

You are appointed by a car dealership to create their database infrastructure. There is only one store. In each business day, cars are being sold by a team of salespersons. Each transaction would contain information on the date and time of transaction, customer transacted with, and the car that was sold. 

The following are known:
- Each car can only be sold by one salesperson.
- There are multiple manufacturers’ cars sold.
- Each car has the following characteristics:
- Manufacturer
- Model name
- Serial number
- Weight
- Price

Each sale transaction contains the following information:
- Customer Name
- Customer Phone
- Salesperson
- Characteristics of car sold

Set up a PostgreSQL database using the base `docker` image [here](https://hub.docker.com/_/postgres) 
given the above. We expect at least a `Dockerfile` which will stand up your database with the DDL 
statements to create the necessary tables. Produce entity-relationship diagrams as necessary to 
illustrate your design.

Your team also needs you to query some information from the database that you have designed. 
You are tasked to write a `sql` statement for each of the following task:

1) I want to know the list of our customers and their spending.

2) I want to find out the top 3 car manufacturers that customers bought by sales (quantity) and 
the sales number for it in the current month.

# Obtaining the DockerFile

Download the dockerfile from:

> https://drive.google.com/file/d/1VV5JZ8-P2IA1DYBf_QL14ej7KZLZnXhT/view?usp=sharing

Unfortunately, the dockerfile was too big to push to git, so I uploaded it to drive due to lack of 
time.

The size is likely due to other installations in the docker image, and the size could be reduced by 
removing unused packages.

I've read online that something like https://github.com/jwilder/docker-squash might work to reduce 
the size, but I would need time to test this out.

# Running the DockerFile

Load up the dockerfile:

> docker import dockerfile

Find the docker container ID:

> docker ps

Run the docker container in bash (example container ID: c2caa90ed577):

> docker exec -it <container ID> bash

Run the queries:

1. I want to know the list of our customers and their spending.

> psql postgres postgres -f /opt/sql/query1.sql

Expected output:
>  name  | spending \
--------+----------\
 Tom    |   210000\
 Jill   |   130000\
 Daniel |   160000\
 Harry  |   220000\
(4 rows)

2. 2) I want to find out the top 3 car manufacturers that customers bought by sales 
(quantity) and the sales number for it in the current month.

query2.sql fetches for the month of 2022 Jan. This is done as the transactions are
fixed in dates, so the current month doesn't apply here.

query3.sql will fetch for the current month. But the transactions are not made for
this month, so nothing will be printed.

> psql postgres postgres -f /opt/sql/query2.sql

Expected output:

> manufacturer | sales_count | sales  \
--------------+-------------+--------\
 Subaru       |           2 | 230000\
 Audi         |           1 | 110000\
 Porsche      |           1 | 120000\
(3 rows)

Explanation: There are 3 cars sold from Lancia but are sold in another month, so
it does not appear here (for the month of 2022 Jan).

Alternatively, you can try to run this if you don't want to use the docker container:
> docker exec -it <container ID> psql postgres postgres -f /opt/sql/init.sql

Using sudo may be necessary (it is on my linux machine).

# Comments

The sql files used in the docker container are placed here too in \sql.
