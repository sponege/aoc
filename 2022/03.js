a=`vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
`
a=document.body.innerText

a.split`\n`.filter(c=>c).map(l=>{
	let [r1,r2]=[l.slice(0,l.length/2),l.slice(l.length/2)]
	for (let c of r1) if (r2.includes(c)) return c;
}).map(c => {
	return c.charCodeAt(0)-(c == c.toUpperCase() ? 'A'.charCodeAt(0) - 26 : 'a'.charCodeAt(0))+1;
}).reduce((a,b)=>a+b)
