import java.util.*;

public class MaxEleInArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        System.out.print("Enter the elements of the Array: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int value = maxValue(arr);
        System.out.print("The maximum value in the array is: " + value);
        sc.close();
    }

    static int maxValue(int[] arr) {
        int max = Integer.MIN_VALUE;
        if (arr.length == 0) {
            System.out.println("The Array is empty");
        }
        for (int num : arr) {
            if (num > max) {
                max = num;
            }
        }
        return max;
    }
}
