import java.util.*;

class LinearSearchStringInRange {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the name: ");
        String str = sc.next();
        str = str.toLowerCase();
        System.out.print("Enter the character you want to search: ");
        char c = sc.next().charAt(0);
        char covertedCharacter = Character.toLowerCase(c);

        boolean result = search(str, covertedCharacter, 1, 3);
        if (result) {
            System.out.println("Character is present in the Name.");
        } else {
            System.out.println("Character is not present in the Name.");
        }
        sc.close();
    }

    static boolean search(String str, char c, int start, int end) {
        if (str.length() == 0)
            return false;

        for(int i = start; i <= end; i++ ){
            if(str.charAt(i) == c)
                return true;
        }
        return false;
    }

}