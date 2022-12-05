#include "paststring.h"
#include <iostream>
using namespace std;

int main() {
    String strg("Hello, ");
    String const substrg = strg[1][5];
    cout << substrg.str << endl;
    char * str = getline();
    strg.append(str);
    cout << strg.str << "!\n";
    cout << strgstr(strg.str, substrg.str);
    return 0;
}
