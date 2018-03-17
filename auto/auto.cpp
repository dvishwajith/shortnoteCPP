#include <stdio.h>
#include <iostream>

int main(){

    
    auto var_int = 5;
    auto var_doub = 6.4 ;
    auto var_doub2 = 10.4 ;
    printf("var_int %d var_doub %f\n",var_int,var_doub);
    printf("swapped  wrong output by swapping keep in mind var_int %f var_doub %d\n",var_int,var_doub2);

    //Most easy methd is using cout
    std::cout << "var_int "<< var_int << " var_doub " << var_doub << std::endl;
    return 0;
}