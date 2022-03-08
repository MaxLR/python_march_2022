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

// 1 make a function that takes in 2 parameters
// create an empty string for the output
// array length = 1 or 0? return arr[0] or empty string
// loop through the array
    // push stuff into my output from the array
    // push separator into my output from the array
// return output



/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {
    
}


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
function acronymize(str) {}


// create a function that takes in a string
// create an empty output
// split on " "
// loop through the resulting array
    //pass the string[0].upper() into output


//create a function that takes in a string
// create empty output
// loop through input string
    // if index == 0 && string[index] != " ", push string[index] into output
    // if current letter is a space, pass string[index + 1].upper() to output
// return my output