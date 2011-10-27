public class Euler_108 {

    public static void main (String [] args) {
	
	boolean found_sol = false;

	long n = 4;

	while (!found_sol) {
	    int sols = 0;

	    for (long x = 2*n; x > n; x--) {
		double y = (n*x) / (double)(x - n);
		if (y == (long)y) 
		    sols++;
	    }

	    if (sols > 1000) {
		found_sol = true;
	    }

	    n++;
	}

	System.out.println("Solution: " + n);

    }
    
}