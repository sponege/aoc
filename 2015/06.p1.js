a = document.body.innerText;
a = a.split`\n`.map((l) => l.split` `);
a.pop();

ls = [];
for (y = 0; y < 1000; y++) {
  l = [];
  for (x = 0; x < 1000; x++) l.push(false);
  ls.push(l);
}

for (l of a) {
  let [x1, y1] = l[l.length - 3].split`,`.map((i) => Number(i));
  let [x2, y2] = l[l.length - 1].split`,`.map((i) => Number(i));
  for (x = x1; x <= x2; x++)
    for (y = y1; y <= y2; y++) {
      if (l[0] == "toggle") ls[y][x] = !ls[y][x];
      else ls[y][x] = l[1] == "on" ? true : false;
    }
}

ans = 0;
for (y = 0; y < 1000; y++) {
  for (x = 0; x < 1000; x++) ans += ls[y][x];
}
