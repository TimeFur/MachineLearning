#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;

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
int myAtoi(string str) {
	const int len = str.size();
	int start_i = 0;
	int v = 0;
	int result = 0;
	bool pos_flag = 1;
	
	for (int i = 0; i < len; i++)
	{
		if (str[i] != ' ')
		{
			start_i = i;
			break;
		}
	}
	
	printf("Start i = %d\n", start_i);
	
	if (((str[start_i] >= '0' && str[start_i] <= '9') || str[start_i] == '-' || str[start_i] == '+') == 0)
		return 0;
	if (str[start_i] == '-')
	{
		pos_flag = 0;
		start_i++;
	}
	else if (str[start_i] == '+')
	{
		pos_flag = 1; 
		start_i++;
	}
		
	
	for (int i = start_i; i < len; i++)
	{
		v = str[i] - '0';
		if (v >= 0 && v <= 9)
			result = result * 10 + v;
		else
			break;
		
		//overflow
		if ((result % 10) != v)
		{
			if (pos_flag == 0)
				return INT_MIN;    
			else
				return INT_MAX;
		}
			
	}

	if (start_i > 0 && str[start_i - 1] == '-')
	{
		return  result * (-1);
	}
	return result;
}
int maxArea(vector<int>& height) {
	int left = 0;
	int right = height.size() - 1;
	int w, h;
	int max = 0;
	
	while(right > left)
	{
		w = right - left;
		if (height[left] > height[right])
		{
			h = height[right];
			right--;
		}
		else
		{
			h = height[left];
			left++;
		}
		if ((w * h) > max)
			max = (w * h);    
	}
	
	
	return max;
}
void str_pointer()
{
	// std::string str_1 = "456";
	// *str1 = "123";
	// char *ptr = (char *)&str1;
	
	// printf("c = %c\n",ptr[0]);
	
}

int main()
{
	int result = 0;
	Integer solve_obj;
	
	result = solve_obj.reverse(456);
	printf("Input = %d, and result is %d\n",456, result);
	
	result = solve_obj.isPalindrome(1654561);
	printf("The %d is palindrome = %d\n",1654561, result);
	
	str_pointer();
	
	return 0;
}