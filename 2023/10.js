// Advent of Code 2023 Day 10
// Written by Jordan Perry
// This could have been written so much better ;-;

a=`..F7.
.FJ|.
SJ.L7
|F--J
LJ...`
// a=`.....
// .S-7.
// .|.|.
// .L-J.
// .....`
a=`FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L`
// a=`...........
// .S-------7.
// .|F-----7|.
// .||.....||.
// .||.....||.
// .|L-7.F-J|.
// .|..|.|..|.
// .L--J.L--J.
// ...........`
// a=`.F----7F7F7F7F-7....
// .|F--7||||||||FJ....
// .||.FJ||||||||L7....
// FJL7L7LJLJ||LJ.L-7..
// L--J.L7...LJS7F-7L7.
// ....F-J..F7FJ|L7L7L7
// ....L7.F7||L7|.L7L7|
// .....|FJLJ|FJ|F7|.LJ
// ....FJL-7.||.||||...
// ....L---J.LJ.LJLJ...`
a=document.body.innerText

g=(i)=>i.split`\n`.map(l=>l.split``)
ug=(i)=>i.map(l=>l.join``).join`\n`
findall=(s,r)=>{let o=[];for(e of s.matchAll(r)){o.push(e)}return o}
d=/(-?\d+)/g
ints=(s)=>findall(s,d).map(i=>Number(i[0]))

a=g(a);
pts=[];
[x,y]=[0,0];

for(y=0;y<a.length;y++){for(x=0;x<a[0].length;x++){
    if(a[y][x]=='S')break;
}
    if(a[y][x]=='S')break;
}

[ox,oy]=[x,y]

paths=[]

for([dx,dy]of[[1,0],[-1,0],[0,1],[0,-1]]){
    try{
        nx=dx+x
        ny=dy+y
        if('-|'.includes(a[ny][nx])){paths.push([nx,ny,dx,dy]);break;} // this line doesn't account for no straight pipes connected to S
    }catch{}
}


for(_=2;_<1000000;_++){
    nps=[]
    for([i,path]of paths.entries()){
        [x,y,dx,dy]=path
        if('FLJ7'.includes(a[y][x])){
            if(a[y][x]=='F'){
                if(dy==-1){
                    dy=0
                    dx=1
                }else{
                    dy=1
                    dx=0
                }
            }
            if(a[y][x]=='L'){
                if(dy==1){
                    dy=0
                    dx=1
                }else{
                    dy=-1
                    dx=0
                }
            }
            if(a[y][x]=='J'){
                if(dy==1){
                    dy=0
                    dx=-1
                }else{
                    dy=-1
                    dx=0
                }
            }
            if(a[y][x]=='7'){
                if(dy==-1){
                    dy=0
                    dx=-1
                }else{
                    dy=1
                    dx=0
                }
            }
        }
//         a[y][x]='#'
        
        try{
            nx=dx+x
            ny=dy+y
            if('|-FLJ7S'.includes(a[ny][nx])){nps.push([nx,ny,dx,dy]);pts.push([nx,ny])}
        }catch{}
    }
    paths=nps
    
//     if(nps.length==0)break;
    if(nps[0][0]==ox&&nps[0][1]==oy)break;
    // if(nps.length==0)break;
}

console.log(ug(a))
console.log("part 1:", _/2)

double_area=0
for(i=0;i<pts.length;i++)double_area+=pts[i][0]*pts[(i+1)%pts.length][1] - pts[i][1]*pts[(i+1)%pts.length][0]
double_area=Math.abs(double_area)

console.log("part 2:", Math.floor((double_area - _)/2)+1)