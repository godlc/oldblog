import pymysql
pymysql.install_as_MySQLdb()

db = pymysql.connect('localhost', 'root', 'LIANG520.3', 'books')
cursor = db.cursor()
db.close()