import java.util.Scanner;
import static java.lang.System.out;
class InsertArr
{
 public static void main(String args[])
 {
  Scanner sc = new Scanner(System.in);
  out.println("Enter size of arr");
  int n = sc.nextInt();
  out.println("Enter array element");
  int arr[] = new int[n+1];
  for(int i=0;i<n;i++)
  {
   arr[i] =sc.nextInt();
  }
  
  out.println("enter at index to insert");
  int index = sc.nextInt();
  out.println("Enter element");
  int ele = sc.nextInt();
  
  for(int i=n-1;i>=index;i--)
  {
   arr[i+1] = arr[i];
  }
  arr[index] = ele;
  out.println("array after insertion");
  for(int i=0;i<arr.length;i++)
  {
   out.println(arr[i]+" ");
  }
 }
} 