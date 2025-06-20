import java.util.Scanner;

public class IsRectangle {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Input (x,y) >> ");
        int x = sc.nextInt();
        int y = sc.nextInt();
        if(x<=200&&x>=100&&y>=100&&y<=200){
            System.out.println("Point ("+x+", "+y+") is in the rectangle.");
        }else{
            System.out.println("Point ("+x+", "+y+") is not in the rectangle.");
        }
    
         sc.close();
    }
}
