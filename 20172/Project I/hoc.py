import pymysql.cursors  
 
# Kết nối vào database.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1111',                             
                             db='nmcnpm',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
print ("connect successful!!")
try:
  
 
    with connection.cursor() as cursor:
       
        # SQL 
        sql = "SELECT username,password FROM manager "
         
        # Thực thi câu lệnh truy vấn (Execute Query).
        cursor.execute(sql)
         
        print ("cursor.description: ", cursor.description)
 
        print()
        for row in cursor:
            print(row['username'],"\t",row['password'])
             
finally:
    # Đóng kết nối (Close connection).       
    connection.close()
