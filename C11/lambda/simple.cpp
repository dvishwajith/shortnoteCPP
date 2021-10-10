#include <bits/stdc++.h>
#include <vector>

void printVector(std::vector<int> &v)
{
    for_each(v.begin(), v.end(), [](int i)
    {
        std::cout << i << " ";
    } );
    std::cout << std::endl;
}

int main()
{

    /**
                [ capture clause ] (parameters) -> return-type  
                {   
                definition of method   
                } 
     * 
     */    
    std::vector<int> v {1,2,3,4,5,6,7,8,9};

    printVector(v);

    // below snippet find first number greater than 4
    // find_if searches for an element for which
    // function(third argument) returns true

    auto iter_g4 = std::find_if(v.begin(), v.end(), [](int i) -> bool
    {
        return i > 4;
    });
    /**
     *  If a lambda has one statement and that statement is a return statement (and it returns an expression), 
     * the compiler can deduce the return type from the type of that one returned expression.
     * 
     */

    std::cout << "First number greater that 4 is " <<  *iter_g4 << std::endl;


    /**
     * Count the nuber greater than 6
     * 
     */
    auto count_g6 = std::count_if(v.begin(), v.end(), [](int i)
    {
        return i > 6;
    });

    std::cout << "Number of numbers greater that 6 is " << count_g6 << std::endl;


    /**
     * Remove consecutive duplivate elemets
     * (if you want to remove all the duplicated, sort before unique function)
     * 
     */
    std::vector<int> dupl_v {1,2,3,3,3,4,5,5,5,5,6,7,8,9};
    auto duplicates_iter = unique(dupl_v.begin(), dupl_v.end(), [](int a, int b)
    {
        return a == b;
    });
    /**
     * This return an iterator. All the consecutive duplicates goes to the end of the vector giving 
     * iterator to the starting of the duplicates.
     * So we resie the vector until the starting of the duplicates
     */
    //dupl_v.resize(std::distance(v.begin(), duplicates_iter));
    dupl_v.erase(duplicates_iter, dupl_v.end());

    std::cout << "Duplicate removed vector is " ;
    printVector(dupl_v);


    /**
     * Using Accumultae to compute factorial
     * 
     */

    auto factorial = std::accumulate(v.begin(), v.end(), 1, [](int a, int b)
    {
        return a*b;
    });

    std::cout << "Factorial of whole array is " << factorial << std::endl;

    return 0;
}