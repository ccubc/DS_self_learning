import jsjf.*;

/**
 * PriorityQueue implements a priority queue using a heap.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class PriorityQueue<T> extends ArrayHeap<PrioritizedObject<T>>
{
    /**
     * Creates an empty priority queue.
     */
    public PriorityQueue() 
    {
        super();
    }
    
    /**
     * Adds the given element to this PriorityQueue.
     *
     * @param object the element to be added to the priority queue
     * @param priority the integer priority of the element to be added
     */
    public void addElement(T object, int priority) 
    {
        PrioritizedObject<T> obj = new PrioritizedObject<T>(object, priority);
	    super.addElement(obj);
    }
    
    /**
     * Removes the next highest priority element from this priority 
     * queue and returns a reference to it.
     *
     * @return a reference to the next highest priority element in this queue
     */
    public T removeNext() 
    {
        PrioritizedObject<T> obj = (PrioritizedObject<T>)super.removeMin();
        return obj.getElement();
    }
}


