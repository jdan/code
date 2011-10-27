
/**
 * Write a description of class Iterate here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Iterate
{
    public static void main() {
        long i = 0;
        int max_steps = 0, steps = 0, max_stepper = 0;
        for (int n = 2; n <= 1000000; n++) {
            i = (long) n;
            steps = 0;
            while (i != (long) 1) {
                if (i % 2 == 0) {
                    i = i / 2;
                } else {
                    i = 3 * i + 1;
                }
                steps += 1;
            }
            if (steps > max_steps) {
                max_steps = steps;
                max_stepper = n;
            }
            System.out.println(n + ": " + steps);
        }
        System.out.println("Max: " + max_steps + " with " + max_stepper);
    }
}
