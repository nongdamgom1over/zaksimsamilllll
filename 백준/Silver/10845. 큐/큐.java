
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static int[] queue = new int[10001]; // 큐 배열
	static int first = 0;
	static int last = 0;
	
   public static void main(String[] args) throws IOException{
	   BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	   int N = Integer.parseInt(br.readLine());
	   StringBuilder sb = new StringBuilder();
	   
	   for(int i=0; i<N; i++) {
		   StringTokenizer st = new StringTokenizer(br.readLine());
		   String command = st.nextToken();
		   
		   switch(command) {
		   case "push":
			   push(Integer.parseInt(st.nextToken()));
			   break;
		   case "pop":
			   sb.append(pop()).append("\n");
			   break;
		   case "size":
			   sb.append(size()).append("\n");
			   break;
		   case "empty":
			   sb.append(empty()).append("\n");
			   break;  
		   case "front":
			   sb.append(front()).append("\n");
			   break;  
		   case "back":
			   sb.append(back()).append("\n");
			   break;    
		   }
	   }
	   System.out.println(sb);
	   
   }

private static int back() {
	// TODO Auto-generated method stub
	if (first == last) {
		return -1;
	}
	else {
		int res = queue[last-1];
		return res;
	}
}

private static int front() {
	// TODO Auto-generated method stub
	if (first == last) {
		return -1;
	}
	else {
		int res = queue[first];
		return res;
	}
}

private static int empty() {
	// TODO Auto-generated method stub
	if (first == last) {
		return 1;
	}
	else {
		return 0;
	}
}

private static int size() {
	// TODO Auto-generated method stub
	return last-first;
}

private static int pop() {
	// TODO Auto-generated method stub
	if (last == first) {
		return -1;
	}
	else {
		int res = queue[first];
		first++;
		return res;
	}
}

private static void push(int num) {
	// TODO Auto-generated method stub
	queue[last] = num;
	last++;
}

}
