import java.util.*;

class LinearSearchArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        System.out.println("Enter the elements of the array");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }
        int result = searchArray(arr, 19);
        System.out.print("The targeted element is found at " + result);
        sc.close();
    }

    static int searchArray(int[] arr, int target) {
        if (arr.length == 0)
            return -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target) {
                return i;

            }
        }
        return -1;
    }
}
