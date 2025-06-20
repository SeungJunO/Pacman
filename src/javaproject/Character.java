package javaproject;

import java.awt.*;

import javaproject.Monster;

public class Character {
    private int x, y; // 팩맨의 현재 위치를 저장하는 변수

    public Character(int x, int y) {
        this.x = x;
        this.y = y;
    }
    // 팩맨 객체 생성하면서 시작 위치 설정 생성자

    public void move(int dx, int dy, Maze maze) {
        int newX = x + dx;
        int newY = y + dy;
        if (!maze.isWall(newX, newY)) {
            x = newX;
            y = newY;
        }
    }

    // 팩맨을 움직이는 메서드
    // dx, dy: 이동 방향
    // if문안의 조건 : 이동하려는 위치가 벽인지 확인
    // 벽이 아니면 좌표를 업데이트 하여 팩맨이 이동

    public void draw(Graphics g) {
        g.setColor(Color.YELLOW); // 노란색으로 설정
        g.fillOval(x * 30, y * 30, 30, 30); // 원 모양으로 팩맨 그림 ( 그리기 좌표, 한칸의 크기가 20픽셀이라는 가정)
    }
    // 팩맨을 그리는 메서드

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }
    // 현재 팩맨의 위치를 외부에서 가져울 수 있도록 하는 Getter 메서드들
}
