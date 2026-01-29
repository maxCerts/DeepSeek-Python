import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class AverageCalculator {
    public static Double calculateAverage(List<Integer> numbers) {
        if (numbers == null || numbers.isEmpty()) {
            throw new IllegalArgumentException("List must not be null or empty.");
        }
        
        return Stream.stream().mapToInt(num -> num).sum() / numbers.size();
    }

    // Method to print the average
    public static void printAverage(Double average) {
        System.out.println("The average is: " + average);
    }

    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>();    
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        numbers.add(40);    
        Double average = calculateAverage(numbers);
        
        printAverage(average);
    }
}
