package javaproject;

import java.awt.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Monster implements Runnable {
    private int x, y;
    private boolean running = true;
    private Maze maze;
    private Random rand = new Random();
    private int currentDir; // 0: up, 1: down, 2: left, 3: right

    public Monster(int startX, int startY, Maze maze) {
        this.x = startX;
        this.y = startY;
        this.maze = maze;
        this.currentDir = rand.nextInt(4); // 초기 방향 설정
    }

    public void stop() {
        running = false;
    }

    public void moveSmart() {
        int[] dx = { 0, 0, -1, 1 };
        int[] dy = { -1, 1, 0, 0 };

        int newX = x + dx[currentDir];
        int newY = y + dy[currentDir];

        if (maze.isWalkable(newX, newY)) {
            x = newX;
            y = newY;
        } else {
            // 다른 방향 탐색
            List<Integer> directions = new ArrayList<>();
            for (int i = 0; i < 4; i++) {
                if (i == currentDir)
                    continue; // 현재 방향 제외
                int tx = x + dx[i];
                int ty = y + dy[i];
                if (maze.isWalkable(tx, ty)) {
                    directions.add(i);
                }
            }
            if (!directions.isEmpty()) {
                currentDir = directions.get(rand.nextInt(directions.size()));
                x += dx[currentDir];
                y += dy[currentDir];
            }
        }
    }

    @Override
    public void run() {
        while (running) {
            moveSmart();
            try {
                Thread.sleep(300); // 0.3초마다 이동
            } catch (InterruptedException e) {
                break;
            }
        }
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void draw(Graphics g) {

        int tileSize = 30;
        g.setColor(Color.RED); // 또는 이미지로도 가능
        g.fillOval(x * tileSize, y * tileSize, tileSize, tileSize);
    }
}
