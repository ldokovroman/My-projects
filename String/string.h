#pragma once
#include "functions.h"

struct String {
    String(const char * = "");
    String(size_t n, char);
    String(const String &);
    ~String();
    void swap(String &);
    String &operator=(const String &);
    void append(const String &);
    struct PastString;
    PastString operator[](size_t) const;
    size_t size;
    char * str;
};


