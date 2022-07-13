x = X
y = Y
P= polyfit(X, Y, 3)   %三阶多项式拟合

xi=0:.2:10;  

yi= polyval(P, xi);  %求对应y值

plot(xi,yi,x,y,'r*');