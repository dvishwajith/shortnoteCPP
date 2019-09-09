#To run doctest file with out 

 if __name__ == "__main__":
     import doctest
     doctest.testfile("doctest_from_file.txt")

python -m doctest -v example.txt



#To run doctest  with out 

 if __name__ == "__main__":
     import doctest
     doctest.testmod()

python -m doctest -v doctest_sample.py