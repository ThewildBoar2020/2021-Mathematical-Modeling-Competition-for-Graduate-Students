clear;
data=importdata('data.mat');
net123=importdata('C43_123.mat');
net023=importdata('C43_023.mat');
net013=importdata('C43_013.mat');
net012=importdata('C43_012.mat');
for i=1:size(data,1)
    tem123=[data(i,2),data(i,3),data(i,4)];
    tem023=[data(i,1),data(i,3),data(i,4)];
    tem013=[data(i,1),data(i,2),data(i,4)];
    tem012=[data(i,1),data(i,2),data(i,3)];
    t123=sim(net123,tem123');
    t023=sim(net023,tem023');
    t013=sim(net013,tem013');
    t012=sim(net012,tem012');
    result(i,:)=[t123',t023',t013',t012',data(i,8)];
end
    