import java.util.Scanner;
import static java.lang.System.out;
class DeleteArr
{ 

 static boolean checkPalindrom(int num)
 {
  
    int n = num;
    int rev = 0;
    while(n>0)
    {
       int a = n % 10;
       rev = rev * 10+ a;
       n = n / 10; 
    }
    if(rev==num)
    return true;
    return false;
 }
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
  int max = 0;
  for(int i=0;i<n;i++)
  { 
      int count = 0;
      if(checkPalindrom(arr[i]))
      {
              //implementation remaining
      }
  }
  sc.close();
 }
}