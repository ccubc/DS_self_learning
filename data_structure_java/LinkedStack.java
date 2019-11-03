
import exceptions.*;
import java.util.Iterator;

/**
 * Represents a linked implementation of a stack.
 *
 * @author Java Foundations 
 * @version 4.0
 */
public class LinkedStack<T> implements StackADT<T>
{
    private int count;  
    private LinearNode<T> top; 

    /**
     * Creates an empty stack.
     */
    public LinkedStack()
    {
        count = 0;
        top = null;
    }

    /**
     * Adds the specified element to the top of this stack.
     * @param element element to be pushed on stack
     */
    public void push(T element)
    {
        LinearNode<T> temp = new LinearNode<T>(element);
        temp.setNext(top);
        top = temp;
        count++;
    }

    /**
     * Removes the element at the top of this stack and returns a
     * reference to it. 
     * @return element from top of stack
     * @throws EmptyCollectionException if the stack is empty
     */
    public T pop() throws EmptyCollectionException
    {
        if (isEmpty())
            throw new EmptyCollectionException("stack");

        T result = top.getElement();
        top = top.getNext();
        count--;
 
        return result;
    }
   
    /**
     * Returns a reference to the element at the top of this stack.
     * The element is not removed from the stack.  
     * @return element on top of stack
     * @throws EmptyCollectionException if the stack is empty  
     */
    public T peek() throws EmptyCollectionException
    {
    	if(isEmpty())
    		throw new EmptyCollectionException("stack");
        T result = top.getElement();
        return result;
        }

    /**
     * Returns true if this stack is empty and false otherwise. 
     * @return true if stack is empty
     */
    public boolean isEmpty()
    {
        // To be completed as a Programming Project
    	return (count == 0);
    }
 
    /**
     * Returns the number of elements in this stack.
     * @return number of elements in the stack
     */
    public int size()
    {
        // To be completed as a Programming Project
    	return count;
    }

    /**
     * Returns a string representation of this stack. 
     * @return string representation of the stack
     */
    public String toString()
    {
        // To be completed as a Programming Project
    	String result = "";
    	LinearNode current = top;
    	while (current != null)
    	{
    		result=result+current.getElement()+"\n";
    		current=current.getNext();
    	}
    	return result;
    }
    public static void main(String args[]){
    	LinkedStack testStack = new LinkedStack();
		testStack.push("1");
		testStack.push("2");
		testStack.push("3");
		testStack.push("4");
		System.out.println("Ordinary Stack:");
		System.out.println(testStack);
	    System.out.println("after popping the top element");
	    testStack.pop();
	    System.out.println(testStack);
	    
	    System.out.println("current size of the stack is "+ testStack.size());
	    System.out.println("peek operation returns: " + testStack.peek());
	  

    }
}
