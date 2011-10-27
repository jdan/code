import java.util.*;

public class Main
{
	static Scanner sc;
	
	public static void main (String [] args) {
		sc = new Scanner(System.in);
		
		int trials = sc.nextInt();
		int c;
		String num;
		
		for (int i = 0; i < trials; i++) {
			c = sc.nextInt() + 1;
			num = c + "";
			while (!(num.equals(flip(num)))) {
				c++;
				num = c + "";
			}
			System.out.println(c);
		}
		
		sc.close();
	}
	
	public static String flip (String s) {
		String fin = "";
		for (int i = s.length() - 1; i >= 0; i--) {
			fin += s.charAt(i);
		}
		return fin;
	}
}