import java.util.*;

public class Main {
    public static int[] stack; // 스택 배열
    public static int size = 0; // 현재 스택의 크기

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int N = sc.nextInt(); // 명령어 반복 횟수
        stack = new int[N]; // 스택 배열 크기 설정

        for (int i = 0; i < N; i++) {
            String command = sc.next();

            switch (command) {
                case "push":
                    push(sc.nextInt());
                    break;

                case "pop":
                    sb.append(pop()).append('\n');
                    break;

                case "size":
                    sb.append(size()).append('\n');
                    break;

                case "empty":
                    sb.append(empty()).append('\n');
                    break;

                case "top":
                    sb.append(top()).append('\n');
                    break;
            }
        }
        System.out.print(sb);
    }

    private static void push(int num) {
        stack[size] = num;
        size++;
    }

    private static int pop() {
        if (size == 0) {
            return -1;
        } else {
            size--;
            return stack[size];
        }
    }

    private static int size() {
        return size;
    }

    private static int empty() {
        return size == 0 ? 1 : 0;
    }

    private static int top() {
        if (size == 0) {
            return -1;
        } else {
            return stack[size - 1];
        }
    }
}
