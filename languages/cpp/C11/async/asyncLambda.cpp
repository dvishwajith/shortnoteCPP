#include <iostream>
#include <string>
#include <chrono>
#include <thread>
#include <future>


std::string fetchDataFromFile(std::string recvdData)
{
    // Make sure that function takes 5 seconds to complete
    std::this_thread::sleep_for(std::chrono::seconds(3));
    //Do stuff like fetching Data File
    return "File_" + recvdData;
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
    std::future<std::string> resultFromDB = std::async(std::launch::async, 
        [](std::string recvdData){
            // Make sure that function takes 5 seconds to complete
            std::this_thread::sleep_for(std::chrono::seconds(5));
            //Do stuff like creating DB Connection and fetching Data
            return "DB_" + recvdData;
        }    
    , "Data");
    
    /*
    std::future<std::string> resultFromDB = std::async(std::launch::deferred, 
        [](std::string recvdData){
            // Make sure that function takes 5 seconds to complete
            std::this_thread::sleep_for(std::chrono::seconds(5));
            //Do stuff like creating DB Connection and fetching Data
            return "DB_" + recvdData;
        }    
    , "Data");
    */

    //Feth data from file
    std::string fileData = fetchDataFromFile("Data");

    //wait for data from DB is completed
    std::string dbData = resultFromDB.get();

    auto end = std::chrono::system_clock::now();

    auto diff = std::chrono::duration_cast<std::chrono::seconds>(end -start).count();

    std::cout << " Total Time taken " << diff << " seconds" << std::endl;

    return 0;

    
}