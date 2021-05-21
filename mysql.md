#### MySQL commands learnt during Ques10 Internship [resource](https://www.mysqltutorial.org/)
Command | Use | Extras
|----|----|----|
mysql -u username -p | log in to server | every user has different level of access, root user, user1, user2 etc
use database_name | database to use |
show tables | all the tables present in the database |
desc table_name | short description about the table named |
select * from table_name | full table  |
select coulmn1, coulmn2 from tables_name | table with selected coulmns |
truncate table_name | clear all data from table |

#### MySQL commands [resource](https://www.mysqltutorial.org/)
Command | Use | Extras
|----|----|----|
SHOW DATABASES | To display databases in the current server |
source file.sql | To load database (sample) to current server | 
SELECT coulmn_names FROM table_name | output is called result set | from -> select
SELECT * FROM table_name | often called select star or select all | 
SELECT * FROM table_name ORDER BY coulmn1 ASC, coulmn2 DESC | To sort the queried data, we add a *ORDER BY* clause to the select statement , It's ascending by default, | from -> select -> order by

#### Extras 
* A Database is merely a structured collection of data.
* The data relating to each other by nature, e.g., a product belonged to a product category and associated with multiple tags. Therefore, we use the term relational database.
* Database has multiple tables, relating to one another using relationships like : one to one  , many to one 
* SQL is the standardized language used to access the database.
* SQL contains three parts:
    * Data definition language includes statements that help you define the database and its objects, e.g., tables, views, triggers, stored procedures, etc.
    * Data manipulation language contains statements that allow you to update and query data.
    * Data control language allows you to grant the permissions to a user to access specific data in the database.
* MySQL is a database management system that allows you to manage relational databases. 
