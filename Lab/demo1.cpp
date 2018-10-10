//   程序实现了
// 1.遍历某给定文件夹下的文件
// 2.统计每一文件中各个字段，此程序只将ip字段出现的ip及个数统计出来
// todo 多线程并发

#include <iostream>
#include <vector>
#include <regex>
#include <set>
#include <io.h>
#include <fstream>
using namespace std;

void error(string &msg) {
  cout << "[ERROR] " << msg << endl;
}


void debug(string &msg) {
  cout << "[DEBUG] " << msg << endl;
}


//遍历某给定文件夹dirname下的文件
bool ls(string dirname, vector<string> &files) {
    // 获取dirname下的所有文件名，将其存储到files中
    debug(dirname);
    struct _finddata_t fileinfo;  // 存储文件信息的结构体对象  
    
    string strFile = dirname + "*"; //* 指目录下所有文件
  
    /***遍历目录系统函数要求先尝试寻找一个文件，看是否存在***/
    long handle;
    
    //_findfirst( ,  )  找不到文件返回-1
    if ((handle = _findfirst(strFile.c_str(), &fileinfo)) == -1L) {
        return 0;  // 如果查询log文件失败，直接返回
    } else {
        strFile = dirname + fileinfo.name;
        cout << strFile << endl;   // 对第一个加载的文件处理，此处仅做输出处理
        files.push_back(strFile); 
        
        /***一直遍历，直到所有文件得到加载与处理***/
        int i=1;       //统计文件数目
        while (!(_findnext(handle, &fileinfo))){
            ++i;
            strFile = dirname + fileinfo.name;
            cout << strFile << endl; // 对后续加载的文件处理
            files.push_back(strFile);  
        }
        
        _findclose(handle);  // 释放遍历目录的句柄
        // windows不统计/.  /.. 两个目录
        cout << i-2 <<" log files finded" << endl;
    }
    return true;
}


bool parseLine(string line, vector<string> &results) {
  //std::smatch parseLine(string line, std::smatch &results) {
  // 正则匹配提取每一行中的各个字段
  std::regex e ("(.*) - - (.*) (\\[.*\\]) (.*) \"(.*)\" (.*) (.*) (.*) \"(.*)\" \"(.*)\" \"(.*)\" \"(.*)\" (.*) \"(.*)\" (.*)");
  std::smatch sm;
  if (!std::regex_match(line, sm, e)) {
    string msg = "error occured when parse line";
    error(msg);
    return false;
  }
  //cout << "=================================" << endl;
  // auto 作用
  // for (std::smatch::const_iterator it = sm.begin()+1; it != sm.end(); it++)
  for (auto it = sm.begin()+1; it != sm.end(); it++) {
    results.push_back(*it);
  }
  //cout << endl;
  
  return true;
}


bool parseFile(string filename) {
  // 处理filename指向的文件中的日志信息,并用map函数统计ip及每个ip出现的次数
  ifstream in(filename);
  if (in) {
    string buf;
    //set<string> ips;     //：set只能找到出现多少个ip
    
    // map 统计出现得所有ip以及每个ip出现的次数
    map<string, int> tables;
    while (getline(in,buf))
    {
      vector<string> results;
      if (parseLine(buf, results)) {
        //for (auto it = results.begin();it != results.end();it++) {
          //cout << *it << endl;    // 屏幕不打印
        //}
        
        //ips.insert(results[0]);     //：set
        tables[results[0]] += 1;     //results[0]取出ip字段，设置table["10.12.13.14"] +=1     
      }
    }
    
    cout << "----------------- " << endl;
    //cout << "in file " << filename << "  totally ips : " << ips.size() << endl;   //：set
    cout << "in file " << filename << "  totally ips : "  << tables.size() << endl;
    cout << "----------------- " << endl;
    // for (auto it = ips.begin();it != ips.end();it++) {      //：set
    //   cout << *it << "  occurred ... times"<< endl;
    // }  
    
    for (auto it = tables.begin();it != tables.end();it++) {
        cout <<"["<< it->first << "] =  " << it->second << endl;
    } 
  
  } else {
    string msg = "error occurred when parseFile --> open file(";
    msg += filename + ")";
    error(msg);
    return false;
  }
  
  return true;
}



bool parseDir(string dirname) {
  // 处理dirname指向的文件夹中的每一个文件的日志信息
  vector<string> files;
  if (!ls(dirname, files)) {
    string msg = "error occurred when ls dir(";
    msg += dirname + ")";
    error(msg);
    return false;
  }
  //cout << files.size() << endl;
  for (auto it = files.begin();it != files.end();it++) {
    if (!parseFile(*it)) {
      // todo 过滤掉/. /.. 这两个文件，否则报错，看着难受
      string msg = "error occurred when parse every file(";
      msg += *it + ")";
      error(msg);
      //return false;
    }
  }
  return true;
}

int main(void) {
  parseDir("E:/c1/data_for_exe/13/"); 
  return 0;
}
