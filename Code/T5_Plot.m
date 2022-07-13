x=[0  5000  0   5000    ];
y=[0   0   5000 5000       ];
z=[1300  1700  1700  1300    ];

scatter3(x,y,z,'filled')
hold on;
%%
[xx,yy] = meshgrid(linspace(min(x),max(x),30),linspace(min(y),max(y),30));

zz = griddata(x,y,z,xx(:),yy(:),'v4');

zz = reshape(zz,size(xx));

mesh(xx,yy,zz)

hold on
ha=gca;

text(0,0,1300,'A0','FontSize',15,'color','b');
text(5000,0,1700,'A1','FontSize',15,'color','b');
text(0,5000,1700,'A2','FontSize',15,'color','b');
text(5000,5000,1300,'A3','FontSize',15,'color','b');

ha=gca;
set(ha,'xlim',[0,5000])%将x轴上的取值范围设置为[x1,x2]

set(ha,'ylim',[0,5000])%将y轴上的取值范围设置为[y1,y2]

set(ha,'zlim',[0,3000])%将z轴上的取值范围设置为[z1,z2]
%%
plot3(x,y,z,'*')
for i=1:length(result)
    i_XYZ = result(i,:)
    plot3(i_XYZ(1,1),i_XYZ(1,2),i_XYZ(1,3), '.', 'color','b')
end
% plot(result)

xlabel('x')

ylabel('y')

zlabel('z')
title('实验场景1 任务5')

%













