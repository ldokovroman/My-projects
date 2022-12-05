#include "paststring.h"

String::PastString::PastString(size_t i, const String &other) {
    shift = i;
    past_strg = other;
}

String String::PastString::operator[](size_t i) const {
    size_t new_size = i - shift;
    String strg(new_size, '\0');
    for (size_t j = 0; j < new_size; ++j)
        strg.str[j] = past_strg.str[j];
    return strg;
}