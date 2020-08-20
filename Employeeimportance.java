/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        
        Map<Integer,Employee> map = new HashMap<Integer,Employee>();
        for(Employee e: employees){
            map.put(e.id,e);
        }
        
        Queue<Employee> q = new LinkedList<Employee>();
        q.offer(map.get(id));
        int total = 0;
        while(!q.isEmpty()){
            Employee e = q.poll();
            total+=e.importance;
            for(int i: e.subordinates){
                q.offer(map.get(i));
            }
            
        }
        
        return total;
        
    }
}