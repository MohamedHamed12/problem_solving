
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int testnum,n,h,x,y;

     scanf("%d",&testnum);
    while(testnum--)
    {
        int nomOfy=0;
        int nomOfX=0;
        char p[1000];
        scanf("%d %d %d %d",&n,&h,&x,&y);

        for ( int i=0;i<n;i++)
        {
                   scanf("%s",&p);

               for(int m=0;m<strlen(p);m++ )
               {

                   if (p[m]=='.')
                   {
                       if (p[m]=='.'&&p[m+1]=='.')
                      {
                          nomOfy=nomOfy+1;
                          p[m]='*';
                          p[m+1]='*';


                      }
                      else
                      {
                          nomOfX+=1;
                          p[m]='*';
                      }
                   }


               }

        }







      /*  for (int i=0;i<n;++i)
        {

            for(int j=0;j<m;++j)
               {
                   if (a[i][j]=='.' && a[i][j+1]=='.')
                   {
                       numOfy+=1;
                       a[i][j]='*';
                       a[i][j+1]='*';
                   }



                    else if (a[i][j]=='.')
                   {
                       nomOfX+=1;
                       a[i][j]=='*';
                   }

               }
        }*/
        calyandx(x,y,nomOfX,nomOfy);
        }


    return 0;
}


void calyandx (int x,int y,int numx,int numy)
{

    int all=0;
    if ( 2*x <= y)
    {
        all=numx*x+numy*x+numy*x;
    }
    else
    {
        all=numx*x+numy*y;
    }

                printf("%d\n",all);
}