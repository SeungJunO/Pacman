import java.util.Scanner;

public class Season {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Input month (1~12) >>  ");
        int n = sc.nextInt();
        
        String season;

        if (n==12||n==1||n==2){
            season = "Winter";
        }else if (n>=3 && n<=5){
            season = "Spring";
        }else if (n>=6&&n<=8){
            season = "Summer";
        }else if (n>=9&&n<=11){
            season = "Autumn";
        }else{
            season = "Invalid";
        }
        System.out.println("Season: "+season);

    
        sc.close();
    }
}
