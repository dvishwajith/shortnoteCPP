#include <iostream>
#include <string>
#include <chrono>
#include <thread>
#include <future>
#include <vector>

std::string fftHugeCalc(std::string recvdData)
{
    // Make sure that function takes 5 seconds to complete
    std::this_thread::sleep_for(std::chrono::seconds(5));
    //Do stuff like creating DB Connection and fetching Data
    return "DB_" + recvdData;
}


int main()
{
    /* Get Start time */
    auto start = std::chrono::system_clock::now();

    //Feth data from db

    /**
     * Asnc options
     * std::launch::async  It guarantees the asynchronous behaviour i.e. passed function will be executed in seperate thread.
     * std::launch::deferred  Non asynchronous behaviour i.e. Function will be called when other thread will call get() on future to access the shared state.
     * std::launch::async | std::launch::deferred (default) With this launch policy it can run asynchronously or not depending on the load on system. But we have no control over it.
     */

    std::vector<std::future<std::string>> fft_futures;

    for (size_t i = 0; i < 10; i++) 
    {
        std::string input = std::to_string(i);
        fft_futures.push_back(std::async(std::launch::async, fftHugeCalc, "Data "+input));
    }
    
    std::string output = "";
    //wait for data from DB is completed
    for(auto &fft_future: fft_futures)
    {
        output += fft_future.get()+ " ";
    }

    
    

    auto end = std::chrono::system_clock::now();

    auto diff = std::chrono::duration_cast<std::chrono::seconds>(end -start).count();

    std::cout << " Total Time taken " << diff << " seconds" << std::endl;
    std::cout << "output :" << output << std::endl;

    return 0;

    
}