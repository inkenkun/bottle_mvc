import MySQLdb
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config/db.cnf')

dbhandle = MySQLdb.connect(
  host = config.get('db', 'host'),
  port = config.getint("db","port"), 
  user = config.get('db', 'user'),
  passwd = config.get('db', 'password'),
  db = config.get('db', 'database'),
  use_unicode=1
)
con = dbhandle.cursor(MySQLdb.cursors.DictCursor)
