// let stdin = process.stdin;
// // without this, we would only get streams once enter is pressed
// stdin.setRawMode(true);

// // resume stdin in the parent process (node app won't quit all by itself
// // unless an error or process.exit() happens)
// stdin.resume();

// // i don't want binary, do you?
// stdin.setEncoding("utf8");

// stdin.on("data", function (key) {
//   // ctrl-c ( end of text )
//   if (key === "\u0003") {
//     process.exit();
//   }
//   // write the key to stdout all normal like
//   // process.stdout.write(key);
//   //
//   console.log(key.split``.map((c) => c.codePointAt(0)));

//   //^v><
// });

// function log(s) {
//   let doThing = (thing) => thing.map((c) => String.fromCharCode(c)).join("");
//   /* [ 27, 91, 65 ]
//   [ 27, 91, 66 ]
//   [ 27, 91, 67 ]
//   [ 27, 91, 68 ]*/
//   process.stdout.write(
//     doThing([27, 91, 65]).repeat(5) + "\n" + s + doThing([27, 91, 66])
//   );
// }

function log(str) {
  readline.cursorTo(process.stdout, 0, 0);
  readline.clearScreenDown(process.stdout);
  lines.unshift(str);
  lines = lines.slice(0, BOTTOM_ROW);
  for (let row = 0; row < Math.min(BOTTOM_ROW, lines.length); row++) {
    process.stdout.write(lines[row]);
    readline.cursorTo(process.stdout, 0, row + 1);
  }
  readline.cursorTo(process.stdin, 0, BOTTOM_ROW);
}
console.log("> ");
log("asdf");
