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
ug=(_i)=>_i.map(l=>l.join``).join`\n`
findall=(s,r)=>{let o=[];for(e of s.matchAll(r)){o.push(e)}return o}
d=/(-?\d+)/g

a=g(a)

h=[ug(a)]
for(i=0;i<500;i++){
    // o=a.copyWithin();
    while(true){
        l=0;
        for(y=a.length-1;y>0;y--){
            for(x=0;x<a[0].length;x++){
                if(a[y][x]=='O'&&a[y-1][x]=='.'){l=1;a[y][x]='.';a[y-1][x]='O'}
            }
        }
        if(!l)break;
    }
    while(true){
        l=0;
        for(x=a[0].length-1;x>0;x--){
            for(y=0;y<a.length;y++){
                if(a[y][x]=='O'&&a[y][x-1]=='.'){l=1;a[y][x]='.';a[y][x-1]='O'}
            }
        }
        if(!l)break;
    }
    while(true){
        l=0;
        for(y=0;y<a.length-1;y++){
            for(x=0;x<a[0].length;x++){
                if(a[y][x]=='O'&&a[y+1][x]=='.'){l=1;a[y][x]='.';a[y+1][x]='O'}
            }
        }
        if(!l)break;
    }
    while(true){
        l=0;
        for(x=0;x<a[0].length-1;x++){
            for(y=0;y<a.length;y++){
                if(a[y][x]=='O'&&a[y][x+1]=='.'){l=1;a[y][x]='.';a[y][x+1]='O'}
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
    // console.log(a)
    if (h.indexOf(ug(a))>1) {
        index=h.indexOf(ug(a));
        billion_index = (10**9 - index) % ((i+1) - index) + index;
        a=g(h[billion_index]);
        console.log('found');
        break;
    }
    
    h.push(ug(a))
    // if(ans==o)break;
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
h.length