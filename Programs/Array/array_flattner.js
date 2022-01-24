function flat(arr,out){
	arr.forEach(element => {
		if(typeof(element)==='object'){
			flat(element,out)
		}
		else{
			out.push(element)
		}
	});
	return out
} 

console.log(flat([1,[2,[3,[9,[67,90]]],4,[87,[5,9,[4]]]],[5]],[]))
