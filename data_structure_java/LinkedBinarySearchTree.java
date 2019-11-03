package jsjf;

import jsjf.exceptions.*;

import java.awt.List;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.*;

import jsjf.*;

/**
 * LinkedBinarySearchTree implements the BinarySearchTreeADT interface 
 * with links.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class LinkedBinarySearchTree<T> extends LinkedBinaryTree<T>
                                        implements BinarySearchTreeADT<T>
{
    /**
     * Creates an empty binary search tree.
     */
    public LinkedBinarySearchTree() 
    {
        super();
    }
    
    /**
     * Creates a binary search with the specified element as its root.
     *
     * @param element the element that will be the root of the new binary
     *        search tree
     */
    public LinkedBinarySearchTree(T element) 
    {
        super(element);
        
        if (!(element instanceof Comparable))
            throw new NonComparableElementException("LinkedBinarySearchTree");
    }
    
    /**
     * Adds the specified object to the binary search tree in the
     * appropriate position according to its natural order.  Note that
     * equal elements are added to the right.
     *
     * @param element the element to be added to the binary search tree
     */
    public void addElement(T element) 
    {
        if (!(element instanceof Comparable))
            throw new NonComparableElementException("LinkedBinarySearchTree");

        Comparable<T> comparableElement = (Comparable<T>)element;

        if (isEmpty())
            root = new BinaryTreeNode<T>(element);
        else 
        {
            if (comparableElement.compareTo(root.getElement()) < 0)
            {
                if (root.getLeft() == null) 
                    this.getRootNode().setLeft(new BinaryTreeNode<T>(element));
                else
                    addElement(element, root.getLeft());
            }
            else
            {
                if (root.getRight() == null) 
                    this.getRootNode().setRight(new BinaryTreeNode<T>(element));
                else
                    addElement(element, root.getRight());
            }
        }
        modCount++;
    }
    
    /**
     * Adds the specified object to the binary search tree in the
     * appropriate position according to its natural order.  Note that
     * equal elements are added to the right.
     *
     * @param element the element to be added to the binary search tree
     */
    private void addElement(T element, BinaryTreeNode<T> node) 
    {
        Comparable<T> comparableElement = (Comparable<T>)element;
        
        if (comparableElement.compareTo(node.getElement()) < 0)
        {
            if (node.getLeft() == null) 
                node.setLeft(new BinaryTreeNode<T>(element));
            else
                addElement(element, node.getLeft());
        }
        else
        {
            if (node.getRight() == null) 
                node.setRight(new BinaryTreeNode<T>(element));
            else
                addElement(element, node.getRight());
        }
    }
        
        
    /**
     * Removes the first element that matches the specified target
     * element from the binary search tree and returns a reference to
     * it.  Throws a ElementNotFoundException if the specified target
     * element is not found in the binary search tree.
     *
     * @param targetElement the element being sought in the binary search tree
     * @throws ElementNotFoundException if the target element is not found
     */
    public T removeElement(T targetElement)
                                  throws ElementNotFoundException 
    {
        T result = null;

        if (isEmpty())
            throw new ElementNotFoundException("LinkedBinarySearchTree");
        else
        {
            BinaryTreeNode<T> parent = null;
            if (((Comparable<T>)targetElement).equals(root.element)) 
            {
                result =  root.element;
                BinaryTreeNode<T> temp = replacement(root);
                if (temp == null)
                    root = null;
                else 
                {
                    root.element = temp.element;
                    root.setRight(temp.right);
                    root.setLeft(temp.left);
                }

                modCount--;
            }
            else 
            {                
                parent = root;
                if (((Comparable)targetElement).compareTo(root.element) < 0)
                    result = removeElement(targetElement, root.getLeft(), parent);
                else
                    result = removeElement(targetElement, root.getRight(), parent);
            }
        }
        
        return result;
    }
                
    /**
     * Removes the first element that matches the specified target
     * element from the binary search tree and returns a reference to
     * it.  Throws a ElementNotFoundException if the specified target
     * element is not found in the binary search tree.
     *
     * @param targetElement the element being sought in the binary search tree
     * @param node the node from which to search
     * @param parent the parent of the node from which to search
     * @throws ElementNotFoundException if the target element is not found
     */
    private T removeElement(T targetElement, BinaryTreeNode<T> node, BinaryTreeNode<T> parent)
    throws ElementNotFoundException 
    {
        T result = null;
        
        if (node == null)
            throw new ElementNotFoundException("LinkedBinarySearchTree");
        else
        {
            if (((Comparable<T>)targetElement).equals(node.element)) 
            {
                result =  node.element;
                BinaryTreeNode<T> temp = replacement(node);
                if (parent.right == node)
                    parent.right = temp;
                else 
                    parent.left = temp;

                modCount--;
            }
            else 
            {                
                parent = node;
                if (((Comparable)targetElement).compareTo(node.element) < 0)
                    result = removeElement(targetElement, node.getLeft(), parent);
                else
                    result = removeElement(targetElement, node.getRight(), parent);
            }
        }
        
        return result;
    }
    
    /**
     * Returns a reference to a node that will replace the one
     * specified for removal.  In the case where the removed node has 
     * two children, the inorder successor is used as its replacement.
     *
     * @param node the node to be removed
     * @return a reference to the replacing node
     */
    private BinaryTreeNode<T> replacement(BinaryTreeNode<T> node) 
    {
        BinaryTreeNode<T> result = null;
        
        if ((node.left == null) && (node.right == null))
            result = null;
        
        else if ((node.left != null) && (node.right == null))
            result = node.left;
        
        else if ((node.left == null) && (node.right != null))
            result = node.right;
        
        else
        {
            BinaryTreeNode<T> current = node.right;
            BinaryTreeNode<T> parent = node;
            
            while (current.left != null)
            {
                parent = current;
                current = current.left;
            }
            
            current.left = node.left;
            if (node.right != current)
            {
                parent.left = current.right;
                current.right = node.right;
            }
            
            result = current;
        }
        
        return result;
    }
    
    /**
     * Removes elements that match the specified target element from 
     * the binary search tree. Throws a ElementNotFoundException if 
     * the sepcified target element is not found in this tree.
     *
     * @param targetElement the element being sought in the binary search tree
     * @throws ElementNotFoundException if the target element is not found
     */
    public void removeAllOccurrences(T targetElement)
                   throws ElementNotFoundException 
    {
        removeElement(targetElement);
        
        try
        {
            while (contains((T)targetElement))
                removeElement(targetElement);
        }
        
        catch (Exception ElementNotFoundException)
        {
        }
    }

    /**
     * Removes the node with the least value from the binary search
     * tree and returns a reference to its element.  Throws an
     * EmptyCollectionException if this tree is empty. 
     *
     * @return a reference to the node with the least value
     * @throws EmptyCollectionException if the tree is empty
     */
    public T removeMin() throws EmptyCollectionException 
    {
        T result = null;

        if (isEmpty())
            throw new EmptyCollectionException("LinkedBinarySearchTree");
        else 
        {
            if (root.left == null) 
            {
                result = root.element;
                root = root.right;
            }
            else 
            {
                BinaryTreeNode<T> parent = root;
                BinaryTreeNode<T> current = root.left;
                while (current.left != null) 
                {
                    parent = current;
                    current = current.left;
                }
                result =  current.element;
                parent.left = current.right;
            }

            modCount--;
        }
 
        return result;
    }

    /**
     * Removes the node with the highest value from the binary
     * search tree and returns a reference to its element.  Throws an
     * EmptyCollectionException if this tree is empty. 
     *
     * @return a reference to the node with the highest value
     * @throws EmptyCollectionException if the tree is empty
     */
    public T removeMax() throws EmptyCollectionException 
    {
    	T result = null;
    	if(isEmpty())
    		throw new EmptyCollectionException("LinkedBinarySearchTree");
    	else
    	{
    		if (root.right == null)
    		{
    			result = root.element;
    			root = root.left;
    		}
    		else
    		{
    			BinaryTreeNode<T> parent = root;
    			BinaryTreeNode<T> current = root.right;
    			while(current.right != null)
    			{
    			parent = current;
    			current = current.right;
    			}
    		result = current.element;
    		parent.right = current.left;
    		}
    	modCount--;
    	}
    	return result;
    }

    /**
     * Returns the element with the least value in the binary search
     * tree. It does not remove the node from the binary search tree. 
     * Throws an EmptyCollectionException if this tree is empty.
     *
     * @return the element with the least value
     * @throws EmptyCollectionException if the tree is empty
     */
    public T findMin() throws EmptyCollectionException 
    {
    	T rootElement = null;
    		LinkedBinaryTree<T> current = this;
    		while(!current.isEmpty()){
    			rootElement = current.getRootElement();
    			current = current.getLeft();
    		}
    		return rootElement;
    }

    /**
     * Returns the element with the highest value in the binary
     * search tree.  It does not remove the node from the binary
     * search tree.  Throws an EmptyCollectionException if this 
     * tree is empty.
     *
     * @return the element with the highest value
     * @throws EmptyCollectionException if the tree is empty
     */
    public T findMax() throws EmptyCollectionException 
    {
    	T rootElement = null;
    		LinkedBinaryTree<T> current = this;
    		while(!current.isEmpty()){
    			rootElement = current.getRootElement();
    			current = current.getRight();
    		}
    		return rootElement;
    }

    /**
     * Returns a reference to the specified target element if it is
     * found in the binary tree.  Throws a NoSuchElementException if
     * the specified target element is not found in this tree.
     *
     * @param targetElement the element being sough in the binary tree
     * @throws ElementNotFoundException if the target element is not found
     */
    public T find(T targetElement) throws ElementNotFoundException 
    {
    	BinaryTreeNode<T> current = root;
    	BinaryTreeNode<T> temp = current;
    	if(!(current.element.equals(targetElement)) && (current.left != null) && (((Comparable)current.element).compareTo(targetElement)>0))
    		current = findNode(targetElement, current.left);
    	
    	else if (!(current.element.equals(targetElement)) && (current.right != null))
    		current = findNode(targetElement, current.right);
    	if (!(current.element.equals(targetElement)))
    		throw new ElementNotFoundException ("binarytree");
    	return current.element;
    }
       
    
    /**
     * Returns the left subtree of the root of this tree.
     *
     * @return a link to the left subtree of the tree
     */
    public LinkedBinarySearchTree<T> getLeft()
    {
    	LinkedBinarySearchTree<T> result = new LinkedBinarySearchTree<T>();
    	result.root = root.getLeft();
    	return result;
    }
    
    /**
     * Returns the right subtree of the root of this tree.
     *
     * @return a link to the right subtree of the tree
     */
    public LinkedBinarySearchTree<T> getRight()
    {
    	LinkedBinarySearchTree<T> result = new LinkedBinarySearchTree<T>();
    	result.root = root.getRight();
    	return result;
    }
    
    /**
     * Returns a reference to the specified target element if it is
     * found in this tree.  
     *
     * @param targetElement the element being sought in the tree
     * @param next the tree node to begin searching on
     */
    private BinaryTreeNode<T> findNode(T targetElement, BinaryTreeNode<T> next) 
    {
    	BinaryTreeNode<T> current = next;
    	if (!(next.element.equals(targetElement)) && (next.left != null) && (((Comparable)next.element).compareTo(targetElement)>0))
    		next = findNode(targetElement, next.left);
    	else if (!(next.element.equals(targetElement)) && (next.right != null))
    		next = findNode(targetElement, next.right);
    	return next;
    }
    
    public void balanceTree() 
    {  	
    	ArrayList<T> list = new ArrayList<T>();
    	for (Iterator<T> iter = iteratorInOrder(); iter.hasNext();) {
    		list.add(iter.next());
    		}
    	root = balanceTreeRecursive(list);
    	System.out.println("Level Order Traversal of the new balanced tree is:");
    	for (Iterator<T> iter2 = iteratorLevelOrder(); iter2.hasNext();) {
    		System.out.println(" " + iter2.next());
    		}
    }
    
    private BinaryTreeNode<T> balanceTreeRecursive(java.util.List<T> list)
    {
    	if (list.isEmpty())
    		return null;
    	else
    	{
    		int middle = list.size() / 2;
    		BinaryTreeNode<T> node = new BinaryTreeNode<T>(list.get(middle));
    		node.setLeft(balanceTreeRecursive(list.subList(0, middle)));
    		node.setRight(balanceTreeRecursive(list.subList(middle + 1, list.size())));
    		return node;
    	}  	
    }
    
    
    public static LinkedBinarySearchTree<Integer> generateTestTree1(){
    	LinkedBinarySearchTree<Integer> testTree = new LinkedBinarySearchTree<Integer>();
    	    	for(int i=1 ; i<16 ; i++) {
    	    		testTree.addElement(i);
    	    	}
    	return testTree;
    	}
    
    public static LinkedBinarySearchTree<Integer> generateTestTree2(){
    	LinkedBinarySearchTree<Integer> testTree = null;
    	return testTree;
    }
    
    public static LinkedBinarySearchTree<Integer> generateTestTree3(){
    	LinkedBinarySearchTree<Integer> testTree = new LinkedBinarySearchTree<Integer>(1);
    	return testTree;
    	}
    
    public static LinkedBinarySearchTree<Integer> generateTestTree4(){
    	LinkedBinarySearchTree<Integer> testTree = new LinkedBinarySearchTree<Integer>();
    	for(int i=1 ; i<3 ; i++) {
    		testTree.addElement(i);
    	}
    	return testTree;  	
    }
    public static LinkedBinarySearchTree<Integer> generateTestTree5(){
    	LinkedBinarySearchTree<Integer> testTree = new LinkedBinarySearchTree<Integer>();
    	for(int i=1 ; i<4 ; i++) {
    		testTree.addElement(i);
    	}
    	return testTree;  	
    }
    public static LinkedBinarySearchTree<Integer> generateTestTree6(){
    	LinkedBinarySearchTree<Integer> testTree = new LinkedBinarySearchTree<Integer>();
 
    	return testTree;  	
    }
    public static LinkedBinarySearchTree<Integer> generateTestTree7(){
    	LinkedBinarySearchTree<Integer> testTree = new LinkedBinarySearchTree<Integer>();
    	for(int i=1 ; i<18 ; i++) {
    		testTree.addElement(i);
    	}
    	return testTree;  	
    }

    public static void main (String[] args) throws NullPointerException
    {
    	

    	System.out.println("testing the balanced tree method of the LinkedBinarySearchTree class: ");
    	LinkedBinarySearchTree<Integer> testTree = generateTestTree1();
    	/*
    	 * Test the cases one by one.
    	 * TestTree1 is a general case, consisting of 15 nodes.
    	 * TestTree2 is NULL
    	 * TestTree3 has only the root node.
    	 * TestTree4 only has 2 nodes.
    	 * TestTree5 only has 3 nodes.
    	 * TestTree6 is an empty tree.
    	 * TestTree7 has 17 nodes.
    	LinkedBinarySearchTree<Integer> testTree = generateTestTree2();
    	LinkedBinarySearchTree<Integer> testTree = generateTestTree3();
    	LinkedBinarySearchTree<Integer> testTree = generateTestTree4();
    	LinkedBinarySearchTree<Integer> testTree = generateTestTree5();
    	LinkedBinarySearchTree<Integer> testTree = generateTestTree6();
    	 */
    	if (testTree == null)
    	{
    	throw new NullPointerException("Test tree is NULL");
    	}

    	System.out.println("The root of the tree is: " + testTree.getRootElement());
    	System.out.println("The height of the tree is: " + testTree.getHeight());
    	System.out.println("Balance the tree using brute force method ...");
    	testTree.balanceTree();
    	System.out.println("The root of the new tree is: " + testTree.getRootElement());
    	System.out.println("The height of the new tree is: " + testTree.getHeight());

    	
    	
    }

}

