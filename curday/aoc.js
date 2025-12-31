let keyQueue = [];
var keyResolve;
var keyPromise = new Promise((res, rej) => {
  keyResolve = res;
});
var stdin;
import fs from "fs";
import { exec, spawn } from "child_process";
import { JSDOM } from "jsdom";
const session = readFile("../state/session");
var state = JSON.parse(readFile("../state/state.json"));

var filechangeResolve;
var filechange = new Promise((res) => {
  filechangeResolve = res;
});

let colors = {
  header: "\x1b[95m",
  blue: "\x1b[94m",
  cyan: "\x1b[96m",
  green: "\x1b[92m",
  warning: "\x1b[93m",
  fail: "\x1b[91m",
  end: "\x1b[0m",
  bold: "\x1b[1m",
  underline: "\x1b[4m",
};

function a() {}

(async () => {
  const time = new Date();
  const month = time.getMonth() + 1; // months from 1-12
  const day = time.getDate();
  const year = time.getFullYear();
  // console.log(month, day, year);
  let upcoming = false;

  //  url = "http://localhost";

  // console.log(`session=${session}`);

  setupStdin();
  setupWatchdog();

  // on any data into stdin
  if ((month == 11 && day == 30) || (month == 12 && day < 25)) {
    let key = await keyinput(
      "Are you playing the upcoming challenge? (anykey/n) "
    );
    upcoming = key != "n";
  }

  let newday = false;

  if (upcoming) {
    state = {
      year: year,
      day: (day + 1) % 30,
    };

    // let cur = Math.floor(Date.now() / 1000);

    while (1) {
      let d = new Date(
        new Date().toLocaleString("en-US", {
          timeZone: "US/Eastern",
        })
      );

      if (d.getDate() == state.day) break;

      let timeleft = 24 * 60 * 60;
      let deltatime =
        60 * 60 * d.getHours() + 60 * d.getMinutes() + d.getSeconds();
      // deltatime = timeleft - 5 + Math.floor(Date.now() / 1000) - cur;
      timeleft -= deltatime;

      let time = "";
      for (let i = 0; i < 3; i++) {
        let number = `${timeleft % 60}`;
        if (number.length < 2) number = `0${number}`;
        time = `${number}:` + time;
        timeleft /= 60;
        timeleft = Math.floor(timeleft);
      }

      time = time.slice(0, time.length - 1);

      process.stdout.write(`\x0dCountdown to midnight EST: ${time}`);
      await sleep(1000);
    }

    process.stdout.write(
      `\nSleeping five more seconds because I'm reading the puzzle in the first five seconds, not looking at the input.\n`
    );
    await sleep(5000);
  } else {
    newday = (await keyinput("Are you starting a new day? (y/anykey) ")) == "y";
    if (newday) {
      let year = await numinput("What year? ");
      let day = await numinput("What day? ");
      let part = (await keyinput("Part two? (y/anykey) ")) == "y";
      state = {
        year: year,
        day: day,
        part: part ? 2 : 1,
      };
    }
  }

  if (upcoming || newday) {
    await fs.writeFileSync("../state/state.json", JSON.stringify(state));
  }

  async function submit(answer) {
    console.log(
      `Submitting ${colors.blue + colors.bold}${answer}${colors.end} for part ${
        colors.blue + colors.bold
      }${state.part}${colors.end}...`
    );
    let url = `https://adventofcode.com/${state.year}/day/${state.day}/answer`;
    let data = { level: state.part, answer };
    let response = await get(url, {
      method: "POST",
      headers: {
        Cookie: `session=${session};`,
        "User-Agent":
          "github.com/sponege/aoc by apples@jappl.es (still testing right now so sorry)",
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams(data),
    });
    /*
    if (response.status != 200) {
      console.log(`uh oh server responded with code ${response.status}`);
      return;
    }
		*/
    if (!response.includes("main")) {
      console.log(response);
      console.log(
        "UH OH RED ALERT (wtf wrong with advent of code servers this time??? hopefully its not your wifi)"
      );
      return;
    }
    let dom = new JSDOM(response);
    console.log(dom.window.document.querySelector("main").textContent.trim());
    if (response.includes("That's the right answer")) {
      let fileName = `../${state.year}/${state.day.toString().padStart(2, '0')}.p${state.part}.py`
      if (fs.existsSync(fileName)) fileName = `../${state.year}/${state.day.toString().padStart(2, '0')}.p${state.part}.${crypto
          .getRandomValues(new Uint8Array(1))[0]
          .toString(16)}.py`;
      fs.writeFileSync(
        fileName,
        fs.readFileSync("./curday.py").toString("utf8")
      );
      state.part = 2;
      await fs.writeFileSync("../state/state.json", JSON.stringify(state));
    }
    if (response.includes("this victory or")) {
      console.log("gg");
      process.exit();
    }
  }

  let inputPath = `inputs/${state.year}/${state.day
    .toString()
    .padStart(2, "0")}.txt`;
  let input = "No input retrieved!!";
  let resultText = "";
  if (state.part == null) state.part = 1;

  if (!fs.existsSync(inputPath)) {
    console.log("Downloading input...");
    let url = `https://adventofcode.com/${state.year}/day/${state.day}/input`;

    input = await get(url, {
      headers: {
        Cookie: `session=${session};`,
        "User-Agent":
          "github.com/sponege/aoc by apples@jappl.es (still testing right now so sorry)",
      },
    });
    
    let path = `inputs/${state.year}`
    if (!fs.existsSync(path)) fs.mkdirSync(path)
    fs.writeFileSync(inputPath, input);
    fs.writeFileSync("./curday-input.txt", input);
    resultText = "Downloaded input";
  } else {
    console.log("Reading input from file...");
    input = await readFile(inputPath);
    resultText = "Got input from file";
  }
  fs.writeFileSync("./curday-input.txt", input);
  console.log("-".repeat(20));
  if (input.length < 1000) console.log(input);
  else console.log(`(${input.length} bytes of input)`);
  console.log("-".repeat(20));
  console.log(resultText);

  let file = "curday.py";
  let modifiedFile;
  let _;

  let child, output, answer, type, changed, code;

  while (1) {
    let killed = false;
    for (let [curInp, inputType] of [
      [input, "real input"],
      [readFile("./test.txt"), "test input"],
    ]) {
      if (killed) break;
<<<<<<< HEAD
=======
      if (curInp.length == 0) continue;
>>>>>>> ee7cd9e8adec6edc9eab2467ad577fa203a410ff
      console.log(`Running ${file} with ${inputType}...`);
      console.log("-".repeat(20));
      child = runCode(file, curInp, inputType == "test input");
      // output = ""; // i dont even use this variable, im dumb, i created this variable during development and forgot about it
      let curans = null;

      child.stdout.on("data", (data) => {
        let out = data.toString().trim();
        for (let line of out.split`\n`) {
<<<<<<< HEAD
          if (line.includes("ans")) curans = out.split`:`[1].trim();
=======
          if (line.includes("ans")) curans = out.split`ans:`[1].trim();
>>>>>>> ee7cd9e8adec6edc9eab2467ad577fa203a410ff
          else {
            // output += out;
            console.log(line);
          }
        }
      });

      child.stderr.on("data", (data) => {
        console.error(data.toString());
      });

      code = null;
      changed = false;

      while (1) {
        [type, code] = await Promise.race([
          new Promise((res) => child.on("close", (a) => res(["exit", a]))),
          new Promise((res) => keyPromise.then((a) => res(["key", a]))),
          // filechange,
        ]);
        if (type == "change") changed = true;
        if (changed) {
          console.log("> File change detected so killing program");
          modifiedFile = "Some file"; // no time to fix bug
        }
        if ((type == "key" && code == "t") || changed) {
          child.kill();
          killed = true;
          console.log("> Killed process (from aoc.js)");
        }
        if (type == "exit") break;
      }
      console.log("-".repeat(20));

      if (code != null) console.log(`Program exited gracefully`);
      else console.log(`Program was terminated`);

      if (curans != null) {
        console.log(
          `Found answer ${colors.blue + colors.bold}${curans}${colors.end}`
        );
        if (inputType == "real input") answer = curans;
      }
    }

    if (!changed) {
      let areyousure = 0;
      console.log("Waiting for file changes...\n");
      while (1) {
        let [type, value] = await Promise.race([
          filechange,
          new Promise((r) => keyPromise.then((k) => r(["key", k]))),
        ]);
        if (type == "key") {
          if (value == "s") {
            areyousure++;
            if (areyousure < 2) {
              console.log(
                `Are you sure you want to submit ${
                  colors.blue + colors.bold
                }${answer}${colors.end} for part ${colors.blue + colors.bold}${
                  state.part
                }${colors.end}?`
              );
            } else {
              let response = await submit(answer);
              console.log("\nWaiting...");
              areyousure = 0;
              continue;
            }
          }
        } else {
          if (type == "change") {
            modifiedFile = value;
            areyousure = 0;
            break;
          }
        }
      }
    }
    console.log(`${modifiedFile} was modified`);
    await sleep(10);
  }
})().then(process.exit);

function setupStdin() {
  stdin = process.stdin;
  // without this, we would only get streams once enter is pressed
  stdin.setRawMode(true);

  // resume stdin in the parent process (node app won't quit all by itself
  // unless an error or process.exit() happens)
  stdin.resume();

  // i don't want binary, do you?
  stdin.setEncoding("utf8");

  stdin.on("data", function (key) {
    // ctrl-c ( end of text )
    if (key === "\u0003") {
      process.exit();
    }
    // write the key to stdout all normal like
    // process.stdout.write(key);
    //
    keyResolve(key);
    keyPromise = new Promise((res) => {
      keyResolve = res;
    });
  });

  stdin = {
    getKey: () => {
      return keyPromise;
    },
  };
}

let watchedFiles = ["curday.py", "test.py", "util.py", "test.txt"];

function setupWatchdog() {
  fs.watch("./", (eventType, filename) => {
    if (eventType != "change" || !watchedFiles.includes(filename)) return;
    let data = [eventType, filename];
    // console.log(data);
    filechangeResolve(data);
    filechange = new Promise((res) => {
      filechangeResolve = res;
    });
  });
}

async function keyinput(str) {
  process.stdout.write(str);
  let key = await stdin.getKey();
  process.stdout.write("\n");
  return key;
}

async function input(str = "") {
  process.stdout.write(str);
  let inp = "";
  let key = await stdin.getKey();
  while (key != "\x0d") {
    process.stdout.write(key);
    inp += key;
    key = await stdin.getKey();
  }
  process.stdout.write("\n");
  return inp;
}

async function numinput(str) {
  return Number(await input(str));
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

function readFile(fname) {
  return fs.readFileSync(fname).toString().trim();
}

async function get(url, options) {
  /*
  return new Promise((r) => {
    let result = "";
    let req = https.request(options, (res) => {
      res.setEncoding("utf8");
      res.on("data", (chunk) => {
        result += chunk;
      });

      res.on("end", () => {
        r(result.trim());
      });
    });
    req.on("error", console.log);
    req.end();
  });
	*/
  let res = await fetch(url, options);
  let text = await res.text();
  return text.trim();
}

function runCode(file, inp, test) {
  let child = spawn("pypy3", [file, test ? "t" : ""]);
  child.stdin.write(inp);
  child.stdin.end();

  /*
  return new Promise((res) => child.on("close", res));
	*/
  return child;
}
