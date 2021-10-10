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


/**
 * A lambda expression can have more power than an ordinary function by having access to variables from the enclosing scope. We can capture external variables from enclosing scope by three ways :
      Capture by reference
      Capture by value
      Capture by both (mixed capture)

Syntax used for capturing variables :
      [&] : capture all external variable by reference
      [=] : capture all external variable by value
      [a, &b] : capture a by value and b by reference

A lambda with empty capture clause [ ] can access only those variable which are local to it.
Capturing ways are demonstrated below :
 * 
 */


    std::vector<int> v1 = {1,2,2,3,3,3,4,5,6};
    std::vector<int> v2 = {10, 2, 7, 16, 9};

    /**
     * @brief Pushing a value in to v1 and v2 at the same time using referece &
     * 
     */
    auto pushintoV1andV2 = [&](int val)
    {
        v1.push_back(val);
        v2.push_back(val);
    };

    pushintoV1andV2(1);
    pushintoV1andV2(2);
    pushintoV1andV2(3);
    pushintoV1andV2(4);

    printVector(v1);
    printVector(v2);


    // access v1 by copy
    std::vector<int> dupl_v {1,2,3,3,3,4,5,5,5,5,6,7,8,9};

    auto printDuplicate = [dupl_v]()
    {
        /**
         * dply_v is passed by copy. The value is not mutable. To change the value specifally should be mentioned that is is mutable
         * 
         */
        std::cout << "Print duplicate_v by copy "; 
        for(auto &i: dupl_v)
        {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    };

    printDuplicate();

    auto removeDuplicate = [dupl_v]() mutable 
    {
        /**
         * Remove consecutive duplivate elemets
         * (if you want to remove all the duplicated, sort before unique function)
         * 
         */
        
        auto duplicates_iter = unique(dupl_v.begin(), dupl_v.end(), [](int a, int b)
        {
            return a == b;
        });
        /**
         * This return an iterator. All the consecutive duplicates goes to the end of the vector giving 
         * iterator to the starting of the duplicates.
         * So we resie the vector until the starting of the duplicates
         */

        dupl_v.erase(duplicates_iter, dupl_v.end());
        std::cout << "Duplicate removed vector is " ;
        printVector(dupl_v);
    };

    removeDuplicate();
    /**
     * Eventhough duplicated a revoed above, since it is passed by copy , values are not changef
     * outside that scope
     * 
     */
    printVector(dupl_v);

    return 0;
}