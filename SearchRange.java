class Solution {
    public int[] searchRange(int[] nums, int target) {
        if(nums.length==0){
            int[] a = new int[2];
            a[0]=-1;
            a[1]=-1;
            return a;
        }
        
        int a = leftbinarysearch(nums,target);
        
        int b = rightbinarysearch(nums,target);
        
        int[] ans = new int[2];
        ans[0] = a;
        ans[1] = b;
        return ans;
        
    }
    
    public int leftbinarysearch(int[] nums, int target){
        
        int l =0;
        int r = nums.length-1;
        
        while(l<r){
            int mid = (int)((l+r)/2);
            
            if(target>nums[mid]){
                l= mid+1;
            }
            else{
                r = mid;
            }
        }
        
        if(nums[l]==target){
            return l;
        }
        else{
            return -1;
        }
        
        
        
    }
    
    public int rightbinarysearch(int[] nums,int target){
        
        int l =0;
        int r =nums.length-1;
        
        while(l<r){
            int mid =  (int)((l+r+1)/2);
            // System.out.println(mid+""+l+""+r);
            if(nums[mid]>target){
                r=mid-1;
            }
            else{
                l=mid;
            }
        }
        if(nums[l]==target){
        return l;
        }   
        else{return -1;}
    }
    
    
}