import java.util.Scanner; //imports the ability to get user input 

public class AreaOfCircle {  // class that defines what we are doing 

	public static void main(String[] args) {  // main method for the area of a circle 
		System.out.println("Enter Your Favorite Number In The World: "); // displays to the user to enter there favorite number 
		Scanner sn = new Scanner(System.in);  // takes in the number and obtains the variable 
		Double raduis = sn.nextDouble();  // takes the number and turns it to a double variable for use in the calculations in the next line
		Double area = Math.PI * raduis * raduis; // calculates the area of a circle 
		System.out.println("The Area Of The Circle From Your Favorite Number Is = "+area); // displays the area of the circle 
	}
}