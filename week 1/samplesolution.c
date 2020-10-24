#include <stdio.h>

int main(void)
{
  for(int i = 0; i < 100; i++)
  {
    printf("%i\n",i);

    if(((i % 3) == 0) && ((i % 5) == 0))
    {
      printf("fizzbuzz\n");
    }
    else if((i % 3) == 0)
    {
      printf("fizz\n");
    }
    else if((i % 5) == 0)
    {
      printf("buzz\n");
    }
  }
  return 0;
}
