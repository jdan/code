import java.util.*;
import java.lang.Math;

public class Main
{
	static Scanner sc;
	static ArrayList<Integer> al;
	
	public static void main (String [] args) {
		sc = new Scanner(System.in);
		int trials = sc.nextInt();
		int low, high;
		
		al = new ArrayList<Integer>;
		al.add(2);
		al.add(3);
		al.add(5);
		
		for (int i = 0; i < trials; i++) {
			low = sc.nextInt();
			high = sc.nextInt();
			for (int k = low; k <= high; k++) {
				if (isPrime(k)) {
					System.out.println(k);
				}
			}
			System.out.println();
		}
		
		sc.close();
	}
	
	public static boolean isPrime (int n) {
		if (n == 2) {
			return true;
		} else if (n % 2 == 0) {
			return false;
		} else {
		    for (int c = 3; c <= Math.sqrt(n); c += 2) {
				if (n % c == 0) {
					return false;
				}
			}
			return true;
		}
	}
}