clear;
%有限元方法，场景一空间[5000,5000,3000];
global s1 s2
s1=[0 0 1300;5000 0 1700;0 5000 1700;5000 5000 1300];%场景1；
s2=[0 0 1200;5000 0 1600;0 3000 1600;5000 3000 1200];%场景2；
% step=10;%划分的网格节点数
% x=linspace(0,5000,step);
% y=linspace(0,3000,step);
% z=linspace(0,1600,step);
d=[];D=[];
% for i=1:size(x,2)
%     for j=1:size(y,2)
%         for k=1:size(z,2)
%             dd=distance1(x(i),y(j),z(k));
%             DD=distance2(x(i),y(j),z(k));
%             d=[d;dd];
%             D=[D;DD];
%         end
%     end
% end
% defined_cord=importdata('defined_cord.mat');
% for i=1:size(defined_cord,1)
%             dd=distance2(defined_cord(i,1),defined_cord(i,2),defined_cord(i,3));
%             DD=distance1(defined_cord(i,1),defined_cord(i,2),defined_cord(i,3));
%             d=[d;dd];
%             D=[D;DD];
% end

s2_normal=importdata('s2_normal.mat');
s2_abnormal=importdata('s2_abnormal.mat');
scene2=[s2_normal;s2_abnormal];
% noneerorr=d
Normal4D_XYZ_8=importdata('Normal4D_XYZ_8.mat');
Abnormal4D_XYZ_8=importdata('Abnormal4D_XYZ_8.mat');
% net_8=importdata('net_8.mat');
result=[];
for i=1:10%场景二映射到场景一
    tempdata=transpose(scene2(i,:));
        t=sim(net_8,tempdata);
        result=[result;t'];
end
final_result_normal=[];%无干扰信号在场景一中坐标
for i=1:5
    tempdata=transpose(result(i,:));
        t=sim(Normal4D_XYZ_8,tempdata);
        final_result_normal=[final_result_normal;t'];
end
final_result_abnormal=[];%干扰信号在场景一中坐标
for i=6:10
    tempdata=transpose(result(i,:));
        t=sim(Abnormal4D_XYZ_8,tempdata);
        final_result_abnormal=[final_result_abnormal;t'];
end
function dd=distance1(a,b,c)
global s1
dd=[];
for i=1:4
    temp=sqrt((a-s1(i,1))^2+(b-s1(i,2))^2+(c-s1(i,3))^2);
    dd=[dd,temp];
end
end
function dd=distance2(a,b,c)
global s2
dd=[];
for i=1:4
    temp=sqrt((a-s2(i,1))^2+(b-s2(i,2))^2+(c-s2(i,3))^2);
    dd=[dd,temp];
end
end


