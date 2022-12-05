#pragma once
#include <cstddef>

size_t strglen(const char *);
void strgcpy(char *, const char *);
void strgcat(char *, const char *);
int strgstr(const char *, const char *);
char * resize(const char *, size_t, size_t);
char * getline();
