let keyQueue = [];
var keyResolve;
var keyPromise = new Promise((res, rej) => {
  keyResolve = res;
});
var stdin;
import fs from "fs";
import fetch from "node-fetch";
import { exec, spawn } from "child_process";
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

  let inputPath = `inputs/${state.year}/${state.day
    .toString()
    .padStart(2, "0")}.txt`;
  let input = "No input retrieved!!";
  let resultText = "";
  if (state) state.part = 1;

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

    fs.writeFileSync(inputPath, input);
    resultText = "Downloaded input";
  } else {
    console.log("Reading input from file...");
    input = await readFile(inputPath);
    resultText = "Got input from file";
  }
  console.log("-".repeat(20));
  console.log(input);
  console.log("-".repeat(20));
  console.log(resultText);

  let file = "curday.py";
  let _;

  while (1) {
    console.log(`Running ${file}...`);
    console.log("-".repeat(20));
    let child = runCode(file, input);
    let output = "";
    let answer = null;

    child.stdout.on("data", (data) => {
      let out = data.toString().trim();
      if (out.includes("ans")) answer = out.split`:`[1].trim();
      else {
        output += out;
        console.log(out);
      }
    });

    child.stderr.on("data", (data) => {
      console.error(data.toString());
    });

    let code = await new Promise((res) => child.on("close", res));
    console.log("-".repeat(20));

    console.log(`Program exited with code ${code}`);

    if (answer != null) {
      console.log(
        `Found answer ${colors.blue + colors.bold}${answer}${colors.end}`
      );
    }

    console.log("Waiting for file changes...\n");
    [_, file] = await filechange;
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

let watchedFiles = ["curday.py", "test.py"];

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

function runCode(file, inp) {
  let child = spawn("pypy3", [file]);
  child.stdin.write(inp);
  child.stdin.end();

  /*
  return new Promise((res) => child.on("close", res));
	*/
  return child;
}
