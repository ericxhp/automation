#encoding=utf-8
#Read data from excel and insert to db
import xlrd
import MySQLdb

fileName="DRIVE_PERFORMANCE_SM2752_ES4_2X_REL_2017_06_13_15_58_21.xlsx"

with xlrd.open_workbook(fileName) as bk:

	shxrange = range(bk.nsheets)

	try:

		sh = bk.sheet_by_name("Detail")
	except:
		print "no sheet in {} named Detail".format(fileName)

nrows = sh.nrows
print "There are {} number line in Detail sheet".format(nrows)

row_list = []

raw_data = sh.row_values(0)

for i in range(1,nrows):
	raw_data = sh.row_values(i)
	print raw_data
	TestCaseName ,Para , _ ,_ ,Status,ExecutTime,NodeName,_,_,LogPath,Comments = raw_data
	dbRow=["MRT","123",TestCaseName,Status,Para,NodeName,ExecutTime,"789ACD","Sample data"]

try:
	db = MySQLdb.connect("localhost","root","840706","database_test" )
	print "Connected to DB"
except:
	print "Can't connect to DB"


cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version : %s " % data

cursor.execute("SHOW TABLES")
tableInfo = cursor.fetchall()
print tableInfo[0][0]

# sql = "insert into detail(TestSuite, BuildID, TestCase,Status,Para,TestNode,ExecuteTime,LogPath,Comments) values(%s, %s, %s, %s, %s, %s, %s, %s ,%s)"  
# tmp = ("MRT","123",TestCaseName,Status,Para,NodeName,ExecutTime,"789ACD","Sample data")
# n=cursor.execute(sql, tmp)  
# print n

db.commit()  


n = cursor.execute("select * from detail")    
queryData = cursor.fetchall()
print queryData    
