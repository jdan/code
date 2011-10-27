
/**
 * Write a description of class AllPrimes here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class AllPrimes
{
   public static void main() {
       double total = 0.0;
       for (int i = 2; i < 2000000; i++) {
           if (isPrime(i)) {
               total += (double) i;
               System.out.println(i + ": Prime");
            } else {
                System.out.println(i);
            }
        }
        System.out.println(total);
    }
    public static boolean isPrime(int n) {
        if (n % 2 == 0) {
            return false;
        }
        for (int i = 3; i <= n/2; i+=2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
