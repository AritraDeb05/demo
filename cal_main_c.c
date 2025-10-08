#include <stdio.h>
#include <math.h>

double add(double a, double b) { return a + b; }
double subtract(double a, double b) { return a - b; }
double multiply(double a, double b) { return a * b; }
double divide(double a, double b) { return b != 0 ? a / b : INFINITY; }
double remainder_func(double a, double b) { return b != 0 ? fmod(a, b) : NAN; }
double power(double a, double b) { return pow(a, b); }
double percentage(double a, double b) { return b != 0 ? (a / b) * 100 : NAN; }

int main() {
    double result, num;
    char op;

    printf("Operators: + - * / %% ^ p (percentage)\n");
    printf("Enter first number: ");
    if (scanf("%lf", &result) != 1) return 1;

    while (1) {
        printf("Enter operator: ");
        if (scanf(" %c", &op) != 1) break;

        printf("Enter number: ");
        if (scanf("%lf", &num) != 1) break;

        switch (op) {
            case '+': result = add(result, num); break;
            case '-': result = subtract(result, num); break;
            case '*': result = multiply(result, num); break;
            case '/': result = divide(result, num); break;
            case '%': result = remainder_func(result, num); break;
            case '^': result = power(result, num); break;
            case 'p': result = percentage(result, num); break;
            default:
                printf("Unknown operator.\n");
                continue;
        }

        printf("= %.2lf\n", result);
    }

    printf("Calculator exited.\n");
    return 0;
}
