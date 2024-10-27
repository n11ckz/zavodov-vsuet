package utils;

import java.util.Scanner;

public class Console {
    private static final int ITERATIONS = 100;

    private final Scanner scanner = new Scanner(System.in);

    public void write(String message) {
        System.out.print(message);
    }

    public void writeLine(String message) {
        System.out.println(message);
    }

    public String readLine() {
        return scanner.nextLine();
    }

    public void clear() {
        for (int i = 0; i < ITERATIONS; i++) {
            System.out.println();
        }
    }
}
