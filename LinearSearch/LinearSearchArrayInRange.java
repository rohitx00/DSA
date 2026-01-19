import java.util.*;

class LinearSearchArrayInRange {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        System.out.print("Enter the elements of the array: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.print("Enter the target element to search: ");
        int target = sc.nextInt();
        int result = searchArray(arr, target, 1, 3);
        System.out.print("The targeted element is found at " + result);
        sc.close();
    }

    static int searchArray(int[] arr, int target, int start, int end) {
        if (arr.length == 0)
            return -1;
        for (int i = start; i <= end; i++) {
            if (arr[i] == target) {
                return i;

            }
        }
        return -1;
    }
}