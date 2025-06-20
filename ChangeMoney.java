import java.util.Scanner;

public class ChangeMoney{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Input KRW >> ");

        double money = scanner.nextDouble();

        double changemoney = money / 1100;
        System.out.println(money+"KRW is "+ changemoney+"USD");



        scanner.close();
    }
}
