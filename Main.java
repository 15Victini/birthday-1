import java.util.Scanner;
public class Main{
    public static void Main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Your IP address is mine now :)");
        System.out.println("Enter your birthday (MM/DD/YYYY)");
        String bday = scan.next();
        if (bday.length != 10){
            System.out.println("You are a bozo");
        }
    }
}