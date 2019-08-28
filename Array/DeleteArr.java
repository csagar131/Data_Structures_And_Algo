import java.util.Scanner;
import static java.lang.System.out;
class DeleteArr
{ 
 public static void main(String args[])
 {
  Scanner sc = new Scanner(System.in);
  out.println("Enter size of arr");
  int n = sc.nextInt();
  out.println("Enter array element");
  int arr[] = new int[n];
  for(int i=0;i<n;i++)
  {
   arr[i] =sc.nextInt();
  }
  
  out.println("enter at index to delete");
  int index = sc.nextInt();
  for(int i=0;i<n;i++)
  {
   if(i==index)
   {
    for(int j=i;j<n-1;j++)
	{
	  arr[j] = arr[j+1];
	}
	break;
   }
  }
  
  out.println("array after deletion");
  for(int i=0;i<n-1;i++)
  {
   out.println(arr[i]+" ");
  }
  sc.close();
 }
} 
  