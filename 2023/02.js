a=`Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
`
a=document.body.innerText

a=a.split`\n`.filter(c=>c).map(l=>{
	return l.split(': ')[1].replaceAll(';',',').split(', ').map(s=>s.split(' '))
})

sol=0

for (let [i,s] of a.entries()){
	console.log(s);
  z=1;
	for (let [w,c] of s){
		w=Number(w);
		let expected = [12,13,14]['red green blue'.split(' ').indexOf(c)]
		console.log(w,c,expected)
		if (w > expected){z=0;break};
	}
  if (z) sol+=i+1;
}

sol
