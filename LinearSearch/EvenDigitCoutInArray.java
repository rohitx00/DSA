import java.util.*;

public class EvenDigitCoutInArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[5];
        System.out.print("Enter the elements into the Array: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();

        }
        int ans = findNumber(arr);
        System.out.println("The number of even digits are: " + ans);
        sc.close();
    }

    static int findNumber(int[] arr) {
        int count = 0;
        for (int num : arr) {
            if (even(num)) {
                count++;
            }
        }
        return count;
    }

    static boolean even(int num) {
        int count = 0;

        while (num > 0) {
            num /= 10;
            count++;

        }
        if (count % 2 == 0) {
            return true;
        }

        return false;
    }
}
