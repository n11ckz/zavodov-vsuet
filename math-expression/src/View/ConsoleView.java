package View;

public class ConsoleView {
    public void displayValue(Object value) {
        System.out.println(value.toString());
    }

    public void displayException(Exception exception) {
        System.out.println("Error: " + exception.getMessage());
    }
}
