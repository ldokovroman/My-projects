#include "functions.h"
#include <iostream>

size_t strglen(const char * str) {
    int len = 0;
    while (*str++) ++len;
    return len;
}

void strgcpy(char * to, const char * from) {
    while (*from) {
        *to = *from;
        ++to;
        ++from;
    }
    *to = *from;
}

void strgcat(char * to, const char * from) {
    while (*to) ++to;
    strgcpy(to, from);
}

int strgstr(const char * text, const char * pattern) {
    const char * p = pattern;
    const char * t = text;
    while (*t && *p) {
        if (*t == *p) ++p;
        else if (p != pattern) {
            --t;
            p = pattern;
        }
        ++t;
    }
    if (*p == '\0') return (t - text) - (p - pattern);
    else return -1;
}

char * resize(const char * str, size_t size, size_t new_size) {
    char * new_str = new char[new_size];
    for(size_t i = 0; i < size && i < new_size; ++i)
        new_str[i] = str[i];
    delete [] str;
    return new_str;
}

char * getline() {
    size_t k = 0;
    size_t size = 1;
    char c;
    char * res = new char[size];
    while (std::cin.get(c) && (c != '\n')) {
        res[k] = c;
        ++k;
        if (k == size) {
            res = resize(res, size, size * 2);
            size *= 2;
        }
    }
    res[k] = '\0';
    return res;
}

