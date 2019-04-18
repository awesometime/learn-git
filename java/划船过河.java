/**
第五题：

题目描述：
有n个人要过河，但是河边只有一艘船；
船每次最多坐三个人，每个人单独坐船过河的时间为a[i]；
两个人或者三个人一起坐船时，过河时间为他们所有人中的最长过河时间；
为了安全起见，要求每次至少有两个人才能过河。
问最短需要多少时间，才能把所有人送过河。

输入描述：
第一行是整数n，表示测试样例格式
每个测试样例的第一行是一个正整数n，表示参加过河的人数（2<=n<100000）
第二行是n个正整数a[i](0<a[i]<100000)，表示n个人单独过河的时间；

输出描述
对每个测试样例，输出应该准备的最少的过河时间

示例1：
输入：
2
2
1 2
4 
1 1 1 1

输出
2
3
*/


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] res = new int[n];
		for(int i=0;i<n;i++) {
			int k = Integer.parseInt(br.readLine());
			String p = br.readLine();
			String[] s1 = p.trim().split(" ");
			int[] nums = new int[k];
			for(int j=0;j<k;j++)
				nums[j]= new Integer(s1[j]);
			res[i] = method(k,nums);
		}
		for(int i=0;i<n;i++)
			System.out.println(res[i]);
		
	}
	public static int method(int k,int[] nums) {
		int time=0;
		Arrays.sort(nums);
		if(k<=3)
			return nums[k-1];
		else
			time+=nums[2];       // 3人过河 时间取最大的那个人nums[2]
		for(int i=3;i<k;i++) {
			time+=nums[1];       // 返回两个人 时间最大为nums[1]  返回2个人划船很狗 有什么意义
			time+=nums[i];       // 回来的两人 再拉一个人
		}
		
		return time;
	}

}
