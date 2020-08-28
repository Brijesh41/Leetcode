class Solution {
   HashSet<Integer> visited;
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        
        visited  = new HashSet<Integer>();
        
        int nodes = rooms.size();
            
                dfs(rooms,0);
            
        
        // for(Integer s:visited){
        //     System.out.println(s);
        // }
        return visited.size()==nodes;
    }
    public void dfs(List<List<Integer>> rooms,int u){
        if(visited.contains(u)){
                return ;
            }
        
        visited.add(u);
        
        for(int i =0;i<rooms.get(u).size();i++){
            int v = rooms.get(u).get(i);
            dfs(rooms,v);
        }
    }
    
}