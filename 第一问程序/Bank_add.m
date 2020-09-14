clear
load('A_LiuShi.mat')
load('B_LiuShi.mat')
load('C_LiuShi.mat')
load('NianLiLv.mat')
load('WeiYueLv.mat')
load('XinYongPingJi.mat')
load('Precentage.mat')
syms t
Rent_Amount=1000000;
ftp=0.02;
Max_=-1000000*ones(1,123);
T=zeros(1,123);
for i=1:302 %对每一个企业
    if XinYongPingJi(i)==1
       [f,~]=Language(NianLiLv,A_LiuShi,0.04); 
    elseif XinYongPingJi(i)==2
       [f,~]=Language(NianLiLv,B_LiuShi,0.04);
    elseif XinYongPingJi(i)==3
       [f,~]=Language(NianLiLv,C_LiuShi,0.04); 
    else
        break
    end
    for t=0.04:0.001:0.10 %贷款年利率
        E=eval(Rent_Amount*t/(1-WeiYueLv(i))*(1-subs(f)));
        Antici_loss=WeiYueLv(i)*Rent_Amount;
        Costing=ftp*Rent_Amount;
        M=E-Antici_loss-Costing;
        if M>Max_(i)
            Max_(i)=M;
            T(i)=t/(1-WeiYueLv(i));
        end
    end
end
