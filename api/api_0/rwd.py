# 从ls.txt文件中读取108位梁山好汉的信息存入一个列表中
import pymysql

# 从文件中读取信息
def read():
    # 创建一个空列表以存储梁山108位好汉的信息
    allls = []
    # 打开ls.txt文件
    with open('ls.txt', 'r+') as file:
        # 文件中有108位梁山好汉，需要执行108次
        for i in range(108):
            # 创建一个空列表用以存储单个梁山好汉的信息
            onels = []
            # 在文件中一位梁山好汉的信息有7行，所以要连续读取七行的数据收集齐信息存入创建的空列表中
            for j in range(7):
                # 读取的行有最后的换行符，要去除
                a = file.readline().rstrip()
                # 将独立的单个信息存入个人列表
                onels.append(a)
            # 单人的完整信息存入梁山的总列表中
            allls.append(onels)
    return allls


# 与数据库建立连接，主要是为了做装饰器来修饰其他的功能
def connectsql(old):
    def now_function(*args, **kwargs):
        # 连接数据库
        mydb = pymysql.connect(host='localhost', user='root', password='147258', database='nszd1')
        # 游标
        mycursor = mydb.cursor()
        # 遍历列表依次存入数据库
        result = old(mycursor=mycursor, *args, **kwargs)
        # commit提交
        mydb.commit()
        # 关闭游标
        mycursor.close()
        # 断开与数据库的连接
        mydb.close()
        return result

    return now_function


@connectsql
def write_all(ouli, mycursor):
    # 将列表里的信息插入数据库中
    for ls in ouli:
        mycursor.execute(
            "insert into liangshan value({}, '{}', '{}', '{}', '{}', '{}', '{}');".format(int(ls[0]), ls[1], ls[2], ls[3], ls[4], ls[5], ls[6]))
    return None

# 向表中插入一条信息
@connectsql
def write_one(mycursor=None, number="", star="", nicknames="", name="", debut="", enertmountain="", positions=""):
    mycursor.execute(
        "insert into liangshan value({}, '{}', '{}', '{}', '{}', '{}', '{}');".format(int(number), star, nicknames, name, debut, enertmountain, positions))


@connectsql
def delete_all(mycursor):
    # 删除liangshan表中的所有数据
    return mycursor.execute("delete from liangshan;")


@connectsql
def delete_one(mycursor=None, name=""):
    # 删除liangshan表中指定的数据
    return mycursor.execute("delete from liangshan where name='{}';".format(name))

# 更新一条数据
@connectsql
def update_one(mycursor=None, old_number="", number="", star="", nicknames="", name="", debut="", enertmountain="", positions=""):
    return mycursor.execute(
        "update liangshan set number={}, star='{}', nicknames='{}', name='{}', debut='{}',enertmountain= '{}', positions='{}'  where number='{}';".format(
            int(number), star, nicknames, name, debut, enertmountain, positions, int(old_number)))


# 读取表中的所有信息
@connectsql
def query_all(mycursor=None):
    mycursor.execute("select * from liangshan;")
    results = mycursor.fetchall()
    out = dict()
    ji = 1
    # 将查询到的信息转换为字典类型
    for hang in results:
        dic = {'number': hang[0], 'star': hang[1], 'nicknames': hang[2], 'name': hang[3], 'debut': hang[4], 'enertmountain': hang[5], 'positions': hang[6]}
        out.setdefault(ji, dic)
        ji += 1
    # print(out)
    return out


# 读取表中的所有信息
@connectsql
def query_one(mycursor=None, name=""):
    mycursor.execute("select * from liangshan where name='{}';".format(name))
    results = mycursor.fetchall()
    # 将查询到的内容转换为字典
    for hang in results:
        dic = {'number': hang[0], 'star': hang[1], 'nicknames': hang[2], 'name': hang[3], 'debut': hang[4], 'enertmountain': hang[5], 'positions': hang[6]}
        return dic


if __name__ == '__main__':
    # 向数据库中插入所有108梁山信息
    write_all(read())
