package test;

public class h2 {
    public static void main(String[] args) {
        try {
            System.out.println(1 / 0); //Line 1
        }
        catch (Exception ex) {
            System.out.println("Hello"); //Line 2
        }
        finally {
            System.out.println("Linktech"); //Line 3
        }
    }


}
