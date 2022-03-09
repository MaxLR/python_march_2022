/* 
Given in an alumni interview in 2021.
String Encode
You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
// */
// loop through string and count each character, return 
const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";
function look_boy(str1){
    new_list= []
    for(var i = 0; i < str.length-1; i++){
        if str[i] === str[i+1]{
            count =
        }
        else new_list.push([i]){
             }
    }
console.log(look_boy)
}
// let group 2 know if this works plz

new_string = ""
string = str1
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count = count + 1
    else:         
        new_string =  new_string + string[i] + str(count)
        count = 1
new_string = new_string + string[i+1] + str(count)
print(new_string)


function compress(string){
  let compressed = ""
  let stringArray = string.split("")
  for (let i = 0; i < stringArray.length; i++){
      let count = 1 
      let letter = stringArray[i]
      while (i < stringArray.length - 1 && stringArray[i] === stringArray[i + 1] {
    count++
    i++
    }
  if (count === 1){
  compressed += letter 
    } else { 
    compressed =+ letter + count}
  }
  }
  
  return compressed
  }
  

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

const str7 = "aaabbbaaa";
const expected7 = "a3b3a3"

def encodeStr():

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs only if the
 * character occurs more than two time.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
 */

function encodeStr(str) { }



//-----------------------------------------------------------------------------------------------------



/* 
  String Decode  
*/

const str5 = "a3b2c1d3";
const expected5 = "aaabbcddd";

const str6 = "a3b2c12d10";
const expected6 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) { }

  
module.exports = { decodeStr };