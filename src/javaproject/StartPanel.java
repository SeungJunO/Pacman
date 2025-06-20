package javaproject;

import javax.swing.*;
import java.awt.*;

public class StartPanel extends JPanel {
    private MainFrame frame;

    public StartPanel(MainFrame frame) {
        this.frame = frame;
        setLayout(new GridBagLayout());
        setBackground(Color.BLACK);

        JButton easyButton = new JButton("Easy");
        JButton normalButton = new JButton("Normal");
        JButton hardButton = new JButton("Hard");

        easyButton.addActionListener(e -> frame.showGamePanel(Difficulty.EASY));
        normalButton.addActionListener(e -> frame.showGamePanel(Difficulty.NORMAL));
        hardButton.addActionListener(e -> frame.showGamePanel(Difficulty.HARD));

        JPanel buttonPanel = new JPanel();
        buttonPanel.setOpaque(false);
        buttonPanel.add(easyButton);
        buttonPanel.add(normalButton);
        buttonPanel.add(hardButton);

        add(buttonPanel);
    }
}
