/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
// function join(arr1, separator) {
//   for(var i=0; i<arr1.length; i++){
//     return arr1[i] + separator1 + arr1[i + 1]
//   }
// }
// console.log(join)

function join(arr, separator) {
  for(var i=0; i<arr.length; i++){
    if(arr.length<=1){
      return arr[i];
    }
    else{
      return arr[i] + separator + arr[i + 1] + separator + arr[i + 2];
    }
  }
}
console.log(join(arr1,separator1))



function x(a,b){
  x=a+b
}
x(2,3)
//-------------------------------------------------------------------------------------------------------------------------


/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected6 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night! ";
const expected7 = "LFNYISN";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The given str converted into an acronym.
 */
function acronymize(str) {
  for(var i = 0; i<str.length; i++){
    if (str.charAt(i) === ' '){
      v = true;
    }
    else if (str.charAt(i) != ' ' && v == true){
      result += (str.charAt(i));
      v = flase;
    }
  }
  return result.toUppercase();
}

console.log(str1)