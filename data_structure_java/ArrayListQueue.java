package assignment3;
import java.util.ArrayList;
import exceptions.EmptyCollectionException;
public class ArrayListQueue<T> implements QueueADT<T>

{
	ArrayList<T> queue = new ArrayList<T>();

	/*
	 * Adding specified element to the end of the queue
	 */
	@Override
	public void enqueue(T element) {
		queue.add(element);
	}

	/*
	 * Removing the first element from the queue
	 */
	@Override
	public T dequeue() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("queue");
		T result = queue.remove(0);
		return result;
	}

	/*
	 * Returning the first element of the queue
	 */
	@Override
	public T first() throws EmptyCollectionException
	{
		if (isEmpty())
			throw new EmptyCollectionException("queue");
		return queue.get(0);
	}

	/*
	 * Returning true if the queue is empty, false otherwise
	 */
	@Override
	public boolean isEmpty() {
		return queue.isEmpty();
	}

	/*
	 * Returning the size of queue
	 */
	@Override
	public int size() {
		return queue.size();
	}

	public void display() {
		System.out.println(" " + queue);
	}
	
	
	public static void main(String args[]){
		ArrayListQueue<String> testQueue = new ArrayListQueue<String>();
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
	    testQueue.dequeue(); // the element 1 is enqueued first and it is also dequeued first
	    testQueue.display();	    
	    System.out.println("current size of the queue is "+ testQueue.size());
	    System.out.println("first operation returns: " + testQueue.first());
	    System.out.println("The current Queue is:");
	    testQueue.display(); // after first option, the first element is not removed from the queue
	}
}
