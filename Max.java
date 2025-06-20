import java.util.Scanner;



public class Max {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Input 3 integers >> ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        if((a>b&&b>c) || (c>b&&b>a)){
            System.err.println("Middle number is "+ b);
        }else if((a>c&&c>b) || (b>c&&c>a)){
            System.out.println("Middle number is "+ c);
        }else{
            System.out.println("Middle number is "+ a);
        }



        
        sc.close();
    }
}
