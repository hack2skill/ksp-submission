from sqlconnector import SqlConnector

obj = SqlConnector()
print(obj.retrieve("describe virustotal"))
a = obj.retrieve("select * from app_list")
print(a[0])
a = obj.retrieve("select * from virustotal")
print(a[0])