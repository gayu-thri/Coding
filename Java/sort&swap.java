import java.util.Scanner;
public class Lilys_homework {
    private static void swap(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
 
    private static void reverse(int[] a) {
        int n = a.length;
        for (int i=0; i<n/2; i++) {
            swap(a,i,n-i-1);
        }
    }
 
    private static int solve(int[] a, int n, int[] sorted) {
        int ans = 0;
        Map<Integer, Integer> value2index = new HashMap<Integer, Integer>();
        for (int i = 0; i < n; i++) {
            value2index.put(a[i], i);
        }
 
        for (int i = 0; i < n; i++) {
            if (a[i] != sorted[i]) {
                // At index i there must be value sorted[i]
 
                // Find the position of value sorted[i] in the input array
                int position = value2index.get(sorted[i]);
 
                // Swap sorted[i] with a[i]
                swap(a, i, position);
 
                // Update the position of a[position] in the value2index map
                value2index.put(a[position], position);
 
                // Increment swap count
                ans++;
            }
        }
 
        return ans;
    }
 
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream(System.getProperty("user.home") + "/" + "in.txt"));
 
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
 
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
 
        int[] sorted = Arrays.copyOf(a, a.length);
        Arrays.sort(sorted);
        
        int ans = solve(Arrays.copyOf(a, a.length), n, sorted);
        reverse(sorted);
        int ansR = solve(a, n, sorted);
 
        System.out.println(Math.min(ans,ansR));
    }
