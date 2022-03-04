#include <stdint.h>

static uint64_t __attribute__((section (".test_variable"))) __attribute__((used)) test_variable = 0xF123456789ABCDEF;

int main()
{
	return 0;
}
