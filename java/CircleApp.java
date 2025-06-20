import java.util.Scanner;


class Circle{
    public double radius;

    public double getArea(){
        double area = 3.14*radius*radius;
        return area;
    }
}

public class CircleApp{
    public static void main(String[] args){
        Circle c = new Circle();
        Scanner sc = new Scanner(System.in);

        c.radius = sc.nextDouble();
        System.out.println(c.getArea());
        sc.close();
    }
}


