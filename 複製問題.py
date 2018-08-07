#!usr/bin/python3.5

marxes=['Groucho','ghico','Harpo'];
print(len(marxes));

a=[1,2,3];
b=a;
print(b);
a[0]='superise';
print(b);

#因為這樣a和b是指到同一個陣列，所以a改的話b也會跟著改，若希望b是創造一個跟a不同的列的話有三種方法
#1.copy()
#2.使用轉換list()
#3.使用list的slice
a = [1, 2, 3]
b = a.copy();
c = list(a);
d = a[:];
b[0] = "b";
c[0] = "c";
d[0] = "d";
print("a:",a);
print("b:",b);
print("c:",c);
print("d:",d);


