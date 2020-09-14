function [f,f0]= Language(x,y,x0)
%求已知数据点的拉格朗日插值多项式 
%x,y为已知的数据点的向量,要求维度相等
%xO是要求点的坐标：
%求得的拉格朗日插值多项式：f 
% xO处的插值：fO 
syms t;
n = length(x); 

f = 0.0; 
for i = 2:n-1
    l=y(i);
    for j = 1:i-l
        l = l*(t-x(j))/(x(i)-x(j)); 
    end
    for j =i+1:n
        l = l*(t-x(j))/(x(i)-x(j)); %计算拉格朗日基函数
    end
    f=f+l;%计算拉格朗日插值函数 
    simplify(f);%化简
end
%i=1的情况
l=y(1);
for j =2:n
	l = l*(t-x(j))/(x(1)-x(j)); 
end
f=f+l;
simplify(f);
%i=n的情况
l=y(n);
for j =1:n-1
	l = l*(t-x(j))/(x(n)-x(j));
end
f=f+l;
simplify(f);

f0 = subs(f,'t',x0);
%vpa(f0)%转化为小数


