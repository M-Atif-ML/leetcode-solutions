class Solution {
public:
    int sum(vector <int>arr){
        return accumulate(arr.begin(), arr.end(), 0);
    }
    int min(vector <int > arr){
        return (arr[0] < arr[1]) ? arr[0] :arr[1]; 
    }
    int max(vector<int> arr ){
        return (arr[0] > arr[1]) ? arr[0] :arr[1]; 
    }
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        sort(intervals.begin(), intervals.end());

  
        for(int i= 0 ;i < intervals.size()-1;i++){
            if((intervals[i+1][0] - intervals[i][1]) <= 0 || sum(intervals[i]) ==sum(intervals[i+1])){
                cout<<"Hello";
                int min_ = 0;
                min_ = min(intervals[i]);
                min_ = (min(intervals[i+1]) < min_) ? min(intervals[i+1]) : min_;
                int max_ = 0;
                max_ = max(intervals[i]);
                max_ = (max(intervals[i+1]) > max_) ? max(intervals[i+1]) : max_;
                intervals[i][0] = min_;
                intervals[i][1] = max_;
                intervals.erase(intervals.begin()+(i+1));
                i--;

            }
            
  
        }

        return intervals;
    }
};
