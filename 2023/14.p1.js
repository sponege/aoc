a=`O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
`
a=document.body.innerText

g=(i)=>i.split`\n`.map(l=>l.split``)
ug=(i)=>i.map(l=>l.join``).join`\n`
findall=(s,r)=>{let o=[];for(e of s.matchAll(r)){o.push(e)}return o}
d=/(-?\d+)/g

a=g(a)

while(true){
    l=0;
    for(y=a.length-1;y>0;y--){
        for(x=0;x<a[0].length;x++){
            if(a[y][x]=='O'&&a[y-1][x]=='.'){l=1;a[y][x]='.';a[y-1][x]='O'}
        }
    }
    if(!l)break;
}
ans=0
w=0
for(y=a.length-1;y>=0;y--){
    for(x=0;x<a[0].length;x++){
        if(a[y][x]=='O'){ans+=w}
    }
    w++
}

console.log(ug(a),ans)