//#TODO:optimization, as for large i/p Time Limit is getting exceeded
var getSumAbsoluteDifferences = function(nums) {
    result = []
    k= 0
   for(i=0,j=0;i<nums.length&&j<nums.length;){
    k = k + Math.abs(nums[i]-nums[j])
    if(j<nums.length-1){
        j++
    }
    else if(j == nums.length-1){
        i++;
        j = 0;
        result.push(k)
        k=0
    }
   }
   return result
};
