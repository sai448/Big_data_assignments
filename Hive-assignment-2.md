Scenario Based questions:

### Will the reducer work or not if you use “Limit 1” in any HiveQL query?
```
 Yes reducer will worK
 ```
### Suppose I have installed Apache Hive on top of my Hadoop cluster using default metastore configuration. Then, what will happen if we have multiple clients trying to access Hive at the same time? 
```
 Hive default metastore cant handle multiple requests at the same time.
 ```
### Suppose, I create a table that contains details of all the transactions done by the customers: CREATE TABLE transaction_details (cust_id INT, amount FLOAT, month STRING, country STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ‘,’ ;
Now, after inserting 50,000 records in this table, I want to know the total revenue generated for each month. But, Hive is taking too much time in processing this query. How will you solve this problem and list the steps that I will be taking in order to do so?
```
1.Create a table with the data and partioned with month column
2.Insert overwrite table_name partition(Col_name) select cust_id,amount,month,country from  customers
Hive engine will create partitiones for month based on unique values in month column.
```
### How can you add a new partition for the month December in the above partitioned table?
```
we can either use static partition or dynamic partition.
```
### I am inserting data into a table based on partitions dynamically. But, I received an error – FAILED ERROR IN SEMANTIC ANALYSIS: Dynamic partition strict mode requires at least one static partition column. How will you remove this error?
```
we need to set the property to nonstrict
in strict mode hive will prevent the full table scan, inorder to do full table scan in dynamic partition we need to set it to non strict
```

Suppose, I have a CSV file – ‘sample.csv’ present in ‘/temp’ directory with the following entries:
id first_name last_name email gender ip_address
How will you consume this CSV file into the Hive warehouse using built-in SerDe?


### Suppose, I have a lot of small CSV files present in the input directory in HDFS and I want to create a single Hive table corresponding to these files. The data in these files are in the format: {id, name, e-mail, country}. Now, as we know, Hadoop performance degrades when we use lots of small files.
So, how will you solve this problem where we want to create a single Hive table for lots of small files without degrading the performance of the system?
```
Create external table and point to that directory

syntax:
Create  external table if not exists(
id int,
name string,
email varchar(30),
country string)
row format delimited
fields terminated by ','
location hdfs directory
```


### LOAD DATA LOCAL INPATH ‘Home/country/state/’
OVERWRITE INTO TABLE address;

The following statement failed to execute. What can be the cause?
```
LOCAL PATH IS INCORRECT WE SHOULD GIVE FILE://
```

Is it possible to add 100 nodes when we already have 100 nodes in Hive? If yes, how?















Hive Practical questions:

Hive Join operations

Create a  table named CUSTOMERS(ID | NAME | AGE | ADDRESS   | SALARY)
Create a Second  table ORDER(OID | DATE | CUSTOMER_ID | AMOUNT
)

Now perform different joins operations on top of these tables
(Inner JOIN, LEFT OUTER JOIN ,RIGHT OUTER JOIN ,FULL OUTER JOIN)

BUILD A DATA PIPELINE WITH HIVE

Download a data from the given location - 
https://archive.ics.uci.edu/ml/machine-learning-databases/00360/

1. Create a hive table as per given schema in your dataset 
```
create table if not exists airquality(
 date1 string,
 Time1 string,
 CO Float,
 po smallint,
 nmhc smallint,
 c6h6 float,
 pt08 smallint,
 nox smallint,
 pt08s3 smallint,
 no2 smallint,
 pt08s4 smallint,
 pt08s5 smallint,
 t float,
 rh float,
 ah double)
 row format delimited
 fields terminated by ';'
 TBLPROPERTIES ("skip.header.line.count"="1");
```
2. try to place a data into table location
```
load data local inpath 'file:///config/workspace/AirQualityUCI.csv' into table airquality;

```
3. Perform a select operation . 
```
select * from airquality ;
```
4. Fetch the result of the select operation in your local as a csv file . 
```
insert overwrite local directory '/config/workspace/test.csv' select * from airquality limit 10;
```
5. Perform group by operation . 
```
select date1,avg(co) from airquality group by date1;
```
6. Perform filter operation at least 5 kinds of filter examples . 
```
select * from(select  to_date(from_unixtime(UNIX_TIMESTAMP(date1,'dd/mm/yyyy'))) as date3 from airquality) as innertable where date3 between '2004-01-10'and '2004-02-10';
 select * from(select  to_date(from_unixtime(UNIX_TIMESTAMP(date1,'dd/mm/yyyy'))) as date3 from airquality) as innertable where date3 '2004-02-10';
 ```
7. show and example of regex operation

8. alter table operation 
```
alter table airquality rename to airquality1;
```
9 . drop table operation
```
drop table airquality;
```
10 . order by operation . 
```
select * from airquality orderby po;
```
11. where clause operations you have to perform . 
```
select * from(select  to_date(from_unixtime(UNIX_TIMESTAMP(date1,'dd/mm/yyyy'))) as date3 from airquality) as innertable where date3 between '2004-01-10'and '2004-02-10';
```
12 . sorting operation you have to perform . 
15 . distinct operation you have to perform . 
```
select distinct(po) frpm airquality;
```
16 . like an operation you have to perform . 
17 . union operation you have to perform . 
18 . table view operation you have to perform . 






hive operation with python

Create a python application that connects to the Hive database for extracting data, creating sub tables for data processing, drops temporary tables.fetch rows to python itself into a list of tuples and mimic the join or filter operations
