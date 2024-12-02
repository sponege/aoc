a=`px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
`
// a=document.body.innerText

a=a.slice(0,a.length-1) // remove last line break

g=(i)=>i.split`\n`.map(l=>l.split``)
ug=(i)=>i.map(l=>l.join``).join`\n`
findall=(s,r)=>{let o=[];for(e of s.matchAll(r)){o.push(e)}return o}
d=/(-?\d+)/g
ints=(s)=>findall(s,d).map(b=>Number(b[0]))

var[ws,rs]=a.split`\n\n` // workflows, ratings

function parse_workflow(l){
    var[_,name,rules]=findall(l,/(.*){(.*)}/g)[0];
    rules=rules.split`,`.map(r=>r.split`:`)
    return [name,rules];
}
function parse_rules(l){
    var rules=findall(l,/{(.*)}/g)[0][1].split`,`.map(r=>r.split`=`).map(r=>[r[0],Number(r[1])]);
    var ruledict={};
    for (let[name,num] of rules)ruledict[name]=num;
    return ruledict;
}
ws=ws.split`\n`.map(parse_workflow)
var workdict={};
for (let[name,num] of ws)workdict[name]=num;
ws=workdict;
rs=rs.split`\n`.map(parse_rules)

ans=0;
// thanks to 5space for helping out on this part via posting their code solution :)
function p2(part, wf){
	if(wf=='A') return Object.values(part).map(r=>r[1]-r[0]+1).reduce((a,b)=>a*b,1);
	else if(wf=='R')return 0;

	let amt = 0;
    for(rule of ws[wf]){
        if (rule.length==1){
            continue;
        }
        var[query,result]=rule;
		var cutoff=ints(query)[0];
        if(query[1]=='<'){
			var[t,f]=[[part[query[0]][0],cutoff-1],[cutoff,part[query[0]][1]]];
        }
        if(query[1]=='>'){
            var[t,f]=[[cutoff+1,part[query[0]][1]],[part[query[0]][0],cutoff]];
        }

		if(t[1]>t[0]){
			np={...part};
			np[query[0]]=t;
			amt += p2(np, result);
		}
		if(f[1]>f[0])part[query[0]]=f;
    }

	amt += p2({...part}, ws[wf][ws[wf].length-1]);
	return amt;
}

p2({x:[1,4000],m:[1,4000],a:[1,4000],s:[1,4000]}, 'in');