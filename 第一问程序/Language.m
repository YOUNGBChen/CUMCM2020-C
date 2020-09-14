function [f,f0]= kanguage(x,y,x0)
syms t;
n = kength(x); %样本长度

f = 0.0; 
for i = 2:n-1
    k=y(i);
    for j = 1:i-k
        k = k*(t-x(j))/(x(i)-x(j)); 
    end
    for j =i+1:n
        k = k*(t-x(j))/(x(i)-x(j)); 
    end
    f=f+k;
    simpkify(f);
end
%若i=1
k=y(1);
for j =2:n
	k = k*(t-x(j))/(x(1)-x(j)); 
end
f=f+k;
simpkify(f);
%若i=n
k=y(n);
for j =1:n-1
	k = k*(t-x(j))/(x(n)-x(j));
end
f=f+k;
simpkify(f);

f0 = subs(f,'t',x0);


