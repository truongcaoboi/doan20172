package Controler;
import java.sql.*;
import java.util.*;
import Model.Nongsan;
import Model.Phuongan;
public class Kiemthu {
	public static void main(String args[]) throws SQLException {
		Phuongan dapso;
		Vector<Nongsan> danhsach=new Vector<Nongsan>();
		Vector<Phuongan> ketqua;
		danhsach=new Execute().taoDanhSach("NS01",danhsach,(float)0.9,(float)0.7,11);
		danhsach=new Execute().taoDanhSach("NS02",danhsach,(float)0.9,(float)0.7,10);
		danhsach=new Execute().taoDanhSach("NS03",danhsach,(float)0.9,(float)0.7,11);
		for(int i=0;i<danhsach.size();i++) {
			Nongsan ns=(Nongsan)danhsach.get(i);
			System.out.println("ma: "+ns.get_manongsan()+" namme: "+ns.get_name()+" chiphi: "+ns.get_chiphi()+" giaca: "+ns.getGiaca()+" nangsuat: "+ns.get_nangsuattoida());
		}
		System.out.println("\n");
		ketqua=new Execute().taoKetQua(danhsach,10, 1000000);
		dapso=new Execute().phantich(ketqua,10);
		Vector<Nongsan> vns=dapso.getVectorNS();
		for(int i=0;i<danhsach.size();i++) {
			Nongsan ns=(Nongsan)danhsach.get(i);
			System.out.println("ma: "+ns.get_manongsan()+" namme: "+ns.get_name()+" chiphi: "+ns.get_chiphi()+" giaca: "+ns.getGiaca()+" nangsuat: "+ns.get_nangsuattoida());
		}
		System.out.println("ketqua: ");
		for(int i=0;i<vns.size();i++) {
			Nongsan ns=(Nongsan)vns.get(i);
			System.out.println(ns.get_name()+"\t"+ns.getDientich()*10/100+" (m2)");
		}
		System.out.println("tai sao xoa r ma van hien ra vay?");
	}
}
