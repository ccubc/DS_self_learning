package jsjf;
import java.util.Arrays;

public class MaxHeap {
	private static int N;
	
	/*
	 * This is a Heap Sort method.
	 * Input is an unsorted array.
	 */
    public static void sort(int arr[])
    {       
        heapify(arr);  // make the array to a heap data structure
        for (int i = N; i > 0; i--)
        {
            swap(arr,0, i); // swap the root node(which has the largest number) to loop invariant area (at the end of the array)
            N = N-1; // shorten the array to be sorted, so that sorted array would be loop invariant
            maxheap(arr, 0); // rebuild the unsorted array to heap structure
        }
    }  

    
    /*
     * Build a heap using an array
     */
    public static void heapify(int arr[])
    {
        N = arr.length-1; // N is the index of the last node in the heap
        for (int i = N/2; i >= 0; i--) // build the heap from bottom up 
            maxheap(arr, i);      

    }

    /*
     * The subroutine of building a maxheap using an array
     * This method will move the node at array index i down to the appropriate position, until heap structure is satisfied
     */
    public static void maxheap(int arr[], int i)
    { 
    // System.out.println("max: " + i);
        int left = 2*i + 1; // index of left child of node stored at arr[i]
        int right = 2*i + 2; // index of right child of node stored at arr[i]
        int max = i; // max will be used to store the index of the larger number of arr[i] and both of its children
        if (left <= N && arr[left] > arr[i]) // if arr[i]'s left child exists and it is greater than arr[i]
            max = left;     
        if (right <= N && arr[right] > arr[max]) // if arr[i]'s right child exists and it is greater than arr[i]   
        	max = right; 
        // after the two comparisons, arr[max] is ensured to be the largest among arr[i] and both of its children
        if (max != i) // if arr[i] is smaller than either of its children, need to move it downwards the tree
        {
        swap(arr, i, max); // swap arr[i] and its larger children, and now the element would be stored at arr[max]
        maxheap(arr, max); // keep moving down the element arr[max] by calling the method itself again
        // exit of this recursive program happens when max = i (when i is either a leaf or i is greater than both of its children)
        }
    }    

    /* Function to swap two numbers in an array */

    public static void swap(int arr[], int i, int j)
    {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp; 

    }    

    public static void main(String args[])
    {
    	System.out.println("Test case 1: ");
    	int[] testArray1 = {2,1,3,30,29,78,101,410,83,235,8205,5821,323,45,86,93,100,2774,2};
    	System.out.println("The original inputted array is: " + Arrays.toString(testArray1));
    	sort(testArray1);
    	System.out.println("The array after heap sort is: " + Arrays.toString(testArray1));
    	
    	System.out.println("\n \n Test case 2: ");
    	int[] testArray2 = {2,3,5};
    	System.out.println("The original inputted array is: " + Arrays.toString(testArray2));
    	sort(testArray2);
    	System.out.println("The array after heap sort is: " + Arrays.toString(testArray2));
    	
    	System.out.println("\n \n Test case 3: ");
    	int[] testArray3 = {2};
    	System.out.println("The original inputted array is: " + Arrays.toString(testArray3));
    	sort(testArray3);
    	System.out.println("The array after heap sort is: " + Arrays.toString(testArray3));
    	
      	System.out.println("\n \n Test case 4: ");
    	int[] testArray4 = {};
    	System.out.println("The original inputted array is: " + Arrays.toString(testArray4));
    	sort(testArray4);
    	System.out.println("The array after heap sort is: " + Arrays.toString(testArray4));
    
    	System.out.println("\n \n Test case 5: ");
    	int[] testArray5 = {2,1,3,30,29,78,102,103,424,1,414,14,56,63,62,24,101,410,83,235,8205,5821,323,45,86,93,100,2774,2};
    	System.out.println("The original inputted array is: " + Arrays.toString(testArray5));
    	sort(testArray5);
    	System.out.println("The array after heap sort is: " + Arrays.toString(testArray5));
    	

    }
}
