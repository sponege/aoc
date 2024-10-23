inp=3014387;

n=[];for(i=1;i<=inp;i++)n.push(i);

while(n.length>1){
    // a=n.shift();
    // b=n.shift();
    // n.push(a);
    // console.log(n.length);
    nn=[];
    ol=n.length;
    for (i=0;i<n.length;i++){
        if(i%2==0)nn.push(n[i]);
    }
    
    if(ol%2==1)nn.splice(0,0,nn.pop());
    
    n=nn;
    console.log(n.length,n)
}

console.log(n);
