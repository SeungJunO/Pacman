import java.util.Scanner;

public class same {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Input 2-digit integer(10-99) >> ");
        int number = sc.nextInt();

        int a = number / 10;
        int b = number % 10;

        if (a==b){
            System.out.println("Yes! The digits of 10 and the digits of 1 are the same.");

        }
        else{
            System.out.println("No! The digits of 10 and the digits of 1 are different.");

        }






        sc.close();
    }
}
