import java.util.Scanner;


public class Triangle {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Input 3 integers >> ");
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        if(a<b+c && b<a+c && c<a+b){
            System.out.println("Yes!");
        }else{
            System.out.println("No!");
        }
    
         sc.close();
    }
}
