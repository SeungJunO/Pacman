import java.util.Scanner;

public class Circle{
  int radius;

  public Circle(int radius){
    this.radius = radius;
  }

  public int getRadius(){
    return radius;
  }

  public static void main(String[] args){
    Circle[] c;
    c = new Circle[5];

    for(int i=0;i<5;i++ ){
      c[i] = new Circle(i);
      System.out.println(c[i].getRadius());
    }
  }
}