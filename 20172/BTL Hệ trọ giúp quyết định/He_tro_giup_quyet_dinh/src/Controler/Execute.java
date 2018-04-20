package Controler;
import java.util.*;
import java.sql.*;
import Model.Nongsan;
import Model.Phuongan;
public class Execute {
	public Vector<Nongsan> taoDanhSach(String ma,Vector<Nongsan> v,float k,float t, int thang) throws SQLException{
		Connection con=ConnectDB.connect();
		if(con==null) {
			return null;
		}else {
			Statement state=con.createStatement();
			String sql="select nongsan.ma,name,giaca,nangsuattoida,chiphidukien from nongsan,chiphi where nongsan.ma=chiphi.ma and chiphi.ma=\'"+ma+"\' and thang like \'%"+thang+" %\';";
			ResultSet rs =state.executeQuery(sql);
			while(rs.next()) {
				String mans=rs.getString("ma");
				String name=rs.getString("name");
				float dientich=0;
				float giaca=rs.getFloat("giaca");
				float chiphi=rs.getFloat("chiphidukien");
				float nangsuat=rs.getFloat("nangsuattoida")*k*t;
				Nongsan ns=new Nongsan(name,mans,dientich,giaca,nangsuat,chiphi);
				v.addElement(ns);
			}
		}
		return v;
	}
	public int check(Vector<Nongsan> v,int i,float dientich,float von) {
		float s=0;
		float chiphi=0;
		for(int j=0;j<v.size();j++) {
			Nongsan ns=(Nongsan)v.get(j);
			s=s+ns.getDientich();
		}
		if(s<100) {
			if(i<v.size()-1) {
				return 0;//chua du gia tri
			}else {
				return 1;//chua du dien tich
			}
		}else {
			if(s==100) {
				if(i==v.size()-1) {
					for(int j=0;j<v.size();j++) {
						Nongsan ns=(Nongsan)v.get(j);
						chiphi=chiphi+ns.getDientich()*ns.get_chiphi()*dientich/100;
					}
					if(chiphi<=von) {
						return 2;
					}else {
						return -1;
					}
				}else {
					return -1;
				}
			}else {
				return -1;
			}
		}
/*		if(i<v.size()-1) {
			return 0;
		}else {
			for(int j=0;j<v.size();j++) {
				Nongsan ns=(Nongsan)v.get(j);
				s=s+ns.getDientich();
			}
			if(s<100) {
				return 1;
			}else {
				for(int j=0;j<v.size();j++) {
					Nongsan ns=(Nongsan)v.get(j);
					chiphi=chiphi+ns.getDientich()*ns.get_chiphi()*dientich/100;
				}
				if(chiphi<=von && s==100) {
					return 2;
				}else {
					return -1;
				}
			}
		}*/
	}
	//0 neu chua du gia tri 1 neu chua du dien tich 2 neu thoa man -1 neu ko thoa man
	public Vector<Phuongan> taoKetQua(Vector<Nongsan> ds,float dientich,float von) throws ArrayIndexOutOfBoundsException{
		Vector<Phuongan> ketqua=new Vector<Phuongan>();
		Vector<Nongsan> vns;
		Nongsan ns;
		Phuongan pa=new Phuongan();
		while(true) {
			pa.khoiTao(ds);
			vns=pa.getVectorNS();
			for(int i=0;i<vns.size();i++) {
				ns=(Nongsan)vns.get(i);
				ns.setDientich(ns.getDientich()+5);
				int che=new Execute().check(vns, i, dientich, von);
				if(che==0) {
					continue;
				}else {
					if(che==1) {
						i--;
					}else {
						if(che==2) {
							Vector<Nongsan> bansao=new Vector<Nongsan>();
							Phuongan pa1=new Phuongan();
							for(int j=0;j<vns.size();j++) {
								ns=(Nongsan)vns.get(j);
								Nongsan c=new Nongsan(ns.get_name(),ns.get_manongsan(),ns.getDientich(),ns.getGiaca(),ns.get_nangsuattoida(),ns.get_chiphi());
								bansao.addElement(c);
							}
							pa1.khoiTao(bansao);
							ketqua.addElement(pa1);
							System.out.println("ket qua sau khi them:"+ketqua.size());
							for(int h=0;h<ketqua.size();h++) {
								pa=(Phuongan)ketqua.get(h);
								Vector<Nongsan> dsns=pa.getVectorNS();
								for(int j=0;j<dsns.size();j++) {
									 ns=dsns.get(j);
									System.out.print("dien tich nong san "+j+": "+ns.getDientich());
								}
								System.out.println("\n");
							}
							for(int j=i;j<vns.size();j++) {
								ns=(Nongsan)vns.get(j);
								ns.setDientich(0);
							}
							i=i-2;
						}else {
							for(int j=i;j<vns.size();j++) {
								ns=(Nongsan)vns.get(j);
								ns.setDientich(0);
							}
							i=i-2;
						}
					}
				}
				if(i==-2) {
					break;
				}
			}
			break;
		}
		return ketqua;
	}
	public void tinhLoiNhuanChiPhi(Vector<Phuongan> ketqua,float dientich) {
		for(int i=0;i<ketqua.size();i++) {
			Phuongan pa=(Phuongan)ketqua.get(i);
			pa.setChiphi(pa.tongChiPhi()*dientich/100);
			pa.setLoinhuan(pa.tongLoiNhuan()*dientich/100);
			System.out.println("phuongan: "+i+"co chi phi: "+pa.getChiphi()+"co loi nhuan: "+pa.getLoinhuan());
		}
	}
	public float maxLoiNhuan(Vector<Phuongan> ketqua) {
		float max=-999999999;
		System.out.println(max);
		for(int i=0;i<ketqua.size();i++) {
			Phuongan pa=(Phuongan)ketqua.get(i);
			System.out.println(pa.getLoinhuan());
			if(max<pa.getLoinhuan()) {
				max=pa.getLoinhuan();
				System.out.print(i+" ");
			}
		}
		System.out.println(max);
		return max;
	}
	public float minChiPhi(Vector<Phuongan> ketqua) {
		float min=999999999;
		for(int i=0;i<ketqua.size();i++) {
			Phuongan pa=(Phuongan)ketqua.get(i);
			if(min>pa.getChiphi()) {
				min=pa.getChiphi();
			}
		}
		return min;
	}
	public Phuongan phantich(Vector<Phuongan> ketqua,float dientich){
		Execute ex=new Execute();
		Vector<Phuongan> ketqua1=new Vector<Phuongan>();
		Vector<Phuongan> ketqua2=new Vector<Phuongan>();
		float maxLoiNhuan=0;
		float minChiPhi=0;
		ex.tinhLoiNhuanChiPhi(ketqua,dientich);
		maxLoiNhuan=ex.maxLoiNhuan(ketqua);
		System.out.println(ketqua.size());
		for(int i=0;i<ketqua.size();i++) {
			Phuongan pa=ketqua.get(i);
			if(pa.getLoinhuan()>=maxLoiNhuan) {
				ketqua1.addElement(pa);
			}
		}
		System.out.println(ketqua1.size());
		if(ketqua1.size()==1) {
			Phuongan pa=(Phuongan)ketqua1.get(0);
			Vector<Nongsan> ns=pa.getVectorNS();
			Phuongan dapso=new Phuongan();
			dapso.khoiTao(ns);
			return dapso;
		}else {
			minChiPhi=ex.minChiPhi(ketqua1);
			for(int i=0;i<ketqua1.size();i++) {
				Phuongan pa=ketqua1.get(i);
				if(pa.getLoinhuan() <= minChiPhi) {
					ketqua2.addElement(pa);
				}
			}
			System.out.println(ketqua2.size());
			Phuongan pa1=(Phuongan)ketqua2.get(0);
			Vector<Nongsan> ns=pa1.getVectorNS();
			Phuongan dapso=new Phuongan();
			dapso.khoiTao(ns);
			return dapso;
		}
	}
}

























