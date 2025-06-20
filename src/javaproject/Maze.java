package javaproject;

import java.awt.*;

public class Maze {
    private int[][] map;
    private int width;
    private int height;
    private int totalFood;

    public Maze(Difficulty difficulty) {
        switch (difficulty) {
            case EASY:
                map = getEasyMap();
                break;
            case NORMAL:
                map = getNormalMap();
                break;
            case HARD:
                map = getHardMap();
                break;
            default:
                map = getNormalMap(); // fallback
        }

        width = map[0].length;
        height = map.length;

        totalFood = 0;
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[i].length; j++) {
                if (map[i][j] == 0) {
                    map[i][j] = 2;
                    totalFood++;
                }
            }
        }

    }

    // EASY
    private int[][] getEasyMap() {
        return new int[][] {
                { 1, 1, 1, 1, 1, 1 },
                { 1, 0, 0, 0, 0, 1 },
                { 1, 0, 1, 1, 0, 1 },
                { 1, 0, 0, 1, 0, 1 },
                { 1, 1, 0, 0, 0, 1 },
                { 1, 1, 1, 1, 1, 1 }
        };
    }

    // NORMAL
    private int[][] getNormalMap() {
        return new int[][] {
                { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
                { 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1 },
                { 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1 },
                { 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
                { 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
                { 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 },
                { 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1 },
                { 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1 },
                { 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1 },
                { 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1 },
                { 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1 },
                { 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
                { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 }
        };
    }

    // HARD
    private int[][] getHardMap() {
        return new int[][] {
                { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
                { 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1 },
                { 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1 },
                { 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1 },
                { 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 },
                { 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1 },
                { 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1 },
                { 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1 },
                { 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1 },
                { 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1 },
                { 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1 },
                { 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1 },
                { 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1 },
                { 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 },
                { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 }
        };
    }

    public boolean isWalkable(int x, int y) {
        if (x < 0 || y < 0 || x >= width || y >= height)
            return false;
        return map[y][x] != 1;
    }

    public boolean isWall(int x, int y) {
        if (x < 0 || y < 0 || x >= width || y >= height)
            return true;
        return map[y][x] == 1; // 1이면 벽
    }

    public int getWidth() {
        return map[0].length;
    }

    public int getHeight() {
        return map.length;
    }

    public int getMonsterStartX() {
        return width - 2;
    }

    public int getMonsterStartY() {
        return height - 2;
    }

    public void draw(Graphics g) {
        int tileSize = 30;

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int value = map[y][x];

                if (value == 1) {
                    // 벽
                    g.setColor(Color.BLUE);
                    g.fillRect(x * tileSize, y * tileSize, tileSize, tileSize);
                } else {
                    // 바닥
                    g.setColor(Color.BLACK);
                    g.fillRect(x * tileSize, y * tileSize, tileSize, tileSize);

                    if (value == 2) {
                        // 먹이
                        g.setColor(Color.YELLOW);
                        g.fillOval(
                                x * tileSize + tileSize / 4,
                                y * tileSize + tileSize / 4,
                                tileSize / 2,
                                tileSize / 2);
                    }
                }
            }
        }
    }

    public void eatFood(int x, int y) {
        if (map[y][x] == 2) {
            map[y][x] = 0;
            totalFood--;
        }
    }

    public boolean isAllFoodEaten() {
        return totalFood == 0;
    }

    // getter for map if needed
    public int[][] getMap() {
        return map;
    }

    public int getRows() {
        return height;
    }

}
