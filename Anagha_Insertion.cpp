#include<iostream>
#include<conio.h>
void insertion(int* a, int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		int pos=i;
		while((pos>0)&&(a[pos]<a[pos-1]))
		{
			int t=a[pos];
			a[pos]=a[pos-1];
			a[pos-1]=t;
			pos--;
		}
	}
	for(i=0;i<n;i++)
	 std::cout<<a[i]<<" ";
}
int main()
{
	int a[100], n;
	std::cout<<"Enter the size of the array";
	std::cin>>n;
	std::cout<<"Enter the array";
	for(int i=0;i<n;i++)
	 std::cin>>a[i];
	insertion(a,n); 
	return 0;
}
