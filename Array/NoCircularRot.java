import java.util.Scanner;
import static java.lang.System.out;
public class NoCircularRot
{
    public static int findRotation(int arr[])
    {   int res = 0;
        int n = arr.length;
        int low=0;
        int high=n-1;
        while(true)
        {
            int mid = (low+high)/2;
               
            if(arr[low] <= arr[high])
            {
            
             res = low;
             break;
            }
            /*
            need to check it again
            */
            
            int next = (mid+1) % n;
            int prev = (mid-1+n) % n;
                
            if(arr[mid] <= arr[next] && arr[mid] >= arr[prev])
            {  
               
                res = mid;
                break;
            }
                
            else if(arr[mid] <= arr[high])
                high = mid-1;
            else if(arr[mid] >= arr[low])
                 low =mid+1;    
        }
        return res;

    }

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

        
         int res = findRotation(arr);
         out.println("number of rotation is "+res);
        
         /*
         int k = 0;
        for(int i=1;i<n;i++)
        {
            if(arr[i-1] >= arr[i])
            k = i;
        }
         out.println("Array rotated "+k+" times");
         */
         sc.close();
     }
}