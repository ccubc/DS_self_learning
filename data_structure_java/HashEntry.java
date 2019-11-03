package jsjf;

public class HashEntry {
	private int SSN;
	private String name;
	
	HashEntry(int SSN, String name){
		this.SSN = SSN;
		this.name = name;
	}
	
	public String getName(){
		return name;
	}
	
	public void setName(String name){
		this.name = name;
	}
	
	public void setSSN(int SSN){
		this.SSN = SSN;
	}

	public int getSSN(){
		return SSN;
	}
}
