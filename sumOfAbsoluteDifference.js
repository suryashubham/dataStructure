var getSumAbsoluteDifferences = function(nums) {
    result = []
    biggerSum = 0
    smallerSum = 0
    for(i=0;i<nums.length;i++){
        biggerSum=biggerSum+nums[i]
    }
    for(i=0;i<nums.length;i++){
        const num = nums[i]
        biggerSum-=num
        const smalldiff = (num*i)-smallerSum
        const bigdiff = biggerSum-num*(nums.length-1-i)
        result.push(smalldiff+bigdiff)
        smallerSum += num
    }
    return result    
};
