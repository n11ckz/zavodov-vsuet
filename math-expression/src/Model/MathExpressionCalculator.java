package Model;

import java.util.*;

public class MathExpressionCalculator {
    private final MathExpressionParser parser = new MathExpressionParser();

    public double calculate(String expression) {
        Stack<Double> result = new Stack<>();
        List<String> tokens = this.parser.getTokens(expression);

        for (int i = 0; i < tokens.size(); i++) {
            String token = tokens.get(i);

            if (isNumber(token)) {
                double number = Double.parseDouble(token);
                result.push(number);
            }
            else {
                double rightOperand = result.pop();
                double leftOperand = result.pop();
                result.push(applyOperator(token.charAt(0), leftOperand, rightOperand));
            }
        }

        return result.pop();
    }

    private double applyOperator(char operator, double leftOperand, double rightOperand) {
        switch (operator) {
            case '+':
                return leftOperand + rightOperand;
            case '-':
                return leftOperand - rightOperand;
            case '*':
                return leftOperand * rightOperand;
            case '/':
                if (rightOperand == 0) {
                    throw new ArithmeticException("Division by zero");
                }

                return leftOperand / rightOperand;
            case '%':
                if (rightOperand == 0) {
                    throw new ArithmeticException("Division by zero");
                }

                return leftOperand % rightOperand;
            case '^':
                return Math.pow(leftOperand, rightOperand);
            default:
                throw new IllegalArgumentException("Unknown operator: " + operator);
        }
    }

    private boolean isNumber(String number) {
        try {
            Double.parseDouble(number);
            return true;
        }
        catch (NumberFormatException exception) {
            return false;
        }
    }
}
