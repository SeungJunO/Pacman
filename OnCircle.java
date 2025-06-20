import java.util.Scanner;

public class OnCircle {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Input center and radius of 1st circle >> ");
        double x1 = sc.nextDouble();
        double y1 = sc.nextDouble();
        double r1 = sc.nextDouble();
        System.out.print("Input center and radius of 2nd circle >> ");
        double x2 = sc.nextDouble();
        double y2 = sc.nextDouble();
        double r2 = sc.nextDouble();
        double result = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
        if(result <=r1+r2){
            System.out.println("Two circles are overlapped");
        }else{
            System.out.println("Two circles are not overlapped");
        }


        sc.close();
    }
    
}
