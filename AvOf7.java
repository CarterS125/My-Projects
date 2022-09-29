import java.util.HashMap; // imports the properties for java to use HashMaps 

public class AvOf7 { // class that defines and stores our program 

	public static void main(String[] args) {  // main method of the program entailing what we will do 
		
		int test1 = 88;  
		int test2 = 79;
		int test3 = 65;
 		int test4 = 100;  // these are the different test scores displayed across 7 different integers 
		int test5 = 96;
		int test6 = 80;
		int test7 = 74;
		
		int[] nums = {88, 79, 65, 100, 96, 80, 74};  // integers that will be calculated for the average 
		double sum = 0;	        
			int i=0;
		        while(i < nums.length) { // while loop that iterates through the integers and gets an average for them 
		            sum += nums[i];    // code that does the math portion of the program  
		            i++;			// code that does the math portion of the program 
		        }
		
		HashMap<String, Integer> AvOf7 = new HashMap<String, Integer>();
		AvOf7.put("test1", 88);
		AvOf7.put("test2", 79);
		AvOf7.put("test3", 65);    // HashMap that stores the keys and values for each different test and its score 
		AvOf7.put("test4", 100);
		AvOf7.put("test5", 96);
		AvOf7.put("test6", 80);
		AvOf7.put("test7", 74);
		
		
		double average = (sum / nums.length);  // variable that evaluates the average for the tests
		
		System.out.println(AvOf7);  // print statement for the HashMap that displays all tests and their scores 
		System.out.println("Avof7 : "+average); // print statement that shows the average for all 7 test scores 
	}

}