package jsjf;

/**
 * HeapSort sorts a given array of Comparable objects using a heap.
 * 
 * @author Java Foundations
 * @version 4.0
 */
public class HeapSort<T>
{
    /**
     * Sorts the specified array using a Heap
	 *
	 * @param data the data to be added to the heapsort
     */
	public void HeapSort(T[] data) 
	{
		ArrayHeap<T> temp = new ArrayHeap<T>();

		// copy the array into a heap 
		for (int i = 0; i < data.length; i++)
		    temp.addElement(data[i]);

		// place the sorted elements back into the array 
		int count = 0;
		while (!(temp.isEmpty()))
		{
			data[count] = temp.removeMin();
			count++;
		}
	}
}


