##

settings 里的 DATABASES 字典中，default 这个键是必须的。

python manage.py migrate --database=custom

## 自动路由

数据库 router 是一个类，它提供4个方法，如果不是自定义它的行为，一般学会怎样使用默认的就够了。

### 使用

通过 DATABASE_ROUTERS 这个属性设置。
