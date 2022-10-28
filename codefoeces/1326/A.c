#include <stdio.h>



#define     s     scanf
#define     p      printf

int main () {
    int tc,n,i;

    s ("%d",&tc);

    while (tc--) {
        s ("%d",&n);

        if (n == 1)
            p("-1");
        else
        {
            for (i=1; i<n; i++)
                p("9");

            p ("4");
        }

        p ("\n");
    }

    return 0;
}