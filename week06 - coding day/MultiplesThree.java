
import java.util.Scanner;

public class MultiplesThree {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numbers = new int[10];
        System.out.print("Input 10 positive integers >>");
        for(int i = 0;i<10;i++){
            numbers[i] = sc.nextInt();

        }
        for(int j = 0;j<10;j++){
            if(numbers[j] %3 == 0){
                System.out.print(numbers[j]+" ");
                
            }
        }


       sc.close();

    }
}
