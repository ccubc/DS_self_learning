import exceptions.EmptyCollectionException;

public class ArrayDeque<T>
{
   private final int DEFAULT_CAPACITY = 100;
   private int rear;
   private T[] deque; 

   /******************************************************************
     Creates an empty deque using the default capacity.
   ******************************************************************/
   public ArrayDeque()
   {
      rear = 0;
      deque = (T[])(new Object[DEFAULT_CAPACITY]);
   }

   /******************************************************************
     Creates an empty deque using the specified capacity.
   ******************************************************************/
   public ArrayDeque (int initialCapacity)
   {
      rear = 0;
      deque = (T[])(new Object[initialCapacity]);
   }

   /******************************************************************
     Adds the specified element to the rear of this deque, expanding
     the capacity of the deque array if necessary.
   ******************************************************************/
   public void rearInsert (T element)
   {
      if (size() == deque.length) 
         expandCapacity();

      deque[rear] = element;
      rear++;
   }

   public void frontInsert (T element)
   {
	   if (size() == deque.length)
		   expandCapacity();
	   /** shift the elements **/
	   
	   for (int scan=rear-1; scan>=0; scan--)
		   deque[scan+1] = deque[scan];
	   deque[0] = element;
	   rear++;
   }
   /******************************************************************
     Removes the element at the front of this deque and returns a
     reference to it. Throws an EmptyCollectionException if the
     deque is empty.
   ******************************************************************/
   public T frontRemove() throws EmptyCollectionException
   {
      if (isEmpty())
         throw new EmptyCollectionException ("deque");

      T result = deque[0];

      rear--;

      /** shift the elements  */
      for (int scan=0; scan < rear; scan++)
         deque[scan] = deque[scan+1];
      
      deque[rear] = null;
 
      return result;
   }
   
   /******************************************************************
   Removes the element at the rear of this deque and returns a
   reference to it. Throws an EmptyCollectionException if the
   deque is empty.
 ******************************************************************/
 public T rearRemove() throws EmptyCollectionException
 {
    if (isEmpty())
       throw new EmptyCollectionException ("deque");
    rear--;
    T result = deque[rear];
    deque[rear] = null;

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
         throw new EmptyCollectionException ("deque"); 

      return deque[0];
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
         result = result + deque[scan].toString() + "\n";

      return result;
   }

   /******************************************************************
     Creates a new array to store the contents of this queue with
     twice the capacity of the old one.
   ******************************************************************/
   private void expandCapacity()
   {
      T[] larger = (T[])(new Object[deque.length*2]);

      for (int scan=0; scan < deque.length; scan++)
         larger[scan] = deque[scan];

      deque = larger;
   }
   
   public static void main(String args[]){
	   ArrayDeque testDeque = new ArrayDeque();
	   testDeque.rearInsert(1);
	   testDeque.rearInsert(2);
	   testDeque.rearInsert(3);
	   System.out.println("Current deque is \n" + testDeque);
	   System.out.println("front remove element: " + testDeque.frontRemove());
	   System.out.println("Current deque is \n" + testDeque);
	   testDeque.frontInsert(4);
	   testDeque.frontInsert(5);
	   System.out.println("After front insert twice, current deque is \n" + testDeque);
	   System.out.println("rear remove element: " + testDeque.rearRemove());
	   System.out.println("Current deque is \n" + testDeque);



   }
}