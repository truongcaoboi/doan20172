package Model;
import java.util.*;
public class Phuongan {
	private Vector<Nongsan> v;
	private float loinhuan;
	private float chiphi;
	public float getLoinhuan() {
		return this.loinhuan;
	}
	public float getChiphi() {
		return this.chiphi;
	}
	public void setLoinhuan(float loinhuan) {
		this.loinhuan=loinhuan;
	}
	public void setChiphi(float chiphi) {
		this.chiphi=chiphi;
	}
	public void khoiTao(Vector<Nongsan> c) {
		this.v=new Vector<Nongsan>(c);
	}
	public Vector<Nongsan> getVectorNS(){
		return this.v;
	}
	public float tongChiPhi() {
		float chiphi = 0;
		for(int i=0;i<this.v.size();i++) {
			Nongsan ns=(Nongsan)this.v.get(i);
			chiphi = chiphi + ns.tinhChiphi();
		}
		return chiphi;
	}
	public float tongLoiNhuan() {
		float loinhuan=0;
		for(int i=0;i<this.v.size();i++) {
			Nongsan ns=(Nongsan)this.v.get(i);
			loinhuan=loinhuan+ns.tinhLoiNhuan();
		}
		return loinhuan;
	}
}