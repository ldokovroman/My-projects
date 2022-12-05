#include "string.h"
#include "paststring.h"
#include <algorithm>

String::String(const char * new_str) {
    size = strglen(new_str);
    str = new char[size + 1];
    strgcpy(str, new_str);
}

String::String(size_t n, char c) : size(n) {
    str = new char[size + 1];
    for (size_t i = 0; i < size; ++i)
        str[i] = c;
    str[size] = '\0';
}

String::String(const String &other)
    : size(other.size), str(new char[size + 1]) {
    strgcpy(str, other.str);
}

String::~String() {
    delete [] str;
}

void String::swap(String &other) {
    std::swap(size, other.size);
    std::swap(str, other.str);
}

String &String::operator=(const String &other) {
    if (this != &other)
        String(other).swap(*this);
    return *this;
}

void String::append(const String &other) {
    size += other.size;
    char * new_str = new char[size + 1];
    strgcpy(new_str, str);
    strgcat(new_str, other.str);
    delete [] str;
    str = new_str;
}

String::PastString String::operator[](size_t i) const {
    return String::PastString(i, String(str + i));
}



