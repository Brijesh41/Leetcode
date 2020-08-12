class Solution {
    
    public int[] odd(int n, int[] arr){
        int x = (int)(n/2);
        x = x*-1;
        for(int i =0;i<arr.length;i++){
            arr[i] = x;
            x+=1;
        }
        
        return arr;

        }
    
    public int[] sumZero(int n) {
        if(n==1){return new int[1];}
        
        if(n%2==1){
            int[] arr = new int[n];
            return odd(n,arr);
            }
        else{
            // ArrayList<Integer> a = new ArrayList<Integer>();
            int[] arr = new int[n];
            arr = odd(n-1,arr);
          
            arr[n-1] = (int)(n/2)+1;
            arr[0] = arr[0]-(int)(n/2)-1;
            return arr;
            }
        // return arr;
        }
}