public class Poker {
    
    public static void main(String [] args) {
        Hand h = new Hand(1);
        h.sort();
        for (int i = 0; i < 51; i++) {
            h.draw(1);
            h.sort();
            System.out.println(h.toString());
        }
    }   
    
}
