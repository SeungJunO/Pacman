import java.util.Scanner;


public class starprint {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Input integer >> ");
        int n = sc.nextInt();
        int count;
        for(int i =n;i>=0;i--){
            for(count = 1;count <= i; count++){
                System.out.print("*");
            }
            System.out.println();
        }

        
        sc.close();
    }

}
