package jsjf;

import jsjf.exceptions.*;
import java.util.Iterator;

/**
 * BinarySearchTreeList represents an ordered list implemented using a binary
 * search tree.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class BinarySearchTreeList<T> extends LinkedBinarySearchTree<T> 
                      implements ListADT<T>, OrderedListADT<T>, Iterable<T>
{
    /**
     * Creates an empty BinarySearchTreeList.
     */
    public BinarySearchTreeList() 
    {
        super();
    }

    /**
     * Adds the given element to this list.
     * 
     * @param element the element to be added to the list
     */
    public void add(T element)
    {
        addElement(element);
    }
    
    /**
     * Removes and returns the first element from this list.
     *
     * @return the first element in the list
     */
    public T removeFirst()
    {
        return removeMin();
    }
    
    /**
     * Removes and returns the last element from this list.
     *
     * @return the last element from the list
     */
    public T removeLast()
    {
        return removeMax();
    }

   /**
    * Removes and returns the specified element from this list.
    *
    * @param element the element being sought in the list
    * @return the element from the list that matches the target
    */
    public T remove(T element)
    {
        return removeElement(element);
    }

   /**
    * Returns a reference to the first element on this list.
    *
    * @return a reference to the first element in the list
    */
    public T first()
    {
        return findMin();
    }

   /**
    * Returns a reference to the last element on this list.
    *
    * @return a reference to the last element in the list
    */
    public T last()
    {
        return findMax();
    }

   /**
    * Returns an iterator for the list.
    *
    * @return an iterator over the elements in the list
    */
    public Iterator<T> iterator()
    {
        return iteratorInOrder();
    }
}

