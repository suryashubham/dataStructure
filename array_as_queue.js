input_arr = [2, 3, 4, 5, 6]
let i = 0;
let j = input_arr.length

function dequeue() {
  if (input_arr.length == 0) {
    return "Empty Queue"
  }

  if (i < j) {
    return input_arr[i++]
  }
  return "No more item to be dequeued"
}
