function longest_substring(s) {
    maximum = 0
    temp_list = []
    if (s.length > 0) {
        temp_list.push(s[0])
        maximum=s.length;
    }
    if (s.length == 0) {
        return 0
    }
    else {
        for (i = 0, j = 1; i < s.length && j < s.length;) {
            if (!(temp_list.includes(s[j]))) {
                temp_list.push(s[j++]);
                if (temp_list.length > maximum) {
                    maximum = temp_list.length
                }
            }
            else {
                temp_list = temp_list.slice(1)
                i++;
            }
        }
    }
    return maximum
}
