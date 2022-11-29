// function linear(item, arr) {
//   let ind = 0;
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] == item) {
//       ind = i;
//     }
//   }
//   return ind;
// }
// console.log(linear(5, [3, 6, 1, 2, 4, 5]));

// function binary(arr, item) {
//   let low = 0;
//   let high = arr.length;
//   let found = false;
//   while (!found) {
//     console.log(`for low ${low}, for high ${high}`);
//     let midValue = parseInt((low + high) / 2);
//     // console.log(midValue);
//     if (arr[midValue] == item) {
//       //   console.log("first case", arr[midValue]);
//       console.log("INDEX", midValue);

//       return midValue;
//     } else if (arr[midValue] > item) {
//       high = midValue;
//       //   console.log(arr[midValue]);
//       //   console.log("second case");
//     } else if (arr[midValue] < item) {
//       {
//         low = midValue;
//         console.log(low);
//         console.log(arr[midValue]);

//         // console.log("third case");
//       }
//     } else {
//       //   console.log("outside");
//     }
//   }
// }
// binary([2, 4, 7, 8, 9, 10, 11, 13, 14, 17], 11);
