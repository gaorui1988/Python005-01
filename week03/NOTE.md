## 学习笔记  



- MySQL安装  
```
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