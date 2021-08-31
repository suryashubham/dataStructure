const s = 'babad';
let largest_pallindrome = '';
visited = {}

function _lps(input_string) {
    if (!visited[input_string]) {

        visited[input_string] = true;
        let p_flag = true;

        if (input_string.length == 0) return;
        if (input_string.length == 1) return input_string;

        for (let i = 0, j = input_string.length - 1; i < j; i++, j--) {
            if (input_string[i] == input_string[j]) {
                i++;
                j--;
            }
            else {
                p_flag = false;
                break;
            }
        }
        if (p_flag == false) {
            let s1 = _lps(input_string.slice(1))
            let s2 = _lps(input_string.slice(0, input_string.length - 1))
            if (s1 && s1.length>largest_pallindrome.length) largest_pallindrome=s1;
            if (s2 && s2.length>largest_pallindrome.length) largest_pallindrome=s2;
        }
        return p_flag?input_string:false;
    }
}

_lps(s);
console.log(largest_pallindrome);
