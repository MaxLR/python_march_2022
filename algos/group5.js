/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcddd";
  const expected1 = "a4b2c1d3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";
  
  const str7 = "aaabbbaaa";
  const expected7 = "a3b3a3"

  //if expected.length == str.length return str
  //counter = 0
  //expected = ""0
  // for loop if arr[i] == arr[i +1] counter ++
  //    if arr[i] != arr[i + 1]
//          counter = 0 (resets counter)
function encodeStr(str) {
    var new_str = "";
    var counter = 1;
    //counter
    for(var i=0; i<arr.length; i++){
        if(str[i] == str[i+1]){
            counter++;
        } 
        if (str[i] != str[i+1]){
            new_str += str[i];
            new_str += counter
            //reset
            counter = 1
        }
    }
    if (new_str.length == str.length) {
        return str
    } else {
        return new_str
    }
}

console.log(encodeStr(str4))

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