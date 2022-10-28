#include<stdio.h>
 
int main() 
{
	int t, n, k;
	scanf("%d", &t);
	while (t != 0)
	{
		scanf("%d %d", &n, &k);
		if (k >= n) 
		{
			if (k%n != 0)
			{
				printf("%d\n", k / n + 1);
			}
			else
			{
				printf("%d\n", k / n);
			}
		}
		else 
		{
			if (n%k == 0)
			{
				printf("1\n");
			}
			else
			{
				printf("2\n");
			}
		}
		t--;
	}
	return 0;
}