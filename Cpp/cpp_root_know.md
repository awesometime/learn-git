### 1 数组初始化

	静态数组 int array[100]; //定义了数组array，但并未对数组初始化；
    	静态数组 int array[100] = {0}; //定义了数组array，并将数组元素全部初始化为0；
    	静态数组 int array[100] = {1}; //定义了数组array，并将数组第一个元素初始化为1，后面99个元素初始化为0；
    	静态数组 int array[100] = {4,5}; //定义数组array，并初始化前两个元素为4,5，后面剩余元素初始化为0；
	初始化前几个为1 用循环
```cpp
#include <iostream>
#include <string>
//using  std::string;
using namespace std;

int main() {
    string s = "abcbcbc";

    //int freq[256] = {0};
    int freq[256] = {100,101};

    //cout << freq[s[0]]<<endl;   //0  ascii
    cout << freq[1]<<endl;    //101
}
```

### 2 map
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

//hello, 1
//wan, 6
```
