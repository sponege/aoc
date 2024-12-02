z = `[1,"red",5]`;
z = document.body.innerText;
a = JSON.parse(z);
l = [a];
ans = 0;
while (l.length) {
  t = l.pop();
  // console.log(t)

  if (["object"].includes(typeof t) && !Array.isArray(t)) {
    if (Object.values(t).includes("red")) continue;
    for (c of Object.keys(t)) l.push(t[c]);
  }
  if (Array.isArray(t)) for (c of t) l.push(c);
  if (["number"].includes(typeof t)) ans += t;
}
console.log(ans);
