<?php
$handle = fopen ("php://stdin","r");
$i = 4;
$d = 4.0;
$s = "HackerRank ";
// Declare second integer, double, and String variables.
$var1 = 12;
$var2 = 4.0;
$var3 = "is the best place to learn and practice coding!";
// Read and save an integer, double, and String to your variables.


// Print the sum of both integer variables on a new line.
$result = $i + $var1;
echo $result;
echo "</br>";

// Print the sum of the double variables on a new line.
$sol = $d + $var2;
echo $sol;
echo "</br>";

// Concatenate and print the String variables on a new line
$ans = $s.$var3;
echo $ans;
// The 's' variable above should be printed first.

fclose($handle);
?>