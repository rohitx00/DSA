import java.util.*;

class LinearSearchString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the name: ");
        String str = sc.next();
        str = str.toLowerCase();
        System.out.print("Enter the character you want to search: ");
        char c = sc.next().charAt(0);
        char covertedCharacter = Character.toLowerCase(c);

        boolean result = search(str, covertedCharacter);
        if (result) {
            System.out.println("Character is present in the Name.");
        } else {
            System.out.println("Character is not present in the Name.");
        }
        sc.close();
    }

    static boolean search(String str, char c) {
        if (str.length() == 0)
            return false;
        for (char characters : str.toCharArray()) {
            if (characters == c)
                return true;
        }
        return false;
    }

}