//********************************************************************
//  ArrayQueue.java       Authors: Lewis/Chase
//
//  Represents an array implementation of a queue. The front of
//  the queue is kept at array index 0.
//********************************************************************
import exceptions.*;
import jsjf.QueueADT;
import jsjf.exceptions.EmptyCollectionException;

public class ArrayQueue<T> implements QueueADT<T>
{
   private final int DEFAULT_CAPACITY = 100;
   private int rear;
   private T[] queue; 

   /******************************************************************
     Creates an empty queue using the default capacity.
   ******************************************************************/
   public ArrayQueue()
   {
      rear = 0;
      queue = (T[])(new Object[DEFAULT_CAPACITY]);
   }

   /******************************************************************
     Creates an empty queue using the specified capacity.
   ******************************************************************/
   public ArrayQueue (int initialCapacity)
   {
      rear = 0;
      queue = (T[])(new Object[initialCapacity]);
   }

   /******************************************************************
     Adds the specified element to the rear of this queue, expanding
     the capacity of the queue array if necessary.
   ******************************************************************/
   public void enqueue (T element)
   {
      if (size() == queue.length) 
         expandCapacity();

      queue[rear] = element;
      rear++;
   }

   /******************************************************************
     Removes the element at the front of this queue and returns a
     reference to it. Throws an EmptyCollectionException if the
     queue is empty.
   ******************************************************************/
   public T dequeue() throws EmptyCollectionException
   {
      if (isEmpty())
         throw new EmptyCollectionException ("queue");

      T result = queue[0];

      rear--;

      /** shift the elements  */
      for (int scan=0; scan < rear; scan++)
         queue[scan] = queue[scan+1];
      
      queue[rear] = null;
 
      return result;
   }
   
   /******************************************************************
     Returns a reference to the element at the front of this queue.
     The element is not removed from the queue.  Throws an
     EmptyCollectionException if the queue is empty.  
   ******************************************************************/
   public T first() throws EmptyCollectionException
   {
      if (isEmpty())
         throw new EmptyCollectionException ("queue"); 

      return queue[0];
   }

   /******************************************************************
     Returns true if this queue is empty and false otherwise. 
   ******************************************************************/
   public boolean isEmpty()
   {
      return (rear == 0);
   }
 
   /******************************************************************
     Returns the number of elements currently in this queue.
   ******************************************************************/
   public int size()
   {
      return rear;
   }

   /******************************************************************
     Returns a string representation of this queue. 
   ******************************************************************/
   public String toString()
   {
      String result = "";

      for (int scan=0; scan < rear; scan++) 
         result = result + queue[scan].toString() + "\n";

      return result;
   }

   /******************************************************************
     Creates a new array to store the contents of this queue with
     twice the capacity of the old one.
   ******************************************************************/
   private void expandCapacity()
   {
      T[] larger = (T[])(new Object[queue.length*2]);

      for (int scan=0; scan < queue.length; scan++)
         larger[scan] = queue[scan];

      queue = larger;
   }
   
   public static void main(String args[]){
	   ArrayQueue testQ = new ArrayQueue();
	   testQ.enqueue(1);
	   testQ.enqueue(2);
	   testQ.enqueue(3);
	   System.out.println("Current queue is \n" + testQ);
	   System.out.println("dequeue element: " + testQ.dequeue());
	   System.out.println("Current queue is \n" + testQ);
	   testQ.enqueue(4);
	   System.out.println("Current queue is \n" + testQ);
	   System.out.println("dequeue element: " + testQ.dequeue());
	   System.out.println("Current queue is \n" + testQ);


   }
}