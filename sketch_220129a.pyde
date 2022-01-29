s=300
r=300
u=300
t=300    
f=60
g=60
n=1
l=random(70,550)
k=random(70,550)
v=0
def setup():
    size(600,600)
    
def draw():
    global s,r,u,t,f,g,l,k,v,n
    background(0,255,31)
    fill(255,0,0)
    ellipse(u,s,f,g)
   # rect(78,67,24,78)
    fill(255,188,0)
    ellipse(l,k,18,18)
    fill(199,0,255)
    textSize(25)
    text (u'W=вверх, A=вправо, S=ввниз, D=влево', 20,20)
    fill(0,0,0)
    textSize(32)
    text (u'Счёт:',0,597)
    text (v,85,597)
    if 1==1:
        if key == 'w'and s>34:
            s=s-n
        if key == 'a' and u>34:       
            u=u-n
        if key == 's' and s<566:
            s=s+n
        if key == 'd' and u<566:
            u=u+n
        if keyCode == RIGHT:
            f=f+1
        if keyCode == LEFT:
            f=f-1
        if keyCode == UP:
            g=g+1
        if keyCode == DOWN:
            g=g-1
    if u>l-20 and u<l+20 and s>k-20 and s<k+20 :
        fill(198,192,64)
        textSize(45)
        text(u"съел", 100,100)    
        l=random(70,550)
        k=random(70,550)         
        v=v+1
        n=n+1






s=s+5
u=u-5
r=r-5
t=t+5
f=f+5
g=g+5
