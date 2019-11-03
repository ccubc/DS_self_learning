package assignment3;
import java.util.LinkedList;
import exceptions.EmptyCollectionException;
public class LinkedListStack<T> implements StackADT<T> 
{
	LinkedList<T> stack = new LinkedList<T>();

	/*
	 * Push option: adds the specified element to the top of this stack.
	 */
	@Override
	public void push(T element) {
		stack.addFirst(element);
	}

	/*
	 * Pop option: removes the top element of the stack
	 */
	@Override
	public T pop() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("stack");
		T result = stack.removeFirst();
		return result;
	}

	/*
	 * Peek option: return the element on the top of the stack, the element is not removed from the stack
	 */
	@Override
	public T peek() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("stack");
		return stack.getFirst();
	}
	
	/*
	 * Returns true is the stack is empty and false otherwise.
	 */
	@Override
	public boolean isEmpty() {
		return stack.isEmpty();
	}
	/*
	 * Returns the size of the stack.
	 */
	@Override
	public int size() {
		return stack.size();
	}
	
	public void display(){
		System.out.println(" " + stack);
	}
	
	public static void main(String args[]){
		LinkedListStack<String> testStack = new LinkedListStack<String>();
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
	    System.out.println("After popping, the Stack is");
	    testStack.pop();
	    testStack.display();	
	    System.out.println("After popping, the Stack is");
	    testStack.pop();
	    testStack.display();	
	    System.out.println("current size of the stack is "+ testStack.size());
	    System.out.println("peek operation returns: " + testStack.peek());
	    System.out.println("The current Stack is:");
	    testStack.display();
	}

}
