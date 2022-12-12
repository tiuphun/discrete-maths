//OK
#include <stdio.h>
#include <curses.h>
int x[31],t[31],n, count = 0;
void khoitao()
{
      printf("\nNhap n = ");
      scanf("%d",&n);
      x[0]=1;
      t[0]=0;
}
void xuat(int k)
{
      printf("\n%d = ",n);
      for (int i=1;i<k;i++) printf(" %d + ",x[i]);
      printf(" %d",x[k]);
}
void phantich(int i)
{
      for(int j=x[i-1];j<=((n-t[i-1])/2);j++)
      {
            x[i]=j;
            t[i]=t[i-1]+j;
            phantich(i+1);
      }
      x[i]=n-t[i-1];
      xuat(i); count++;
}
int main()
{
      khoitao();
      phantich(1);
      getchar();
      printf("\n%d\n", count);
}

