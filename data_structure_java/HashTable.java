package jsjf;


/*
 * Implement a dynamically resizable hash table to store people's names and Social Security numbers.
 * Extraction method, with division using last four digits of the SSN.
 * Initial table size is 31, load factor is 0.80.
 * Open addressing, with double hashing using an extracton method on the first three digits of the SSN.
 * Author: Cheng Chen
 */
public class HashTable {
	private static int tablesize = 31;
	private final static float LOAD_FACTOR = (float) 0.8;
	HashEntry[] table; // hash table
	private int count = 0; // count of (SSN, name) pairs in the table
	
	public HashTable(){
		// create a hash table with initial table size
		table = new HashEntry[tablesize];
		for (int i = 0; i < tablesize; i++)
			table[i] = null;
	}
	
	
	public void put(int SSN, String name) {
		// input (SSN, name) pairs to the Hash Table
		// SSN should be a nine digit integer starting with a non-zero number
		int hash = ((SSN % 10000) % tablesize); // make hash code equals (last four digit of SSN) % tablesize
		if (table[hash] == null){
			HashEntry entry = new HashEntry(SSN, name);
			table[hash] = entry;
			}
		else{
			hash = ((Integer.parseInt(Integer.toString(SSN).substring(0, 3))) % tablesize); 
			// double hash code = (first 3 digits of SSN) % TABLE_SIZE
			if(table[hash] == null){ 
				// if found an available slot for new input
				HashEntry entry = new HashEntry(SSN, name);
				table[hash] = entry;
				}
			else{
				// if double hashing still could not return available slot
				while(table[hash] != null){
					hash ++;
					hash = hash % tablesize;
					} // now we found an available slot at table[hash]
				HashEntry entry = new HashEntry(SSN, name);
				table[hash] = entry;
				}
			}
			count ++;
			int maxsize = (int) (tablesize*LOAD_FACTOR);
			if(count >= maxsize)
				rehash(); // resize the table
	}
	
	public String get(int SSN){
		// Retrieve the name associate with the specified SSN, if input SSN is valid
		int hash = ((SSN % 10000) % tablesize);	
		HashEntry entry = table[hash];
		if (entry == null)
			return "Social Security Number not found.";
		if (entry.getSSN() == SSN)
			return entry.getName();
		else{
			hash = ((Integer.parseInt(Integer.toString(SSN).substring(0, 3))) % tablesize); 
			entry = table[hash];
			if (entry == null)
				return "Social Security Number not found.";
			if (entry.getSSN() == SSN)
				return entry.getName();
			else{
				while(table[hash] != null){
					// if input SSN is not valid, table[hash] will reach null and exit the while loop
					hash++;
					hash = hash % tablesize;
					entry = table[hash];
					if(entry.getSSN() == SSN)
						return entry.getName();
				}
				return "Social Security Number not found.";
			}
		}
	}
	public boolean containsSSN(int SSN){
		// tests whether a SSN exists in the hash table, return a boolean value
		int hash = ((SSN % 10000) % tablesize);	
		HashEntry entry = table[hash];
		if (entry == null)
			return false;
		if (entry.getSSN() == SSN)
			return true;
		else{
			hash = ((Integer.parseInt(Integer.toString(SSN).substring(0, 3))) % tablesize); 
			entry = table[hash];
			if (entry == null)
				return false;
			if (entry.getSSN() == SSN)
				return true;
			else{
				while(table[hash] != null){
					// if input SSN is not valid, table[hash] will reach null and exit the while loop
					hash++;
					hash = hash % tablesize;
					entry = table[hash];
					if(entry.getSSN() == SSN)
						return true;
				}
				return false;
			}
		}
	}
	
	public int size(){
		return count;
	}
	
	public void printTable(){
		// print the table for testing purpose
		System.out.println();
		for(int i = 0; i < tablesize; i++) {
			System.out.print(i + ":");
			HashEntry entry = table[i];
			if(entry != null)
				System.out.print(" (" + entry.getSSN() + "," + entry.getName() + ")");
			System.out.println();
		}
	}
	
	public void rehash(){
		tablesize = 2 * table.length;
		HashEntry[] oldTable = table;
		table = new HashEntry[tablesize];
		count = 0;
		for (int i = 0; i < oldTable.length; i++)
			if(oldTable[i] != null)
				put(oldTable[i].getSSN(), oldTable[i].getName());	
		
	}
	
	public void remove(int SSN){
		// remove the data pair with specified SSN, do nothing if the input SSN is not found.
		
		// remove the data pair and set it to null in the HashTable
		if(containsSSN(SSN) == true){
			int hash = ((SSN % 10000) % tablesize);	
			HashEntry entry = table[hash];
			if (entry.getSSN() == SSN)
				table[hash] = null;
			else{
				hash = ((Integer.parseInt(Integer.toString(SSN).substring(0, 3))) % tablesize); 
				entry = table[hash];
				if (entry.getSSN() == SSN)
					table[hash] = null;
				else{
					while(table[hash] != null){
						// if input SSN is not valid, table[hash] will reach null and exit the while loop
						hash++;
						hash = hash % tablesize;
						entry = table[hash];
						if(entry.getSSN() == SSN)
							table[hash] = null;
					}
				}
			}
			count --;
			
		// After the removing, the hash code needs to be changed
			HashEntry[] newTable = table;
			table = new HashEntry[tablesize];
			count = 0;
			for (int i = 0; i < newTable.length; i++)
				if(newTable[i] != null)
					put(newTable[i].getSSN(), newTable[i].getName());	
					
			
		}
		else
			System.out.println("SSN is not found.");
	}
	
	public static void main(String args[]){
		System.out.println("new HashTable");
		HashTable testTable = new HashTable();	
		testTable.put(983712614, "Amy Huang");	
		testTable.put(982712614, "Bob Huang");	
		testTable.put(982312614, "Clair Huang");
		testTable.put(982412614, "Dan Huang");	
		testTable.put(982422614, "Elaine Huang");	
		testTable.put(982432614, "Fionna Huang");	
		testTable.put(982442614, "George Huang");	
		testTable.put(982452614, "Hana Huang");	
		testTable.put(982462614, "Ian Huang");	
		testTable.put(982472614, "Jack Huang");	
		testTable.put(982482614, "Kate Huang");	
		testTable.put(982492614, "Louise Huang");	
		testTable.put(982402614, "Manny Huang");	
		testTable.printTable();
		System.out.println(" \n Testing the get() method");
		System.out.println("\t get(983712614) returns: " + testTable.get(983712614));
		System.out.println("\t get(982712614) returns: " + testTable.get(982712614));
		System.out.println("\t get(982432614) returns: " + testTable.get(982432614));
		System.out.println("\t get(982492614) returns: " + testTable.get(982492614));
		System.out.println("\t get(982402614) returns: " + testTable.get(982402614));
		System.out.println("\t get(100000001) returns: " + testTable.get(100000001));
		System.out.println("\t get(100000004) returns: " + testTable.get(100000004));
		System.out.println(" \n Testing the containsSSN() method");
		System.out.println("\t containsSSN(983712614) returns: " + testTable.containsSSN(983712614));
		System.out.println("\t containsSSN(982712614) returns: " + testTable.containsSSN(982712614));
		System.out.println("\t containsSSN(982432614) returns: " + testTable.containsSSN(982432614));
		System.out.println("\t containsSSN(982492614) returns: " + testTable.containsSSN(982492614));
		System.out.println("\t containsSSN(982402614) returns: " + testTable.containsSSN(982402614));
		System.out.println("\t containsSSN(100000001) returns: " + testTable.containsSSN(100000001));
		System.out.println("\t containsSSN(100000004) returns: " + testTable.containsSSN(100000004));
		System.out.println("\n size() returns: " + testTable.size()); 
		System.out.println("\n testing the remove method: ");
		System.out.println("After remove(100000001: ");
		testTable.remove(100000001);
		System.out.println("After remove(983712614) the new HashTable is" );
		testTable.remove(983712614);
		testTable.printTable();
		System.out.println("After remove(982412614) the new HashTable is" );
		testTable.remove(982412614);
		testTable.printTable();
		System.out.println("\n Testing the resizing method: rehash() by inputting many more value pairs");		
		testTable.put(983712614, "Amy Huang");	
		testTable.put(982412614, "Dan Huang");	
		testTable.put(183712614, "Nancy Huang");	
		testTable.put(182712616, "Oliver Huang");	
		testTable.put(182312532, "Penny Huang");
		testTable.put(182415735, "Queue Huang");	
		testTable.put(182423453, "Racheal Huang");	
		testTable.put(182436236, "Stan Huang");	
		testTable.put(182447907, "Tim Huang");	
		testTable.put(182450000, "Uniqlo Huang");	
		testTable.put(182463425, "Vivian Huang");	
		testTable.put(182472567, "Wisley Huang");	
		testTable.put(182485555, "Xixi Huang");	
		testTable.put(182492252, "Yiyi Huang");	
		testTable.put(182408769, "Zizi Huang");	
		testTable.put(383719593, "Amy Wang");	
		testTable.put(482713555, "Bob Wang");	
		testTable.put(582312235, "Clair Wang");
		testTable.put(624126562, "Dan Wang");	
		testTable.put(682422263, "Elaine Wang");	
		testTable.put(782432333, "Fionna Wang");	
		testTable.put(882442225, "George Wang");	
		testTable.put(912452672, "Hana Wang");	
		testTable.put(922462826, "Ian Wang");	
		testTable.put(932472514, "Jack Wang");	
		testTable.put(942482525, "Kate Wang");	
		testTable.put(952492166, "Louise Wang");	
		testTable.put(962402627, "Manny Wang");	
		testTable.printTable();
		
	}
	
}
