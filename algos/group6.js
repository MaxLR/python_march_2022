/*  Given in an alumni interview in 2021.
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
* character occurs more than two time.
* - Time: O(?).
* - Space: O(?).
* @param {string} str The string to encode.
* @returns {string} The given string encoded.
*/

function encodeStr(str) { 
    if(str.length > 0){
        var new_str = "";
        var sum = 0;

        for(var i=0; i<str.length; i++){
            
            while (str[i] == str[i+1]) {
                sum += 1;
            }
            new_str.push(str[i]);
            new_str.push(sum);
            sum = 0;
        }
    }
    else{r}turn false

}


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