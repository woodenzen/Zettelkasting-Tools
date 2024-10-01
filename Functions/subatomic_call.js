/**
* @returns {(string|bool)} - The extracted subatomic, if found, or false if there's no match.
*/

const subatomic = (content) => {
 const needle = "Subatomic: ";
 const lines = content.split('\n');

 for (const line of lines) {
   if (line.includes(needle)) {
     // Remove the prefix, return the rest.
     return line.split(needle)[1];
   }
 }

 return false;
}




// To use, call subatomic(contentsOfANote), e.g. in a loop over all/some of your notes.

