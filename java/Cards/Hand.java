import java.util.Random;
import java.util.ArrayList;

public class Hand {

    private Random r;
    private Card [] hand;
    
    public Hand (int n) {
        r = new Random();
        ArrayList<Integer> used = new ArrayList<Integer>();
        hand = new Card[n];
        
        for (int i = 0; i < n; i++) {
            Card c = new Card();
            while (used.indexOf(c.getID()) > -1) {
                c = new Card();
            }
            used.add(c.getID());
            hand[i] = c;
        }
    }
    
    public String toString() {
        String fin = "";
        for (int i = 0; i < hand.length; i++) {
            fin += hand[i].toString() + " ";
        }
        return fin;
    }
    
    public void sort() {
        int sorts = 1;
        Card temp;
        while (sorts > 0) {
            sorts = 0;
            for (int i = 0; i < hand.length - 1; i++) {
                if (hand[i].compareTo(hand[i+1]) == 1) {
                    temp = hand[i+1];
                    hand[i+1] = hand[i];
                    hand[i] = temp;
                    sorts++;
                }
            }
        }
    }
    
    public boolean hasPair() {
        this.sort();
        for (int i = 0; i < hand.length - 1; i++) {
            if (hand[i].getNum() == hand[i+1].getNum()) {
                return true;
            }
        }
        return false;
    }
    
    public void draw(int n) {
        Card [] temp = new Card[hand.length + n];
        int i;
        for (i = 0; i < hand.length; i++) {
            temp[i] = hand[i];
        }
        for (; i < hand.length + n; i++) {
            boolean found = true;
            Card c = new Card();;
            while (found) {
                c = new Card();
                found = false;
                for (int k = 0; k < i; k++) {
                    if (temp[k].getID() == c.getID()) {
                        found = true;
                        break;
                    }
                }
            }
            
            temp[i] = c;
        }
        
       hand = temp;
    }
    
    private boolean find(Card c) {
        return find(c.getID());
    }
    
    private boolean find(int id) {
        for (int i = 0; i < hand.length; i++) {
            if (hand[i].getID() == id) { 
                return true;
            }
        } 
        return false;
    }

}
