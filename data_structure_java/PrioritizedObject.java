/**
 * PrioritizedObject represents a node in a priority queue containing a
 * comparable object, arrival order, and a priority value.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class PrioritizedObject<T> implements Comparable<PrioritizedObject>
{
    private static int nextOrder = 0;
    private int priority;
    private int arrivalOrder;
    private T element;

    /**
     * Creates a new PrioritizedObject with the specified data.
     *
     * @param element the element of the new priority queue node
     * @param priority the priority of the new queue node
     */
    public PrioritizedObject(T element, int priority) 
    {
        this.element = element;
        this.priority = priority;
        arrivalOrder = nextOrder;
        nextOrder++;
    }
    
    /**
     * Returns the element in this node.
     *
     * @return the element contained within the node
     */
    public T getElement() 
    {
        return element;
    }
    
    /**
     * Returns the priority value for this node.
     *
     * @return the integer priority for this node
     */
    public int getPriority() 
    {
        return priority;
    }

    /**
     * Returns the arrival order for this node.
     *
     * @return the integer arrival order for this node
     */
    public int getArrivalOrder() 
    {
        return arrivalOrder;
    }
    
    /**
     * Returns a string representation for this node.
     *
     */
    public String toString() 
    {
        return (element + "  " + priority + "  " + arrivalOrder);
    }
    
    /**
     * Returns 1 if the this object has higher priority than 
     * the given object and -1 otherwise.
     *
     * @param obj the object to compare to this node
     * @return the result of the comparison of the given object and 
     *         this one
     */
    public int compareTo(PrioritizedObject obj) 
    {
      int result;
				
      if (priority > obj.getPriority())
          result = 1;
      else if (priority < obj.getPriority())
          result = -1;
      else if (arrivalOrder > obj.getArrivalOrder())
          result = 1;
      else
          result = -1;
      
      return result;
    }
}


