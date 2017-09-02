import java.util.Scanner;
public class Hello {
	public static void main(String[] args)
	{
	Scanner sc=new Scanner(System.in);
	int num=sc.nextInt();
	String s ="Hello";
	int i;
        if(num>0)
	{
	for(i=0;i<5;i++)
	  System.out.println(s);
	}
	else
	 System.out.println("Invalid");
	}
}
