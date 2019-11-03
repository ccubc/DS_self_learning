package assignment3;
import java.util.ArrayList;
import exceptions.EmptyCollectionException;
public class ArrayListStack<T> implements StackADT<T> 
{
	ArrayList<T> stack = new ArrayList<T>();
	/*
	 * Inserts a specified element to the top of the stack
	 */
	@Override
	public void push(T element) {
		stack.add(0, element);
	}
	
	/*
	 * Removes the element on the top from the stack
	 */
	@Override
	public T pop() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("stack");
		T result = stack.remove(0);
		return result;
	}
	/*
	 * Returns the element on the top but not removing from stack
	 */
	@Override
	public T peek() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("stack");
		return stack.get(0);
	}
	
	/* 
	 * Returns true is the stack is empty, false otherwise.
	 */
	@Override
	public boolean isEmpty() {
		return stack.isEmpty();
	}

	/*
	 * Returns size of the stack
	 */
	@Override
	public int size() {
		return stack.size();
	}
	
	public void display(){
		System.out.println(" " + stack);
	}
	
	public static void main(String args[]){
		ArrayListStack<String> testStack = new ArrayListStack<String>();
		/*
		 * if running either of the line of code below, will throw EmptyCollectionException
		testStack.peak();
		testStack.pop();
		*/
		System.out.println("Is the Stack empty?");
		System.out.println(testStack.isEmpty());
		testStack.push("1");
		testStack.push("2");
		testStack.push("3");
		testStack.push("4");
		System.out.println("After pushing 4 elements, the Stack is:");
		testStack.display();
		
		System.out.println("Is the Stack empty?");
		System.out.println(testStack.isEmpty());
	    System.out.println("After popping the top element, the Stack is");
	    testStack.pop();
	    testStack.display();	    
	    System.out.println("current size of the stack is "+ testStack.size());
	    System.out.println("peek operation returns: " + testStack.peek());
	    System.out.println("The current Stack is:");
	    testStack.display();
	}

}
