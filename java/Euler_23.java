import java.util.ArrayList;

public class Euler_23 {

    static ArrayList<Integer> a;
    
    public static void main (String [] args) {
	a = new ArrayList<Integer>();
	// make an arraylist of abundant numbers
	for (int i = 2; i <= 28123; i += 2) 
	    if (isAbundant(i)) a.add(i);

	int t = 0;
	int o_index = 0;
	
	for (int n = 25; n <= 28123; n++) {
	    System.out.println(n);
	    if (a.get(o_index) < n) {
		o_index++;
		while (a.get(o_index) < n) 
		    o_index++;
		o_index--;
	    }

	    int index = o_index;
	    
	    boolean canBeMade = false;
	    while (index >= 0) {
		if (a.indexOf(n - a.get(index).intValue()) > -1) {
		    canBeMade = true;
		    break;
		}

		index--;
	    }

	    if (!canBeMade) t += n;
	}

	t += (23*23 + 23) / 2;  // add the numbers 1 through 23

	System.out.println("Answer: " + t);
    }

    public static boolean isAbundant(int n) {
	int total = 0;	
	for (int i = 1; i < Math.floor(Math.sqrt(n)) + 1; i++) {
	    if (n % i == 0) {
		total += i;
		if (i != n/i) total += n / i;
	    }
	}

	return total > n;
    }

}
