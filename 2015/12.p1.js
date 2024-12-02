console.log(
  document.body.innerText
    .match(/(-?[\d]+)/g)
    .map((c) => Number(c))
    .reduce((a, b) => a + b)
);
