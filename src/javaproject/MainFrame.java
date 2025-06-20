package javaproject;

import javax.swing.*;
import java.awt.*;

public class MainFrame extends JFrame {
    public MainFrame() {
        setTitle("Pac-Man Clone");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(800, 650);
        setResizable(false);
        setLocationRelativeTo(null); // 화면 중앙 정렬

        showStartPanel();
        setVisible(true);
    }

    public void showStartPanel() {
        setContentPane(new StartPanel(this));
        revalidate();
        repaint();
    }

    public void showGamePanel(Difficulty difficulty) {
        GamePanel gamePanel = new GamePanel(difficulty);

        JPanel wrapper = new JPanel(new GridBagLayout());
        wrapper.setBackground(Color.BLACK);
        wrapper.add(gamePanel); // 중앙 정렬

        setContentPane(wrapper);
        revalidate();
        repaint();

        SwingUtilities.invokeLater(() -> {
            gamePanel.requestFocus();
            gamePanel.requestFocusInWindow();
        });
    }
}
