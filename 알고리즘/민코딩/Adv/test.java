import java.util.Scanner;

public class Solution {

    static int max;
    static int[][] arr;
    static int N, L;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 1; t <= T; t++) {
            N = sc.nextInt();
            L = sc.nextInt();

            arr = new int[N][2];

            for (int i = 0; i < N; i++) {
                arr[i][0] = sc.nextInt();
                arr[i][1] = sc.nextInt();
            }

            max = Integer.MIN_VALUE;
            Ham(0, 0, 0);

            System.out.printf("#%d %d\n",t,max);
        }
    }

    public static void Ham(int n, int sumK, int sumS) {
        if (sumK > L) return;

        if (n == N) {
            max = Math.max(max, sumS);
            return;
        }

        Ham(n+1, sumK, sumS);
        Ham(n+1, sumK + arr[n][1], sumS + arr[n][0]);
    }
}