import java.util.Scanner;

public class InCircle {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Input center point & radius >> ");
        double x = sc.nextDouble();
        double y = sc.nextDouble();
        double r = sc.nextDouble();
        System.out.print("Input point >> ");
        double px = sc.nextDouble();
        double py = sc.nextDouble();
        double result = Math.sqrt(Math.pow(x - px, 2) + Math.pow(y - py, 2));

        if(r>=result){
            System.out.println("Point ("+px+", "+py+") is in the circle.");
        }else{
            System.out.println("Point ("+px+", "+py+") is not in the circle.");
        }

    
         sc.close();
    }
}
