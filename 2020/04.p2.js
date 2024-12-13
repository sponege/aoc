a = `eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
`;

a = document.body.innerText.trim();

ans = 0;
for (let passport of a.split`\n\n`.map((p) => p.replaceAll(`\n`, " "))) {
  if (
    `byr iyr eyr hgt hcl ecl pid`.split` `.every((field) =>
      passport.includes(field)
    )
  ) {
    p = {};
    for (let thing of passport.split` `) {
      let [field, value] = thing.split`:`;
      p[field] = value;
    }
    let valid = 1;
    for (let field of `byr iyr eyr hgt hcl ecl pid`.split` `) {
      switch (field) {
        case "byr":
          year = +p[field];
          if (year < 1920 || year > 2002) valid = 0;
          break;
        case "iyr":
          year = +p[field];
          if (year < 2010 || year > 2020) valid = 0;
          break;
        case "eyr":
          year = +p[field];
          if (year < 2020 || year > 2030) valid = 0;
          break;
        case "hcl":
          color = p[field];
          if (
            color[0] != "#" ||
            !color.slice(1).split``.every((h) => "0123456789abcdef".includes(h))
          )
            valid = 0;
          break;
        case "ecl":
          color = p[field];
          if (!`amb blu brn gry grn hzl oth`.split` `.some((c) => c == color))
            valid = 0;
          break;
        case "hgt":
          let height = p[field];
          if (height.includes("cm")) {
            let h = +height.split("c")[0];
            if (h < 150 || h > 193) valid = 0;
          } else if (height.includes("in")) {
            let h = +height.split("i")[0];
            if (h < 59 || h > 76) valid = 0;
          } else valid = 0;
          break;
        case "pid":
          let number = p[field];
          if (
            number.length != 9 ||
            !number.split``.every((n) => "0123456789".includes(n))
          )
            valid = 0;
          break;
      }
    }

    if (valid) {
      console.log(p);
      ans++;
    }
  }
}
console.log(ans);
