# 目标规划

## 序贯法求解

1. <img src="problems\序贯法求解多目标规划.png" alt="image-20220802091135193" style="zoom:67%;" />

```
model: 
sets: 
level/1..3/:p,z,goal; 
variable/1..2/:x; 
h_con_num/1..1/:b; 
s_con_num/1..4/:g,dplus,dminus; 
h_con(h_con_num,variable):a; 
s_con(s_con_num,variable):c; 
obj(level,s_con_num)/1 1,2 2,3 3,3 4/:wplus,wminus; 
endsets 
data: 
ctr=?; 
goal=? ? 0; 
b=12; 
g=1500 0 16 15; 
a=2 2; 
c=200 300 2 -1 4 0 0 5; 
wplus=0 1 3 1; 
wminus=1 1 3 0; 
enddata 
min=@sum(level:p*z); 
p(ctr)=1; 
@for(level(i)|i#ne#ctr:p(i)=0); 
@for(level(i):z(i)=@sum(obj(i,j):wplus(i,j)*dplus(j)+wminus(i,j)* dminus(j))); @for(h_con_num(i):@sum(variable(j):a(i,j)*x(j))<b(i)); @for(s_con_num(i):@sum(variable(j):c(i,j)*x(j))+dminus(i)-dplus(i )=g(i)); @for(level(i)|i #lt# @size(level):@bnd(0,z(i),goal(i))); 
end 
```

2. <img src="problems\序贯法求解多目标规划其二.png" alt="image-20220802101714987" style="zoom:67%;" />

```
model: 
sets: 
level/1..5/:p,z,goal; 
variable/1..3/:x; 
s_con_num/1..8/:g,dplus,dminus; 
s_con(s_con_num,variable):c; 
obj(level,s_con_num)/1 1,2 2,2 3,2 4,3 8,4 5,4 6,4 7,5 1/:wplus,wminus; 
endsets 
data: 
ctr=?; 
goal=? ? ? ? 0; 
g=1700 50 50 80 100 120 100 1900; 
c=5 8 12 1 0 0 0 1 0 0 0 1 1 0 0 0 1 0 0 0 1 5 8 12; 
wplus=0 0 0 0 1 0 0 0 1; 
wminus=1 20 18 21 0 20 18 21 0; 
enddata 
min=@sum(level:p*z); 
p(ctr)=1; 
@for(level(i)|i#ne#ctr:p(i)=0); 
@for(level(i):z(i)=@sum(obj(i,j):wplus(i,j)*dplus(j)+wminus(i,j)* dminus(j))); @for(s_con_num(i):@sum(variable(j):c(i,j)*x(j))+dminus(i)-dplus(i)=g(i)); 
@for(level(i)|i #lt# @size(level):@bnd(0,z(i),goal)); 
End 
```

## 数据包络法求解多指标输入和多指标输出问题

![image-20220802114127833](problems\多指标评价问题.png)

```
model: 
sets: 
dmu/1..6/:s,t,p;    !决策单元; 
inw/1..2/:w;        !输入权重;  
outw/1..2/:u;       !输出权重; 
inv(inw,dmu):x;     !输入变量; 
outv(outw,dmu):y; 
endsets 
data: 
ctr=?; 
x=89.39      86.25        108.13    106.38      62.40      47.19   
  64.3       99           99.6      96          96.2       79.9; 
y=25.2       28.2         29.4      26.4        27.2       25.2   
  223        287          317       291         295        222; 
enddata 
max=@sum(dmu:p*t); 
p(ctr)=1; 
@for(dmu(i)|i#ne#ctr:p(i)=0); 
@for(dmu(j):
s(j)=@sum(inw(i):w(i)*x(i,j)); 
t(j)=@sum(outw(i):u(i)*y(i,j));
s(j)>t(j)
); 
@sum(dmu:p*s)=1; 
end 
```

