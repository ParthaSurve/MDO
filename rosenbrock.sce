clc;
clear;


[X,Y]=meshgrid(-2:.1:2,-2:.1:2);
phi =  100*(Y- X.^2).^2 + (1 - X).^2;
mesh(X,Y,phi);

