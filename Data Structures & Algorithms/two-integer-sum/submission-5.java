class Solution {
    Map<Integer, Integer> compMap = new HashMap<>();

    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if(compMap.containsKey(complement)){
                return new int[] {compMap.get(complement), i};
            }
            else{
                compMap.put(nums[i], i);
            }
        }
        return new int[] {0,0};
    }
}
