 # -- coding: utf8 --
import os
import pymysql.cursors
class Student():
	def __init__(self,mssv,name,diachi,email,sdt,lop,khoavien):
		self.mssv=mssv
		self.name=name
		self.diachi=diachi
		self.email=email
		self.sdt=sdt
		self.lop=lop
		self.khoavien=khoavien
		return
	def display(self):
		print (u"mã số sinh viên: %s"%(self.mssv))
		print (u"họ và tên sinh viên: %s"%(self.name))
		print (u"địa chỉ của sinh viên: %s"%(self.diachi))
		print (u"địa chỉ email của sinh viên: %s"%(self.email))
		print (u"sô điện thoại của sinh viên: %s"%(self.sdt))
		print (u"sinh viên thuộc lớp: %s"%(self.lop))
		print (u"sinh viên thuộc viện: %s"%(self.khoavien))
		return
class Lopsinhvien():
	def __init__(self,malop,tenlop,makhoavien):
		self.malop=malop
		self.tenlop=tenlop
		self.makhoavien=makhoavien
class Khoavien():
	def __init__(self,makhoavien,tenkhoavien):
		self.makhoavien=makhoavien
		self.tenkhoavien=tenkhoavien
class Taikhkoan():
	def __init__(self,username,password,quyen):
		self.username=username
		self.password=password
		self.quyen=quyen
	def getusername(self):
		return self.username
	def getpassword(self):
		return self.password
	def getquyen(self):
		return self.quyen
	def setpassword(self):
		self.password=password
def ketnoiDB():
	con=pymysql.connect(host="localhost",user="root",password="1111",db="btl",charset="utf8",cursorclass=pymysql.cursors.DictCursor)
	return con
def insert_lop():
	try:
		malop=input(u"nhập mã lớp cần thêm: ")
		tenlop=input(u"nhập tên lớp cần thêm: ")
		makhoavien=input(u"nhập mã khoa viện trực thuôc: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""insert into lop(malop,tenlop,makhoavien) values ('"""+malop+"""','"""+tenlop+"""','"""+makhoavien+"""')"""
		cursor.execute(sql)
		con.commit()
	except:
		print(u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def insert_khoavien():
	try:
		makhoavien=input(u"nhập mã khoa viện cần thêm: ")
		tenkhoavien=input(u"nhập tên khoa viện cần thêm: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""insert into khoavien(makhoavien,tenkhoavien) values ('"""+makhoavien+"""','"""+tenkhoavien+"""')"""
		cursor.execute(sql)
		con.commit()
	except:
		print(u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def insert_sinhvien():
	try:
		mssv=input(u"nhập mã số sinh viên cần thêm: ")
		name=input(u"nhập tên sinh viên cần thêm: ")
		diachi=input(u"nhập địa chỉ sinh viên (không được bỏ trống): ")
		email=input(u"nhập địa chỉ email sinh viên (không được bỏ trống): ")
		sdt=input(u"nhập số điện thoại sinh viên (không được bỏ trống): ")
		malop=input(u"nhập mã lớp thêm sinh viên: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""insert into sinhvien(mssv,name,diachi,email,sdt,malop) values ('"""+mssv+"""','"""+name+"""','"""+diachi+"""','"""+email+"""','"""+sdt+"""','"""+malop+"""')"""
		cursor.execute(sql)
		con.commit()
	except:
		print(u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def insert_taikhoan():
	try:
		username=input(u"nhập username: ")
		password=input(u"nhập password: ")
		quyen=input(u"cấp phát quyền(1 là admin, 2 là sinh viên): ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""insert into taikhoan(username,password,quyen) values ('"""+username+"""','"""+password+"""',"""+quyen+""")"""
		cursor.execute(sql)
		con.commit()
	except:
		print(u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def delete_lop():
	try:
		malop=input(u"nhập mã lớp cần xóa: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql1="""delete from taikhoan where username in (select mssv from sinhvien where sinhvien.malop='"""+malop+"""')"""
		sql2="""delete from sinhvien where sinhvien.malop='"""+malop+"""'"""
		sql3="""delete from lop where lop.malop='"""+malop+"""'"""
		cursor.execute(sql1)
		cursor.execute(sql2)
		cursor.execute(sql3)
		con.commit()
	except:
		print(u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def delete_sinhvien():
	try:
		mssv=input(u"nhập mã số sinh viên cần xóa: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql1="""delete from taikhoan where username ='"""+mssv+"""'"""
		sql2="""delete from sinhvien where sinhvien.mssv='"""+mssv+"""'"""
		cursor.execute(sql1)
		cursor.execute(sql2)
		con.commit()
	except:
		print(u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def delete_taikhoan():
	try:
		username=input(u"nhập mã số sinh viên cần xóa: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql1="""delete from taikhoan where username ='"""+username+"""'"""
		cursor.execute(sql1)
		con.commit()
	except:
		print(u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def update_taikhoan(username):
	try:
		password=input(u"nhập mật khẩu mới: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql1="""update taikhoan set password='"""+password+"""' where username='"""+username+"""'"""
		cursor.execute(sql1)
		con.commit()
	except:
		print(u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def update_sinhvien1():
	try:
		mssv=input(u"nhập mssv cần sửa đổi:" )
		mssv1=input(u"nhập lại mã số sinh viên: ")
		name=input(u"nhập lại tên sinh viên: ")
		diachi=input(u"nhập lại địa chỉ (không được bỏ trống): ")
		email=input(u"nhập lại địa chỉ email (không được bỏ trống): ")
		sdt=input(u"nhập lại số điện thoại (không được bỏ trống): ")
		malop=input(u"nhập lại mã lớp: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""update sinhvien set mssv='"""+mssv1+"""',name='"""+name+"""',diachi='"""+diachi+"""',email='"""+email+"""',sdt='"""+sdt+"""',malop='"""+malop+"""' where mssv='"""+mssv+"""'"""
		cursor.execute(sql)
		con.commit()
	except:
		print (u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def update_sinhvien2(username):
	try:
		name=input(u"nhập lại tên sinh viên: ")
		diachi=input(u"nhập lại địa chỉ: ")
		email=input(u"nhập lại địa chỉ email: ")
		sdt=input(u"nhập lại số điện thoại: ")
		malop=input(u"nhập lại mã lớp: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""update sinhvien set name='"""+name+"""',diachi='"""+diachi+"""',email='"""+email+"""',sdt='"""+sdt+"""',malop='"""+malop+"""' where mssv='"""+username+"""'"""
		cursor.execute(sql)
		con.commit()
	except:
		print (u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def thong_tin_ca_nhan(username):
	try:
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""select mssv,name,diachi,email,sdt,tenlop,tenkhoavien from sinhvien,lop,khoavien where sinhvien.malop=lop.malop and lop.makhoavien=khoavien.makhoavien and mssv='"""+username+"""'"""
		cursor.execute(sql)
		for row in cursor:
			mssv=row['mssv']
			name=row['name']
			diachi=row['diachi']
			email=row['email']
			sdt=row['sdt']
			tenlop=row['tenlop']
			tenkhoavien=row['tenkhoavien']
			sv=Student(mssv,name,diachi,email,sdt,tenlop,tenkhoavien)
			sv.display()
	except:
		print (u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def tim_sinh_vien():
	try:
		mssv=input(u"nhập mã số sinh viên bạn muốn tim: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""select mssv,name,tenlop,tenkhoavien from sinhvien,lop,khoavien where sinhvien.malop=lop.malop and lop.makhoavien=khoavien.makhoavien and mssv='"""+mssv+"""'"""
		cursor.execute(sql)
		print (u"mssv\thọ tên\t\t\ttên lớp\t\ttên khoa viện")
		for row in cursor:
			print (u"%s\t%s\t\t\t%s\t\t%s"%(row['mssv'],row['name'],row['tenlop'],row['tenkhoavien']))
	except:
		print(u"có lỗi xảy ra!")
	finally:
		con.close()
def xem_danh_sach_lop():
	try:
		malop=input(u"nhập mã lớp: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""select mssv,name,tenlop,tenkhoavien from sinhvien,lop,khoavien where sinhvien.malop=lop.malop and lop.makhoavien=khoavien.makhoavien and lop.malop='"""+malop+"""'"""
		cursor.execute(sql)
		print (u"mssv\thọ tên\t\t\ttên lớp\t\ttên khoa viện")
		for row in cursor:
			print (u"%s\t%s\t\t\t%s\t\t%s"%(row['mssv'],row['name'],row['tenlop'],row['tenkhoavien']))
	except:
		print(u"có lỗi xảy ra!")
	finally:
		con.close()	
def quan_li_chung():
	try:
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""select makhoavien,tenkhoavien from khoavien"""
		sql1="""select lop.malop as ml,tenlop,count(mssv) as soluong,tenkhoavien from sinhvien,lop,khoavien where sinhvien.malop=lop.malop and lop.makhoavien=khoavien.makhoavien group by lop.malop,tenlop,tenkhoavien"""
		print(u"danh sách các khoa viện: ")
		print(u"mã khoa viện\ttên khoa viên")
		cursor.execute(sql)
		for row in cursor:
			print(u"%s\t%s"%(row['makhoavien'],row['tenkhoavien']))
		cursor.execute(sql1)
		print(u"danh sách các lớp")
		print (u"mã lớp\ttên lớp\t\t\ttên khoa viện\t\tsố lượng sinh viên")
		for row in cursor:
			print (u"%s\t%s\t\t\t%s\t\t%s"%(row['ml'],row['tenlop'],row['tenkhoavien'],row['soluong']))
	except:
		print(u"có lỗi xảy ra!")
	finally:
		con.close()
def check(username,password):
	n=0
	#ket noi voi co so du lieu
	try:
		con=ketnoiDB()
		cursor=con.cursor()
		#lay ra mat khau cua username tuong ung
		sql="""select password,quyen from taikhoan where username='"""+username+"""'"""
		cursor.execute(sql)
		for row in cursor:
			#neu tai khoan ton tai thi so sanh mat khau
			sosanh=row['password']
			if(password==sosanh):
				#neu mat khau trung khop thi xem quyen ung dung
				n=row['quyen']
	except:
		print(u"tài khoản hoặc mật khẩu không đúng")
		nhac=input(u"vui lòng nhập phím enter để tiếp tục!!!")
	finally:
		con.close()
	return n
n=0
while(n==0):
	os.system('cls')
	username=input(u"nhập tài khoản của bạn: ")
	password=input(u"nhập mật khẩu của bạn: ")
	n=check(username,password)
	if(n==0):
		print(u"tài khoản hoặc mật khẩu không đúng")
		nhac=input(u"vui lòng nhập phím enter để tiếp tục!!!")
m=1
while(m==1):
	os.system('cls')
	if(n==1):
		k=0
		while (k==0):
			os.system('cls')
			print(u"1. thêm khoa viên")
			print(u"2. thêm lớp")
			print(u"3. thêm sinh viên")
			print(u"4. thêm tài khoản")
			print(u"5. xóa tài khoản")
			print(u"6. xóa sinh viên")
			print(u"7. xóa lớp")
			print(u"8. sửa thông tin sinh viên")
			print(u"9. tìm kiếm sinh viên")
			print(u"10. xem danh sach sinh viên của lớp")
			print(u"11. xem thông tin chung")
			print(u"12. đổi mật khẩu")
			print(u"13. thoát")
			k=input(u"bạn hãy chọn thao tác thực hiện: ")
			try:
				k=int(k)
			except:
				k=0
			if((0<k) and (k<14)):
				if(k==1):
					insert_khoavien()
					k=0
					nhac=input()
				elif (k==2):
					insert_lop()
					k=0
					nhac=input()
				elif (k==3):
					insert_sinhvien()
					k=0
					nhac=input()
				elif (k==4):
					insert_taikhoan()
					k=0
					nhac=input()
				elif (k==5):
					delete_taikhoan()
					k=0
					nhac=input()
				elif (k==6):
					delete_sinhvien()
					k=0
					nhac=input()
				elif (k==7):
					delete_lop()
					k=0
					nhac=input()
				elif (k==8):
					update_sinhvien1()
					k=0
					nhac=input()
				elif (k==9):
					mssvtim=input(u"nhập mã số sinh viên cần tìm: ")
					thong_tin_ca_nhan(mssvtim)
					k=0
					nhac=input()
				elif (k==10):
					xem_danh_sach_lop()
					k=0
					nhac=input()
				elif (k==11):
					quan_li_chung()
					k=0
					nhac=input()
				elif (k==12):
					update_taikhoan(username)
					k=0
					nhac=input()
				elif (k==13):
					k=1
			else:
				k=0;
				nhac=input(u"bạn lựa chon sai, nhấn phím bất kì để tiếp tục: ")
	else:
		k=0
		while(k==0):
			os.system('cls')
			print(u"1. xem thông tin cá nhân")
			print(u"2. sửa thông tin cá nhân")
			print(u"3. tìm sinh viên")
			print(u"4. xem danh sách lớp")
			print(u"5. đổi mật khẩu")
			print(u"6. thoat")
			k=input(u"hãy chọn thao tác cần thực hiện: ")
			try:
				k=int(k)
			except:
				k=0
			if((0<k) and (k<7)):
				if (k==1):
					thong_tin_ca_nhan(username)
					k=0
					nhac=input()
				elif (k==2):
					update_sinhvien2(username)
					k=0
					nhac=input()
				elif (k==3):
					tim_sinh_vien()
					k=0
					nhac=input()
				elif (k==4):
					xem_danh_sach_lop()
					k=0
					nhac=input()
				elif (k==5):
					update_taikhoan(username)
					k=0
					nhac=input()
				elif (k==6):
					k=1
			else:
				k=0
				nhac=input(u"bạn lựa chọn sai, nhấn phím bất kì để tiếp tục: ")
	m=0
os.system('cls');
nhac=input (u"----GoodBye!!!----")
