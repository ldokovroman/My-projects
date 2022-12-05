#pragma once
#include "string.h"

struct String::PastString {
    PastString(size_t, const String &);
    String operator[](size_t) const;
    size_t shift;
    String past_strg;
};