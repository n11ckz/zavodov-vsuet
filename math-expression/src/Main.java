import Model.MathExpressionCalculator;
import View.ConsoleView;

public class Main {
    public static void main(String[] args) {
        MathExpressionCalculator calculator = new MathExpressionCalculator();
        ConsoleView view = new ConsoleView();

        AppController appController = new AppController(calculator, view);
        appController.Run();
    }
}
