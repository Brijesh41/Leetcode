#include <algorithm>


class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        map<string,int> um;
        for(auto s: words){
            um[s]++;
        }
        struct comp{
            bool operator()(const pair<int,string>& p1, const pair<int,string>& p2){
                if(p1.first!=p2.first){return p1.first<p2.first;}
                
                return p1.second>p2.second;            
            }
        };
        priority_queue<pair<int,string>,vector<pair<int,string>>,comp> Q;
        for(auto it:um){
            Q.emplace(it.second,it.first);
        }
        vector<string> res;
        while (k-- > 0 && !Q.empty()) {
            res.push_back(Q.top().second);
            Q.pop();
        }
        return res;
        }
                       
};

