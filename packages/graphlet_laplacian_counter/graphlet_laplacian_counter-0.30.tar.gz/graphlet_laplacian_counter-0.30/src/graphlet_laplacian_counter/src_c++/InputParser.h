//
// Created by windels on 08/02/18.
// based on the following stack overflow post:
// https://stackoverflow.com/questions/865668/how-to-parse-command-line-arguments-in-c
// todo, look into tclap as mentioned in another posters answer (better error handling

#ifndef NCOUNT2_INPUTPARSER_H
#define NCOUNT2_INPUTPARSER_H

#include "string"
#include "vector"
#include <algorithm>

class InputParser {
public:
    InputParser (int &argc, char **argv){
        for (int i=1; i < argc; ++i)
            this->tokens.push_back(std::string(argv[i]));
    }

    std::string getCmdOption( const std::string &option) {
        std::vector<std::string>::const_iterator itr;
        itr =  std::find(this->tokens.begin(), this->tokens.end(), option);
        if (itr != this->tokens.end() && ++itr != this->tokens.end()){
            return (std::string &) *itr;
        }
        static  std::string empty_string("");
        return empty_string;
    }

    bool cmdOptionExists(const std::string &option) const{
        return std::find(this->tokens.begin(), this->tokens.end(), option)
               != this->tokens.end();
    }
private:
    std::vector <std::string> tokens;

};


#endif //NCOUNT2_INPUTPARSER_H
