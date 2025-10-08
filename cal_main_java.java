import java.util.Scanner;

public class Calculator {
    public static double add(double a, double b) { return a + b; }
    public static double subtract(double a, double b) { return a - b; }
    public static double multiply(double a, double b) { return a * b; }
    public static double divide(double a, double b) { return b != 0 ? a / b : Double.POSITIVE_INFINITY; }
    public static double remainder(double a, double b) { return b != 0 ? a % b : Double.NaN; }
    public static double power(double a, double b) { return Math.pow(a, b); }
    public static double percentage(double a, double b) { return b != 0 ? (a / b) * 100 : Double.NaN; }

    public static double applyOp(double a, double b, char op) {
        switch (op) {
            case '+': return add(a, b);
            case '-': return subtract(a, b);
            case '*': return multiply(a, b);
            case '/': return divide(a, b);
            case '%': return remainder(a, b);
            case '^': return power(a, b);
            case 'p': return percentage(a, b);
            default: return Double.NaN;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double result;

        System.out.println("Operators: + - * / % ^ p (percentage)");
        System.out.print("Enter first number: ");
        result = sc.nextDouble();

        while (true) {
            try {
                System.out.print("Enter operator: ");
                char op = sc.next().charAt(0);

                System.out.print("Enter next number: ");
                double num = sc.nextDouble();

                result = applyOp(result, num, op);
                System.out.println("= " + result);
            } catch (Exception e) {
                System.out.println("Invalid input. Exiting.");
                break;
            }
        }

        sc.close();
    }
}
