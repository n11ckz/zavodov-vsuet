package Model;

import java.util.*;

public class MathExpressionParser {
    public List<String> getTokens(String expression) {
        List<String> tokens = new ArrayList<>();
        Stack<Character> operators = new Stack<>();
        StringBuilder digitSequence = new StringBuilder();

        for (int i = 0; i < expression.length(); i++) {
            char symbol = expression.charAt(i);

            if (isDigit(symbol)) {
                digitSequence.append(symbol);
                continue;
            }

            tryCompleteDigitSequence(digitSequence, tokens);

            if (symbol == '(') {
                operators.push(symbol);
            }
            else if (symbol == ')') {
                while (!operators.isEmpty() && operators.peek() != '(') {
                    String operator = operators.pop().toString();
                    tokens.add(operator);
                }

                operators.pop();
            }
            else if (isOperator(symbol)) {
                if (symbol == '/' && i + 1 < expression.length() && expression.charAt(i + 1) == '/') {
                    symbol = '%';
                    i++;
                }

                while (!operators.isEmpty() && getOperatorPriority(operators.peek()) >= getOperatorPriority(symbol)) {
                    String operator = operators.pop().toString();
                    tokens.add(operator);
                }

                operators.push(symbol);
            }
        }

        tryCompleteDigitSequence(digitSequence, tokens);

        while (!operators.isEmpty()) {
            String operator = operators.pop().toString();
            tokens.add(operator);
        }

        return tokens;
    }

    private void tryCompleteDigitSequence(StringBuilder sequence, List<String> tokens) {
        if (!sequence.isEmpty()) {
            tokens.add(sequence.toString());
            sequence.setLength(0);
        }
    }

    private boolean isDigit(char symbol) {
        return Character.isDigit(symbol) || symbol == '.';
    }

    private boolean isOperator(char symbol) {
        return symbol == '+' || symbol == '-' || symbol == '*' || symbol == '/' || symbol == '%' || symbol == '^';
    }

    private int getOperatorPriority(char operator) {
        return switch (operator) {
            case '+', '-' -> 1;
            case '*', '/', '%' -> 2;
            case '^' -> 3;
            default -> -1;
        };
    }
}
