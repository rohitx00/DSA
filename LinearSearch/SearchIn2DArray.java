class SearchIn2DArray {
    public static void main(String[] args) {
        int[][] arr = {
                { 23, 89, 0 },
                { 22, 78, 12, 10 },
                { 65, 70, 32, 17 },
                { 14, 90 }
        };
        int target = 40;
        boolean result = searchElement(arr, target);
        if (result) {
            System.out.println("Element is present in the array");
        } else {
            System.out.println("Element is not present in the array");
        }
    }

    static boolean searchElement(int[][] arr, int target) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] == target)
                    return true;
            }
        }
        return false;
    }

}