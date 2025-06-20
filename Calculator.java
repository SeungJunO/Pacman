import java.util.Scanner;

public class Calculator {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter >> ");
        double a = sc.nextDouble();
        String op = sc.next();      
        double b = sc.nextDouble();

        switch (op) {
            case "+":
                System.out.println(a+" + "+b+" = "+(a+b));
                break;
            case "-":
                System.out.println(a+" - "+b+" = "+(a-b));
                break;
            case "*":
                System.out.println(a+" * "+b+" = "+(a*b));
                break;
            case "/":
                if (b == 0) {
                    System.out.println("Divide by 0 error");
                } else {
                    System.out.println(a+" / "+b+" = "+(a/b));
                }
                break;
            default:
                System.out.println("Invalid operator");
        }

        sc.close();
    }
    
}
