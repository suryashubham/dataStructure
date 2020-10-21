nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maximum_value = nums[0]
max_i = 0;
max_j = 0;

function find_max_sum_sub_array() {
    flag = false;
    sum = 0
    for (i = 0, j = 1; i < nums.length && j < nums.length;) {
        if (flag == false) {
            sum = nums[i] + nums[j];
            if (sum > maximum_value) {
                maximum_value = sum;
                max_i = i;
                max_j = j;
                j++;
                flag = true
            }
            else {
                i = i + 1;
                j = j + 1
                sum = 0
                flag = false;
            }
        }
        else {
            sum = sum + nums[j];
            if (sum > maximum_value) {
                maximum_value = sum;
                max_j = j;
                max_i = i;
                j++;
            }
            else {
                i = i + 1;
                j = i + 1;
                sum = 0;
                flag = false
            }
        }

    }
}
find_max_sum_sub_array()
console.log(maximum_value)
console.log("start index:" + max_i);
console.log("end index:" + max_j);