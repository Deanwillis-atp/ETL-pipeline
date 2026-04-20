mysql> show databases;
+-----------------------+
| Database              |
+-----------------------+
| aggregated_stock_data |
| fintech               |
| information_schema    |
| mysql                 |
| performance_schema    |
| sys                   |
| test                  |
+-----------------------+
7 rows in set (0.002 sec)

mysql> use aggregated_stock_data;
Database changed
mysql> show tables;
Empty set (0.003 sec)

mysql> show tables;
+---------------------------------+
| Tables_in_aggregated_stock_data |
+---------------------------------+
| financial_data                  |
| metadata                        |
+---------------------------------+
2 rows in set (0.003 sec)

mysql> select count(*) from financial_data;
+----------+
| count(*) |
+----------+
|  1060049 |
+----------+
1 row in set (0.037 sec)

mysql> select count(*) from metadata;
+----------+
| count(*) |
+----------+
|   189541 |
+----------+
1 row in set (0.013 sec)

mysql> select * from metadata limit 5;
+----------------------+------+--------------------------------+------------+------+
| adsh                 | cik  | name                           | filed      | form |
+----------------------+------+--------------------------------+------------+------+
| 0000002178-14-000044 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 2014-05-12 | 10-Q |
| 0000002178-14-000056 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 2014-08-11 | 10-Q |
| 0000002178-14-000064 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 2014-11-07 | 10-Q |
| 0000002178-15-000030 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 2015-05-08 | 10-Q |
| 0000002178-15-000040 | 2178 | ADAMS RESOURCES & ENERGY, INC. | 2015-08-07 | 10-Q |
+----------------------+------+--------------------------------+------------+------+
5 rows in set (0.000 sec)

mysql> 

