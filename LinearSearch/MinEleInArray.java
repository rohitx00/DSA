import java.util.*;

public class MinEleInArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        System.out.print("Enter the elements into the Array: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int min = minValue(arr);
        System.out.println("The minimum value in the array is: " + min);
        sc.close();

    }

    static int minValue(int[] arr) {
        int min = Integer.MAX_VALUE;
        if (arr.length == 0) {
            System.out.println("Array is empty");
        }
        for (int num : arr) {
            if (num < min) {
                min = num;
            }
        }
        return min;
    }
}
