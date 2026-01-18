package Array;

import java.util.*;

public class ReverseArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        System.out.println("Enter the elements into the array");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.print("Array elements are: ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        System.out.print("Reversed Array: ");
        int[] resersedArray = reverse(arr, 0, arr.length - 1);
        for (int num : resersedArray) {
            System.out.print(num + " ");
        }
        sc.close();
    }

    static int[] reverse(int[] arr, int start, int end) {
        while (start < end) {
            SwapArrayEle.swap(arr, start, end);
            start++;
            end--;
        }
        return arr;
    }
}
