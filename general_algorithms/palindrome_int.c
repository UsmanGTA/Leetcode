#include <stdio.h>
#include <stdlib.h>
int is_palindrome(unsigned long n);

/**
 * is_palindrome - checks if a passed number
 * is a palindrome
 * @n: input number
 * Return: 0 if not a palindrome | 1 if it is.
 */
int is_palindrome(unsigned long n)
{
	unsigned long rev_n = 0, temp_n = n, last_digit;

	/* PLAN: */
	/* Since we don't have the len, we can't find what's the */
	/* len of (n) without O(2n). To aid this, we could simply */
	/* reduce the steps by simply reversing the number from */
	/* beginning to end and then check the final with n */

	/* temp_n = 1221 */

	/* rev_n will store the result of reversing n */
	/* temp_n would act as a buffer so we don't has to mess with n */

	while (temp_n)
	{
		last_digit = temp_n % 10;
		rev_n = (rev_n * 10) + last_digit;
		temp_n = temp_n / 10;
	}

	return(rev_n == n);
}

/**
 * main - Entry point
 *
 * @ac: Arguments counter
 * @av: Arguments vector
 *
 * Return: EXIT_SUCCESS or EXIT_FAILURE
 */
int main(int ac, char **av)
{
    unsigned long n;
    int ret;

    if (ac < 2)
    {
        fprintf(stderr, "Usage: %s arg\n", av[0]);
        return (EXIT_FAILURE);
    }

    n = (unsigned long)(atol(av[1]));
    ret = is_palindrome(n);

    printf("%lu is ", n);
    if (ret == 0)
        printf("not ");
    printf("a palindrome.\n");

    return (EXIT_SUCCESS);
}
