package assignment3;
import java.util.LinkedList;
import exceptions.EmptyCollectionException;
public class LinkedListQueue<T> implements QueueADT<T>
{
	
	LinkedList<T> queue = new LinkedList<T>();

/*
 * Adds the specified element to the tail of the queue.
 */
	@Override
	public void enqueue(T element) {
		queue.addLast(element);
	}

/*
 * Removes the specified element from the head of the queue.
 */
	@Override
	public T dequeue() throws EmptyCollectionException
	{
		if(isEmpty())
			throw new EmptyCollectionException("queue");
		T result = queue.removeFirst();
		return result;
	}

/*
 * Returns the first element of the queue without removing it from the queue.
 */
	@Override
	public T first() throws EmptyCollectionException
	{
		if(isEmpty())
			throw new EmptyCollectionException("queue");
		return queue.getFirst();
	}

/*
 * Returns true is the stack is empty and false otherwise.
 */
	@Override
	public boolean isEmpty() {
		return queue.isEmpty();
	}

/*
 * Returns the size of the queue.
 */
	@Override
	public int size() {
		return queue.size();
	}
	
	public void display(){
		System.out.println(" " + queue);

	}
	
	public static void main(String args[]){
		LinkedListQueue<String> testQueue = new LinkedListQueue<String>();
		/*
		 * if running either of the line of code below, will throw EmptyCollectionException
		testQueue.dequeue();
		testQueue.first();
		*/
		System.out.println("Is the Queue empty?");
		System.out.println(testQueue.isEmpty());
		testQueue.enqueue("1");
		testQueue.enqueue("2");
		testQueue.enqueue("3");
		testQueue.enqueue("4");
		System.out.println("After enqueueing 4 elements, the Queue is:");
		testQueue.display();
		System.out.println("Is the Queue empty?");
		System.out.println(testQueue.isEmpty());
	    System.out.println("After dequeing once, the Queue is");
	    testQueue.dequeue();
	    testQueue.display();	    
	    System.out.println("current size of the queue is "+ testQueue.size());
	    System.out.println("first operation returns: " + testQueue.first());
	    System.out.println("The current Queue is:");
	    testQueue.display();
	}

}
