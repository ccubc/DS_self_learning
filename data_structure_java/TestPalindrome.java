import java.util.Scanner;
public class TestPalindrome {

	public static void main(String[] args)
	{
	String word;
	Scanner scan =new Scanner(System.in);
	System.out.println("Please input a word to check whether it is Palindrome");
	word = scan.nextLine();
	System.out.println("is Palindrome?" + word);
	System.out.println(isPalindrome(word));
	
	}
	
	public static Boolean isPalindrome(String str)
	{
		int strlen = str.length();
		ArrayStack<String> stack = new ArrayStack<String>();
		LinkedQueue<String> queue = new LinkedQueue<String>();
		String s = new String();
		for (int i = 0; i<strlen; i++) {
			s = "" + str.charAt(i);
			System.out.println(s);
			queue.enqueue(s);
			stack.push(s);
		}
		for (int i=0; i<strlen; i++) {
			if (!queue.dequeue().equals(stack.pop()))
				return false;
				}
		return true;
	}
}
