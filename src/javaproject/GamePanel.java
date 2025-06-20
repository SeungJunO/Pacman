package javaproject;

import java.util.ArrayList;
import java.util.List;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GamePanel extends JPanel implements ActionListener {
    private Timer timer;
    private Character character;
    private List<Monster> monsters;
    private Maze maze;
    private List<Thread> monsterThreads;
    private boolean gameOver = false;
    private Difficulty difficulty;

    public GamePanel(Difficulty difficulty) {
        this.difficulty = difficulty;
        setFocusable(true);
        setBackground(Color.BLACK);

        // 난이도에 따라 미로 설정
        maze = new Maze(difficulty);
        character = new Character(1, 1);
        monsters = new ArrayList<>();
        monsterThreads = new ArrayList<>();

        addKeyListener(new Keyhandler(character, maze));
        requestFocusInWindow();

        int monsterCount = switch (difficulty) {
            case EASY -> 1;
            case NORMAL -> 2;
            case HARD -> 3;
        };

        for (int i = 0; i < monsterCount; i++) {
            int startX = maze.getMonsterStartX(); // 시작 위치 살짝씩 다르게
            int startY = maze.getMonsterStartY();

            if (difficulty == Difficulty.NORMAL) {
                if (i == 1) {
                    startX = maze.getMonsterStartX();
                    startY = maze.getMonsterStartY() - 6;
                }
            } else if (difficulty == Difficulty.HARD) {
                if (i == 1) {
                    startX = maze.getMonsterStartX();
                    startY = maze.getMonsterStartY() - 12;
                } else if (i == 2) {
                    startX = maze.getMonsterStartX() - 10;
                    startY = maze.getMonsterStartY() - 6;
                }
            }
            Monster monster = new Monster(startX, startY, maze);
            monsters.add(monster);

            Thread thread = new Thread(monster);
            monsterThreads.add(thread);
            thread.start();
        }

        timer = new Timer(1, this);
        timer.start();

        int tileSize = 24;
        int rows = maze.getHeight();
        int cols = maze.getWidth();
        setPreferredSize(new Dimension(tileSize * cols, tileSize * rows));

        SwingUtilities.invokeLater(() -> requestFocusInWindow());
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (!gameOver) {
            checkCollision();
            repaint();
        }
        // 캐릭터가 이동한 후
        maze.eatFood(character.getX(), character.getY());

        if (maze.isAllFoodEaten()) {
            gameOver = true;
            showSuccessMessage();
        }

    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        maze.draw(g);
        character.draw(g);
        for (Monster monster : monsters) {
            monster.draw(g);
        }

    }

    public void stopGame() {
        timer.stop();
        for (Monster monster : monsters) {
            monster.stop();
        }
        for (Thread thread : monsterThreads) {
            thread.interrupt();
        }
    }

    @Override
    public Dimension getPreferredSize() {
        int tileSize = 30;
        return new Dimension(maze.getWidth() * tileSize, maze.getHeight() * tileSize);
    }

    private void checkCollision() {
        for (Monster monster : monsters) {
            if (character.getX() == monster.getX() && character.getY() == monster.getY()) {
                stopGame();
                gameOver = true;

                int option = JOptionPane.showOptionDialog(
                        this,
                        "GAME OVER!\nDo you want to restart?",
                        "Game Over",
                        JOptionPane.YES_NO_OPTION,
                        JOptionPane.INFORMATION_MESSAGE,
                        null,
                        new String[] { "Restart", "Exit" },
                        "Restart");

                if (option == JOptionPane.YES_OPTION) {
                    MainFrame frame = (MainFrame) SwingUtilities.getWindowAncestor(this);
                    frame.setContentPane(new StartPanel(frame));
                    frame.setPreferredSize(new Dimension(800, 650));
                    frame.pack();
                    frame.setLocationRelativeTo(null);
                } else {
                    System.exit(0);
                }
                break;
            }
        }
    }

    private void showSuccessMessage() {
        int option = JOptionPane.showOptionDialog(
                this,
                "Congratulations! You won!\nDo you want to play again?",
                "Game Clear",
                JOptionPane.YES_NO_OPTION,
                JOptionPane.INFORMATION_MESSAGE,
                null,
                new String[] { "Restart", "Exit" },
                "Restart");

        if (option == JOptionPane.YES_OPTION) {
            stopGame(); // 이걸 먼저 호출해서 타이머와 쓰레드 완전 종료
            MainFrame frame = (MainFrame) SwingUtilities.getWindowAncestor(this);
            frame.setContentPane(new StartPanel(frame));
            frame.setPreferredSize(new Dimension(800, 650));
            frame.pack();
            frame.setLocationRelativeTo(null);
        } else {
            System.exit(0); // 게임 종료
        }

    }

}
