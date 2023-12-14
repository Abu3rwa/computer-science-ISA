function sort(arr) {
  let sorted = false;
  while (!sorted) {
    sorted = true;
    for (let i = 0; i <= arr.length; i++) {
      if (arr[i] > arr[i + 1]) {
        sorted = false;
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
      }
    }
  }
  return arr;
}
console.log(sort([2, 999, 3, 2, 0, 33, 11, 5]));
