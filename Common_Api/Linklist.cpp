#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

class Integer {
	public:
		int reverse(int x) {
			bool negative_flag = false;
			int result = 0;
			int v;
			
			if (x < 0)
			{
				negative_flag = true;
				x = x * (-1);
			}
			
			while(x != 0)
			{
				v = x % 10;
				result = result * 10 + v;
				x = x / 10;
				
				if (result % 10 != (v))
					return 0;
				//printf("v = %d, result = %d, x = %d\n", v, result, x);
			}
			
			if (negative_flag == true)
				return (result * -1);
			else
				return result;
		}
		bool isPalindrome(int x) {
			int revert = 0;
			int origin_v = x;
			int v = 0;
			
			if (x < 0)
				return false;
			
			while(x != 0)
			{
				v = x % 10;
				revert = revert * 10 + v;
				x = x / 10;
			}
			
			if ((revert + origin_v) == (origin_v << 1))
				return true;
			else
				return false;
		}
};

int main()
{
	int result = 0;
	Integer solve_obj;
	
	result = solve_obj.reverse(456);
	printf("Input = %d, and result is %d\n",456, result);
	
	result = solve_obj.isPalindrome(1654561);
	printf("The %d is palindrome = %d\n",1654561, result);
	
	
	return 0;
}