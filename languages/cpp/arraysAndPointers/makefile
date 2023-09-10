##############################################################################
# Compiler specifications
# These match the variable names given in /usr/share/lib/make/make.rules
# so that make's generic rules work to compile our files.
# gmake prefers CXX and CXXFLAGS for c++ programs
##############################################################################
# Which compiler should be used

#CC -- the c compiler to use
#CXX -- the c++ compiler to use
#LD -- the linker to use
#CFLAGS -- compilation flag for c source files
#CXXFLAGS -- compilation flags for c++ source files
#CPPFLAGS -- flags for the c-preprocessor (typically include file paths and symbols defined on the command line), used by c and c++
#LDFLAGS -- linker flags
#LDLIBS -- libraries to link

CXX = g++
CC = $(CXX)
RM = rm -rf



# -Wall This enables all the warnings about constructions that some users consider questionable, and that are easy to avoid
DEBUG_LEVEL		=-g 
EXTRA_CCFLAGS	=-Wall -std=c++11 -O3
CXXFLAGS 		=$(DEBUG_LEVEL) $(EXTRA_CCFLAGS) 
CCFLAGS         =$(CXXFLAGS) 
BIN 			=bin


LDFLAGS			=-g 
LDLIBS			=-pthread

# All source files have associated object files.
# This line sets `OFILES' to have the same value as `SRC_FILES' but
# with all the .cpp's changed into .o's.
SRC_FILES 		= $(wildcard *.cpp)
O_FILES         = $(SRC_FILES:%.cpp=%.o)
EXEC			= $(SRC_FILES:%.cpp=%)  #Added variable for executable

all: $(EXEC)


#simplified
$(EXEC): %: %.cpp
	mkdir -p $(BIN)/
	$(CC)    $(LDFLAGS) $(LDLIBS)  $(CCFLAGS) $^  -o  $(BIN)/$@ 

clean:
	$(RM) *.o
	$(RM) $(O_FILES)
	$(RM) $(EXEC)
	$(RM) $(BIN)