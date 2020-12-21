#to read password in text
def readText(filename):
    files = open(filename,"r")
    data = files.read().split('\n')
    files.close()
    return data

class MysqlConfiq():
    # database config
    mysqldata = readText("mysqldata.txt")
    MYSQL_HOST = mysqldata[0]
    MYSQL_USER = mysqldata[1]
    MYSQL_PASS = mysqldata[2]
    MYSQL_DBNAME = mysqldata[3]
    MYSQL_PORT = mysqldata[4]

    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s:%s/%s?charset=utf8mb4" % (
        MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False