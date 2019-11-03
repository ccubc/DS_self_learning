package jsjf;

/**
 * HeapNode represents a binary tree node with a parent pointer for use 
 * in heaps.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class HeapNode<T> extends BinaryTreeNode<T>
{
    protected HeapNode<T> parent;

    /**
     * Creates a new heap node with the specified data.
     * 
     * @param obj the data to be contained within the new heap node
     */
    public HeapNode(T obj) 
    {
        super(obj);
        parent = null;
    }
	
	/**
     * Return the parent of this node.
     *
     * @return the parent of the node
	 */
    public HeapNode<T> getParent() 
    {
        return parent;
    }
	
	/**
     * Sets the element stored at this node.
     *
     * @param the element to be stored 
	 */
    public void setElement(T obj) 
    {
        element = obj;
    }
	
	/**
     * Sets the parent of this node.
     *
     * @param node the parent of the node
	 */
    public void setParent(HeapNode<T> node) 
    {
        parent = node;
    }
}


