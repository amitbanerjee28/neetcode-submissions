class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freqMap = new HashMap<>();
        for(int n : nums){
            freqMap.put(n,freqMap.getOrDefault(n,0)+1);
        }

        List<Integer>[] bucket = new List[nums.length +1];
        for(Map.Entry<Integer,Integer> entry : freqMap.entrySet()){
            int frequency = entry.getValue();
            if(bucket[frequency] == null){
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(entry.getKey());
        }
        int index =  0 ;
        int[] rs = new int[k];
        for(int i = bucket.length - 1; i>= 1 && index < k ;i--){
            if(bucket[i] != null){
                for(int n : bucket[i]){
                    rs[index++] = n;
                    if(index == k){
                        break;
                    }
                }
            }
        }
        return rs;
    }
}
