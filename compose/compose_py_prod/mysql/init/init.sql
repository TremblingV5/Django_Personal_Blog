# compose/mysql/init/init.sql
Alter user 'admin'@'%' IDENTIFIED WITH mysql_native_password BY 'root';
GRANT ALL PRIVILEGES ON personal_blog.* TO 'admin'@'%';
FLUSH PRIVILEGES;