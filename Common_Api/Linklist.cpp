#include <stdio.h>
#include <stdlib.h>

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
};

int main()
{
	int result = 0;
	Integer solve_obj;
	
	result = solve_obj.reverse(456);
	printf("Input = %d, and result is %d\n",456, result);
	
	return 0;
}