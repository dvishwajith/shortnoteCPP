#include <iostream>

/**
 * @brief Meger sort
 * 
 * @param arr 
 * @param begin  starting index
 * @param end    end index
 */

void merge(int *arr, int begin, int mid, int end)
{
    auto length = end - begin + 1;
    int temp[length] = {};
    for (int i=0; i<length; i++)
    {
        temp[i] = arr[begin + i];
    }
    auto leftedge = mid - begin;
    auto rightedge = end - begin;
    int i = begin;
    auto left = 0;
    auto right = leftedge + 1;

    while(left <= leftedge && right <= rightedge)
    {
        if (temp[left] <= temp[right])
        {
            arr[i] = temp[left];
            left++;
        }
        else
        {
            arr[i] = temp[right];
            right++;
        }
        i++;
    }

    while(left <= leftedge)
    {
        arr[i] = temp[left];
        left++;
        i++;
    }

    while(right <= rightedge)
    {
        arr[i] = temp[right];
        right++;
        i++;
    }
}

void mergesort(int *arr, int begin, int end)
{
    if (begin == end)
    {
        return;
    }
    int mid = (end + begin)/2;
    mergesort(arr, begin, mid);
    mergesort(arr, mid+1, end);
    merge(arr, begin, mid, end);
}

int main()
{
    int test_arr[] = {3,6,1,9,4,7,2,9,0};
    mergesort(test_arr, 0, sizeof(test_arr)/sizeof(int)-1);

    for(auto &d:test_arr)
    {
        std::cout << d << " ";
    }
    std::cout<<std::endl;
    return 0;
}