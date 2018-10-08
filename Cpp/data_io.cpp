################   
#   1  实现:读取文件内容并输出
#################
#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
using namespace std;

int main(int argc, char**argv)
{
/*两种文件流皆有open和close函数，之后视情况打开读或者写模式*/
string infile = "data_path";//代表文件名
vector<string> vec;//声明一个vector
ifstream in(infile);//ifstream定义了一个输入流in(文件流)，它被初始化从文件中读取数据
if (in)//检查文件的读取是否成功,养成良好的习惯！
{
    string buf;
    while (getline(in,buf)) //每行独立输入的方法，利用getline
    //while (in >> buf)    //每个单词作为一个元素 存储    
    {
        vec.push_back(buf);
    }
}
else
{
    cerr<<"cannot open this file: "<<infile<<endl;
}
for (int i = 0;i < vec.size();++i)
{
    cout<<vec[i]<<endl;
    cout<<"--- this is data row "<< i+1 <<"  ---"<<endl;
}

return 0;
}

################   
#   2  实现:读取文件内容存入到另一个文件
#################
#include <string>
#include <string.h>
#include <iostream>
#include <fstream>
using namespace std;

int main(){    
	     
	ifstream ifile("ten_data.txt",ios::in);        
	ofstream ofile("outputdata.csv",ios::app); 
	//ofstream ofile("outputdata.txt",ios::app);        
	
	char st[1000]; 
	//while(ifile.getline(st,sizeof(st),' ')){       // 以空格为一行
	while(ifile.getline(st,sizeof(st),'\n')){	 // 以换行符为一行
		ofile<<st<<endl;            
		//cout<<st<<endl;        
	        }         
	 	
	ofile.close();        
	ifile.close();    
	
}


################   
#   3  实现:遍历某一文件夹目录
#################
#include<string>     // 字符串类
#include<io.h>       // 遍历操作
#include <iostream>  // cin、cout
#include <fstream>   // 包含文件读取类与方法
using namespace std;

/*遍历某一文件夹目录*/
int main()
{

    struct _finddata_t fileinfo;  // 存储文件信息的结构体对象  
    string file = "E:/c1/log/12/";      // 放置log文件的目录,路径最后的/一定要有
    string strFile = file + "*"; //* 指目录下所有文件
    //将log目录输出到一个文件out_log_name.txt中
    //ofstream ofile("out_log_name.txt",ios::app);
	
    /***遍历目录系统函数要求先尝试寻找一个文件，看是否存在***/
    long handle;
    
    //_findfirst( ,  )  找不到文件返回-1
    if ((handle = _findfirst(strFile.c_str(), &fileinfo)) == -1L)
    {
        return 0;  // 如果查询log文件失败，直接返回
    }
    else
    {
        strFile = file + fileinfo.name;
        cout << strFile << endl;   // 对第一个加载的文件处理，此处仅做输出处理
        //将log目录输出到一个文件out_log_name.txt中
	//ofile << strFile << endl;
        
	/***一直遍历，直到所有文件得到加载与处理***/
        int i=1;       //统计文件数目
        while (!(_findnext(handle, &fileinfo)))
        {
            ++i;
            strFile = file + fileinfo.name;
            cout << strFile << endl; // 对后续加载的文件处理  
	    //将log目录输出到一个文件out_log_name.txt中
            //ofile << strFile << endl;
	}
        //ofile.close();
        _findclose(handle);  // 释放遍历目录的句柄
        cout << i-2 << endl;
    }
    return 0;
}


################   
#   4  实现:正则匹配并捕获
#################
#include <iostream>
#include <regex>
#include <string>
//#include <iostream>
//#include <fstream>
using namespace std;
 
int main ()
{ 
  std::string s ("112.84.34.103 - - cnki.cdn.bcebos.com [12/Sep/2018:19:00:08 +0800] 68 \"GET /2018CUMCM-AB.rar HTTP/1.1\" 404 600 117 \"http://cumcm.cnki.net/cumcm//studentHome/studentHome\" \"-\" \"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0\" \"220.195.66.7,116.95.27.55\" 5547950 \"MISS\" 58.216.2.35");
  std::regex e ("(.*) - - (.*) (\\[.*\\]) (.*) \"(.*)\" (.*) (.*) (.*) \"(.*)\" \"(.*)\" \"(.*)\" \"(.*)\" (.*) \"(.*)\" (.*)");
  //std::cout << s <<endl;
  
  
  if (std::regex_match (s,e))
    std::cout << "string object matched\n";
  
  
  std::smatch sm;    // same as std::match_results<string::const_iterator> sm;
  std::regex_match (s,sm,e);
  std::cout << "string object with " << sm.size() << " matches\n";

  
  std::cout << "the matches were: ";
  for (unsigned i=1; i<sm.size(); ++i) {
    std::cout  << sm[i] << endl;
    
  }

  return 0;
}

