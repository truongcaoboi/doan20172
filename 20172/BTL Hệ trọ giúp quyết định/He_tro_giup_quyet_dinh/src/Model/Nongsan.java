package Model;

public class Nongsan {
	private String name;
	private String ma_nong_san;
	private float dientich;
	private float giaca;
	private float nangsuattoida;
	private float chiphi;
	public Nongsan(String name,String ma,float dientich,float giaca,float nangsuattoida,float chiphi) {
		this.name=name;
		this.ma_nong_san=ma;
		this.dientich=dientich;
		this.giaca=giaca;
		this.nangsuattoida=nangsuattoida;
		this.chiphi=chiphi;
	}
	public String get_name() {
		return this.name;
	}
	public String get_manongsan() {
		return this.ma_nong_san;
	}
	public float get_nangsuattoida() {
		return this.nangsuattoida;
	}
	public float getDientich() {
		return this.dientich;
	}
	public float getGiaca() {
		return this.giaca;
	}
	public float get_chiphi() {
		return this.chiphi;
	}
	public void setName(String name) {
		this.name=name;
	}
	public void setManongsan(String ma) {
		this.ma_nong_san=ma;
	}
	public void setDientich(float dientich) {
		this.dientich=dientich;
	}
	public void setGiaca(float gia) {
		this.giaca=gia;
	}
	public void setNangsuattoida(float nangsuat) {
		this.nangsuattoida=nangsuat;
	}
	public void setChiphi(float chiphi) {
		this.chiphi=chiphi;
	}
	public float tinhLoiNhuan() {
		float loinhuan;
		loinhuan=(this.giaca*this.nangsuattoida-this.chiphi)*this.dientich;
		return loinhuan;
	}
	public float tinhChiphi() {
		float chiphi;
		chiphi=this.chiphi*this.dientich;
		return chiphi;
	}
}
