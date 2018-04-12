# -- coding: utf8 --
import pymysql.cursors
import os
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
		diachi=input(u"nhập địa chỉ sinh viên: ")
		email=input(u"nhập địa chỉ email sinh viên: ")
		sdt=input(u"nhập số điện thoại sinh viên: ")
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
		username=input(u"nhập username cần xóa: ")
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
		diachi=input(u"nhập lại địa chỉ: ")
		email=input(u"nhập lại địa chỉ email: ")
		sdt=input(u"nhập lại số điện thoại: ")
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
def update_lop():
	try:
		malop=input(u"nhập mã lớp cần sửa đổi: ")
		malop1=input(u"nhập lại mã lớp: ")
		tenlop=input(u"nhập lại tên lớp: ")
		makhoavien=input(u"nhập lại mã khoa viện trực thuôc: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql1="""update sinhvien set malop='"""+malop1+"""' where malop='"""+malop+"""'"""
		cursor.execute(sql2)
		cursor.execute(sql1)
		con.commit()
	except:
		print (u"có lỗi xảy ra")
		con.rollback()
	finally:
		con.close()
def update_khoavien():
	try:
		makhoavien=input(u"nhập mã khoa viện cần sửa đổi: ")
		makhoavien1=input(u"nhập lại mã khoa viện: ")
		tenkhoavien=input(u"nhập tên khoa viện: ")
		con=ketnoiDB()
		cursor=con.cursor()
		sql1="""update lop set makhoavien='"""+makhoavien1+"""' where makhoavien='"""+makhoavien+"""'"""
		cursor.execute(sql2)
		cursor.execute(sql1)
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
def in_danh_sach_lop():
	try:
		malop=input(u"nhập mã lớp cần in: ")
		f=open("ketqua.html","w")
		con=ketnoiDB()
		cursor=con.cursor()
		sql="""select mssv,name,tenlop,tenkhoavien from sinhvien,lop,khoavien where sinhvien.malop=lop.malop and lop.makhoavien=khoavien.makhoavien and lop.malop='"""+malop+"""'"""
		cursor.execute(sql)
		str="mã số sinh viên\thọ tên"
		f.write(u"đặng xuân trường")
		print("zzz")
		for row in cursor:
			str=row['mssv']+"\t"+row['name']
			f.write(str)
	except:
		print (u"có lỗi xảy ra!")
	finally:
		con.close()
		f.close()
#insert_khoavien()
#insert_lop()
#insert_sinhvien()
#insert_taikhoan()
#delete_lop();
#delete_sinhvien()
#delete_taikhoan()
#os.system('cls');
#update_khoavien();
#update_lop();
#thong_tin_ca_nhan('123')
in_danh_sach_lop()
nhac=input (u"nhập một phím để kết thúc: ")
nhac=input (u"nhập một phím để kết thúc: ")