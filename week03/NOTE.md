

# 学习笔记  













## MySQL安装  







```bash
//yum 安装MySQL community 5.7.2

//安装MySQL社区版release包（安装后会生成repo源）
wget http://dev.mysql.com/get/mysql57-community-release-el7-8.noarch.rpm
yum localinstall mysql57-community-release-el7-8.noarch.rpm

//查看repo源中可安装的MySQL社区版相关RPM软件包
yum repolist enabled | grep "mysql.*-community.*"

//使用yum方式安装
yum install mysql-community-server

//查看已安装的MySQL软件包
[root@host54 yum.repos.d]# rpm -qa |grep -i mysql
mysql57-community-release-el7-8.noarch
mysql-community-client-5.7.32-1.el7.x86_64
mysql-community-libs-5.7.32-1.el7.x86_64
mysql-community-libs-compat-5.7.32-1.el7.x86_64
mysql-community-server-5.7.32-1.el7.x86_64
mysql-community-common-5.7.32-1.el7.x86_64
[root@host54 yum.repos.d]#

//启用、开机自启、查看状态
systemctl start mysqld
systemctl enable mysqld
systemctl status mysqld


//查看MySQL安装后默认密码（需修改）
[root@host54 yum.repos.d]# grep 'password'  /var/log/mysqld.log |head  -1
2020-12-09T13:22:32.937372Z 1 [Note] A temporary password is generated for root@localhost: &6dIZgrihXjQ
[root@host54 yum.repos.d]#

//使用管理员root登录MySQL
[root@host54 yum.repos.d]# mysql -uroot -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 5.7.32


//重置root密码（不符合密码复杂度，如下提示）
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
ERROR 1819 (HY000): Your password does not satisfy the current policy requirements
mysql>

//设置root密码（默认策略：需要一定密码复杂度）
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'Xietong@12345';
Query OK, 0 rows affected (0.00 sec)

//查看设置密码策略（默认MEDIUM，复杂度过低会提示过于简单不允许通过）
mysql> SHOW VARIABLES LIKE 'validate_password%';
+--------------------------------------+--------+
| Variable_name                        | Value  |
+--------------------------------------+--------+
| validate_password_check_user_name    | OFF    |
| validate_password_dictionary_file    |        |
| validate_password_length             | 8      |
| validate_password_mixed_case_count   | 1      |
| validate_password_number_count       | 1      |
| validate_password_policy             | MEDIUM |
| validate_password_special_char_count | 1      |
+--------------------------------------+--------+
7 rows in set (0.01 sec)

mysql>

//降低密码复杂度（调整为LOW）
mysql> set global validate_password_policy=0 ;
Query OK, 0 rows affected (0.00 sec)

mysql> SHOW VARIABLES LIKE 'validate_password%';
+--------------------------------------+-------+
| Variable_name                        | Value |
+--------------------------------------+-------+
| validate_password_check_user_name    | OFF   |
| validate_password_dictionary_file    |       |
| validate_password_length             | 8     |
| validate_password_mixed_case_count   | 1     |
| validate_password_number_count       | 1     |
| validate_password_policy             | LOW   |
| validate_password_special_char_count | 1     |
+--------------------------------------+-------+
7 rows in set (0.01 sec)


mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '12345678';
Query OK, 0 rows affected (0.00 sec)

[root@host54 yum.repos.d]# mysql -uroot -p12345678
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.32 MySQL Community Server (GPL)

Copyright (c) 2000, 2020, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> quit
Bye


```

- 正确使用MySQL字符集  

```
//字符集





```


- 多种方式连接MySQL数据库  

```




```









## PyMsql增删改查操作

**mod3_pymsql_conn.py**

```python
#!/usr/bin/python3
# PyMYSQL 连接 MySQL 数据库
# pip3 install PyMySQL

#导入python连接MySQL第三方库
import pymysql

# 打开数据库连接
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';

db = pymysql.connect("server1","testuser","testpass","testdb" )
 
try:

    # 使用 cursor() 方法创建一个游标对象 cursor
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f"fetch error {e}")

finally: 
    # 关闭数据库连接
    db.close()

 
print (f"Database version : {result} ")

```



**mod3_pymsql_insert.py**

```python
#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect("server1","testuser","testpass","testdb")
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        # 拼接SQL语句（对于pymysql，插入数字、字符串都是使用"%s"占位符）
        sql = 'INSERT INTO book (id, name) VALUES (%s, %s)'
        # 支持插入中文（需支持UTF-8的字符集）
        value = (1002, "活着")
        cursor.execute(sql, value)
    # pymysql提交还是要用commit的显式提交（隐式提交：提交已经被封装到SQLAlchemy中）
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    #返回查询结果集当中的行数（并不是当前表中有多少行数据，是当前游标操作后作用的行数）
    print(cursor.rowcount)


```



**mod3_pymysql_query.py**

```python
#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect("server1","testuser","testpass","testdb" )
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = '''SELECT name FROM book'''
        cursor.execute(sql)
        
        # fetchall() 匹配的数据集当中的所有行
        # fetchone() 匹配的数据集当中的一行
        books = cursor.fetchall() 
        # for迭代元组中的值
        for book in books: 
            print(book)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)


```



**mod3_pymysql_update.py**

```python
#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect("server1","testuser","testpass","testdb" )
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        
        # SQL与python之间的思维转换（下面这个执行是不生效的）
        # sql = 'UPDATE book SET name = %s' WHERE id = %s
        # value = ("活着", 1003)
        
        # 正确的更新SQL
        sql = 'UPDATE book SET id = %s WHERE name = %s'
        value = (1003, "活着")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)


```



**mod3_pymsql_delete.py**

```python
#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect("server1","testuser","testpass","testdb" )
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = 'DELETE FROM book WHERE name = %s'
        value = ("活着")
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    # 这里也是判断上面的SQL操作是否正常执行
    print(cursor.rowcount)


```

> 使用pymysql操作数据库时，大部分的结构代码是不需要去改变，唯一要改变的是我们编写的SQL，以及去填入的占位符（通过外部的应用程序，或是用户输入）。
>
> 自己写的python程序，相互调用进行处理的时候，可以通过函数的参数进行直接处理；如果是用户输入的话，输入之前需要做一些检测（比如，用户输入的内容是否合法，用户输入的内容是不是SQL注入等安全性的问题），这样才更适用与企业中的一些应用





