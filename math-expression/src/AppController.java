import Model.MathExpressionCalculator;
import View.ConsoleView;

import java.util.Scanner;

public class AppController {
    private final Scanner scanner = new Scanner(System.in);

    private final MathExpressionCalculator calculator;
    private final ConsoleView view;

    public AppController(MathExpressionCalculator calculator, ConsoleView view) {
        this.calculator = calculator;
        this.view = view;
    }

    public void Run() {
        while (true) {
            System.out.print("Enter math expression: ");
            String expression = this.scanner.nextLine();

            try {
                double result = this.calculator.calculate(expression);
                view.displayValue("Result: " + result);
            }
            catch (Exception e) {
                view.displayException(e);
            }

            System.out.println();
        }
    }
}
