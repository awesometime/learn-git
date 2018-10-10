### 1 map
```cpp
#include <iostream>
#include <list>
#include <string>
#include <stdio.h>
#include <map>
using namespace std;

int main(){
	map<string, int> table;
	
  table["wan"] += 5;
	table["hello"] += 1;
	table["wan"] += 1;
	
  for (auto it = table.begin();it != table.end();it++) {
		cout << it->first << ", " << it->second << endl;
	}
}
```
