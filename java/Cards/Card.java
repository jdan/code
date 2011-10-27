import java.util.Random;

public class Card {

    private int id;
    private Random r;
    private String [] nums = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
    private String [] suits = {"S", "H", "D", "C"};

    public Card() {
        r = new Random();
        id = r.nextInt(52);
    }
    
    public int getID() {
        return id;
    }
    
    public String getNum() {
        return nums[this.id / 4];
    }
    
    public String getSuit() {
        return suits[this.id % 4];
    }
    
    public int getCount() {
        return this.id / 4;
    }
    
    public int compareTo (Card c) {
        if (this.getCount() == c.getCount()) {
            return 0;
        } else if (this.getCount() > c.getCount()) {
            return 1;
        } else {
            return 0;
        }
    }
    
    public String toString() {
        return this.getNum() + this.getSuit();
    }
}