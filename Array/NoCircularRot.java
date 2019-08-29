import java.util.Scanner;
import static java.lang.System.out;
public class NoCircularRot
{
     public static void main(String args[])
     {
         Scanner sc = new Scanner(System.in);
         out.println("enter no. array");
         int n = sc.nextInt();
         out.println("Enter Array element");
         int arr[] = new int[n];
         for(int i=0;i<n;i++)
         {
             arr[i] = sc.nextInt();
         }
         int k = 0;
        for(int i=1;i<n;i++)
        {
            if(arr[i-1] >= arr[i])
            k = i;
        }
         out.println("Array rotated "+k+" times");



         sc.close();
     }
}