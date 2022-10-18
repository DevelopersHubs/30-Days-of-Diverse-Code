function main() {
    var i = 4
    var d = 4.0
    var s = "HackerRank "
    // Declare second integer, double, and String variables.

    // Read and save an integer, double, and String to your variables.
    let num1 = prompt('enter int');
    let num2 = prompt('enter float');
    let num3 = prompt('enter string')
    // Print the sum of both integer variables on a new line.
    console.log(i + parseInt(num1));
    // Print the sum of the double variables on a new line.
    result = d + parseFloat(num2);
    console.log(result.toFixed(1));    
    // console.log(Math.round(parseFloat(result) * 10) / 10);
    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    console.log(`${s}${num3}`);

}
main()