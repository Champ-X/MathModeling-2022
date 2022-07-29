# 线性规划问题

## 常规问题

<img src="problems\常规线性规划.png" style="zoom: 67%;" />

```matlab
model:

sets:
col/1..3/:c,x;
row/1..2/:b;
links(row,col):a;
endsets

data:
c = 3 -1 -1;
a = 1 -2 1 4 -1 -2;
b = 11 -3;
enddata

max = @sum(col:c*x);
@for(row(i):@sum(col(j):a(i,j)*x(j))<b(i));
-2*x(1)+x(3) = 1;
x(1) >= 0;
x(2) >= 0;
x(3) >= 0;

end
```

## 带有绝对值的问题（对于lingo没有区别自动处理了）

<img src="problems\带有绝对值的线性规划.png" style="zoom:67%;" />

```
model:

sets:
col/1..4/:x,c;
row/1..3/:b;
links(row,col):a;
endsets

data:
c = 1 2 3 4;
b = 0 1 -0.5;
a = 1 -1 -1 1
    1 -1 1 -3
    1 -1 -2 3;
enddata
min = @sum(col:c*@abs(x));
@for(row(i):@sum(col(j):a(i,j)*x(j))=b(i));
@for(col:@free(x));
end
```

## 指派问题

<img src="problems\指派问题.png" style="zoom:67%;" />

```
model: 

sets: 
var/1..5/; 
link(var,var):c,x; 
endsets 

data: 
c=3 8 2 10 3   
  8 7 2 9 7   
  6 4 2 7 5   
  8 4 2 3 5   
  9 10 6 9 10; 
enddata 

min = @sum(link:c*x); 
@for(var(i):@sum(var(j):x(i,j))=1); 
@for(var(j):@sum(var(i):x(i,j))=1); 
@for(link:@bin(x)); 

end 
```

