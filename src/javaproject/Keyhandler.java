package javaproject;

import java.awt.event.*;

import javaproject.Character;
import javaproject.Maze;

public class Keyhandler extends KeyAdapter {
    private Character character; // 조작할 팩맨 객체
    private Maze maze; // 미로 정보 저장 필드

    public Keyhandler(Character character, Maze maze) {
        this.character = character;
        this.maze = maze;
    } // 외부에서 팩맨과 미로 객체를 받아와 필드에 저장
      // 이렇게 해야 팩맨을 이동시키거나 벽인지 확인할 수 있음

    @Override
    public void keyPressed(KeyEvent e) {
        switch (e.getKeyCode()) { // 키보드 키가 눌렸을 때 호출 되는 메서드
            case KeyEvent.VK_UP:
                character.move(0, -1, maze);
                break;
            case KeyEvent.VK_DOWN:
                character.move(0, 1, maze);
                break;
            case KeyEvent.VK_LEFT:
                character.move(-1, 0, maze);
                break;
            case KeyEvent.VK_RIGHT:
                character.move(1, 0, maze);
                break;
        } // 각각의 방향키에 대해 팩맨을 한 칸씩 이동시킴
    }
}
