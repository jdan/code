public class Factorial {

    static BigInteger bi;

    public static void main(String [] args) {
	bi = new BigInteger(1);
	for (int i = 2; i <= Integer.parseInt(args[0]); i++) {
	    bi.multiply(i);
	}

	System.out.println(bi);
    }

}