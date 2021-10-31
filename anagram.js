//author: surya shubham kumar
const s = "silent";
const t = "listen";


function get_count(data){
   let res = {}
   for(let i=0;i<data.length;i++){
    if(data[i] in res) res[data[i]] = res[data[i]]+1
    else res[data[i]] = 1
  }
  return res
}

function is_anagram(p,q){
  console.log(p,q)
  for(let i in p){
    if(q[i] !== p[i]) return false
  }
  return true
}

console.log(is_anagram(get_count(s),get_count(t)))
