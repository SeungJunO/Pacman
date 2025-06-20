import java.util.Scanner;

public class Clap {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        
        
        while(true){

            System.out.print("Input integer(1~99) >> ");
            int a = sc.nextInt();
            int tennumber = a / 10;
            int onenumber = a%10;
            boolean isclap = false;
            
            if (tennumber == 3 ||tennumber == 6||tennumber == 9){
                System.out.print("Clap");
                isclap = true;
    
                if (onenumber == 3 ||onenumber == 6||onenumber == 9) {
                    System.out.print(", Clap");
                }
            }else{
                if (onenumber == 3 ||onenumber == 6||onenumber == 9) {
                    System.out.print("Clap");
                    isclap = true;
                }
            }
            if(!isclap) break;
            System.out.println();

        }
        

        

        
         sc.close();
    }
}
