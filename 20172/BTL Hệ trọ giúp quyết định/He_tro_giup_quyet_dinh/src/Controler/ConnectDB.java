package Controler;
import java.sql.*;
public class ConnectDB {
	public static Connection connect(){
//		String url="jdbc:mysql://localhost:3306/HTGQD?autoReconnect=true&useSSL=false&useUnicode=yes&characterEncoding=UTF-8";
//		String user="root";
//		String pass="";
		Connection connection = null;
		try {
//			Class.forName("com.mysql.jdbc.Driver");
			connection = DriverManager.getConnection(
					"jdbc:mysql://localhost:3306/HTGQD?autoReconnect=true&useSSL=false&useUnicode=yes&characterEncoding=UTF-8", "root", "");
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return connection;
	}
}
