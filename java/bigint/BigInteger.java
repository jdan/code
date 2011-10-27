public class BigInteger {

    private int[] a;

    public BigInteger() {
	this(0);
    }

    private void spread() {
        for (int i = 0; i < a.length; i++) {
	    if (a[i] > 9) {
		a[i + 1] += a[i] / 10;
		a[i] %= 10;
	    }
	}
    }

    public BigInteger(int n) {
	a = new int[1000];
	a[0] = n;
	spread();
    }

    public void add(int n) {
	a[0] += n;
	spread();
    }

    public void multiply(int n) {
	for (int i = 0; i < a.length; i++) {
	    a[i] *= n;
	}
	spread();
    }

    public String toString() {
	int i = a.length - 1;
	do {
	    i--;
	} while (a[i] == 0);

	String s = "";
	while (i >= 0) {
	    s += Integer.toString(a[i]);
	    i--;
	}

	return s;
    }
}