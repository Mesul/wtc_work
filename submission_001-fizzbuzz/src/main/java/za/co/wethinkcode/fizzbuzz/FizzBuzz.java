package za.co.wethinkcode.fizzbuzz;

import java.util.Arrays;

public class FizzBuzz {
    public String checkNumber(int number) {
        boolean divisibleBy3 = number % 3 == 0;
        boolean divisibleBy5 = number % 5 == 0;

        if ( divisibleBy3 && divisibleBy5 ) {
            return "FizzBuzz";
        }
        if ( divisibleBy3) {
            return "Fizz";
        }else if (divisibleBy5) {
            return "Buzz";
        }

        return String.valueOf(number);
    }

    public String countTo(int number) {
        String[] fizzbuzz = new String[number];

        for (int j=1; j <= number; j++) {
//            String numbs[] = [checkNumber(j];
            fizzbuzz[j-1] = checkNumber(j);
        }
        return Arrays.toString(fizzbuzz);
    }

    public static void main(String[] args) {
        FizzBuzz fizzBuzz = new FizzBuzz();
        System.out.println(fizzBuzz.countTo(15));
    }
}
