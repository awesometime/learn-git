################   
#   实现:读取文件内容并输出
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
#   实现:读取文件内容存入到另一个文件
#################
#include <string>
#include <string.h>
#include <iostream>
#include <fstream>
using namespace std;

int main(){    
	     
	ifstream ifile("ten_data.txt",ios::in);        
	ofstream ofile("outputdata.txt",ios::app);        
	
	char st[1000]; 
	while(ifile.getline(st,sizeof(st),'\n')){            			           
		ofile<<st<<endl;            
		cout<<st<<endl;        
	        }         
	 	
	ofile.close();        
	ifile.close();    
	
}
