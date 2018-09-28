```
下载 https://sourceforge.net/projects/mingw-w64/files/页的
mingw-w64-install.exe
添加环境变量E:\MinGW64\mingw32\bin

在cmd 中gcc -v
输出版本信息即可
```
```
ps:各个Package的作用：

MinGW
---- MinGW Base System
-------- MinGW Compiler Suit
------------ mingw32-binutils 必选，用于编译生成的 .o 文件的链接、汇编、生成静态库等。
------------ mingw32-gcc 必选，核心的 C 编译器。
------------ mingw32-gcc-ada 可选，Ada 编译器。
------------ mingw32-gcc-fortran 可选，Fortran 编译器。
------------ mingw32-gcc-g++ 建议，C++ 编译器。
------------ mingw32-gcc-objc 可选，Objective-C 编译器。
------------ mingw32-gcc-v3-* 不建议，第三版 GCC 编译器。
------------ mingw32-libgcc 必需，C 编译器编译出来的程序的运行库。
------------ mingw32-libgfortran 可选，如选择了 Fortran 编译器，则必选，Fortran 运行库。
------------ mingw32-libgnat 可选，如选择了 Ada 编译器，则必选，Ada 运行库。
------------ mingw32-libobjc 可选，如选择了 Objective-C 编译器，则必选，Objective-C 运行库。
------------ mingw32-libstdc++ 可选，如选择了 C++ 编译器，则必选，C++ 运行库。
------------ mingw32-libgomp 可选，GNU OpenMP 库，高精度运算。
------------ mingw32-libquadmath 可选，QuadMath 库，数学运行。
------------ mingw32-libssp 可选，StackProtect 库，栈保护。
------------ mingw32-mingwrt 必选，MinGW 工具的运行库。
------------ mingw32-w32api 必选，运行 Windows 程序所必需的 DLL 文件。
-------- MinGW Source-Level Debugger
------------ mingw32-gdb 可选，GNU Debugger，命令窗口的调试器。
-------- MinGW Standard Libraries
------------ mingw32-gmp 可选，GNU 多精度运算库。
------------ mingw32-libgmp 可选，GMP 库的 DLL 文件。
------------ mingw32-libgmpxx 可选，GMP 库用于 C++ 的 DLL 文件。
------------ mingw32-mpfr 可选，MPFR 多精度运算库。
------------ mingw32-libmpfr 可选，MPFR 多精度浮点运算库的 DLL 文件。
------------ mingw32-mpc 可选，MPC 多精度运算库。
------------ mingw32-libmpc 可选，MPC 多精度浮点运算库的 DLL 文件。
------------ mingw32-libpthread-old 可选，旧版本的 POSIX 线程库的 DLL 文件。
------------ mingw32-libpthreadgc 可选，标准的 POSIX 线程库的 DLL 文件。
------------ mingw32-libpthreadgce 可选，使用 C++ 异常处理的 POSIX 线程库的 DLL 文件。
------------ mingw32-libquserex 可选，用于内核态的 POSIX 线程库的 DLL 文件。
------------ mingw32-libz 可选，zlib 库，用于 Zip 压缩及解压。
------------ mingw32-mingwrt 必选，MinGW 的开发库。
------------ mingw32-pthreads-w32 可选，POSIX 线程库的开发文件。
------------ mingw32-w32api 必选，Win32 SDK 的开发库。
---- MinGW Libraries
-------- MinGW Supplementary Libraries
------------ mingw32-lua 可选，Lua 语言的编译器、运行库等。
-------- MinGW Contributed Libraries
------------ mingw32-libunistring 可选，Unicode 字符串处理库。
---- MinGW Contributed
-------- MinGW Contributed Applications
------------ mingw32-tcl 可选，Tool Command Language，tcl 语言。
------------ mingw32-tk 可选，tcl 语言的图形用户界面。
------------ mingw32-xerces-c 可选，Xerces-C++ XML 解析库。
---- MinGW Autotools
-------- mingw32-autoconf 可选，用于 MSYS，Autoconf 的封装脚本
-------- mingw32-autoconf2.* 可选，最好全选，自动配置脚本生成工具。
-------- mingw32-automake 可选，用于 MSYS，Automake 的封装脚本
-------- mingw32-automake1.* 可选，最好全选，自动 Makefile 生成工具。
-------- mingw32-autotools 可选，用于 MSYS，自动选择 autoconf automake 等 Package。
-------- mingw32-gettext 建议，GNU 软件国际化（即多语言）库。
-------- mingw32-libasprintf 建议，GNU 软件国际化库。
-------- mingw32-libcharset 可选，字符集转换库。
-------- mingw32-libgettextpo 建议，GNU 软件国际化（即多语言）库。
-------- mingw32-libiconv 可选，字符集转换库。
-------- mingw32-libintl 建议，GNU 软件国际化库的运行时 DLL 文件。
-------- mingw32-libltdl 可选，可移植的 dlopen 替代库。
-------- mingw32-libtool 可选，共享库生成工具。
MSYS
---- MSYS Base System
-------- msys-base 可选，自动选择 MSYS 开发环境所需的一般的 Package。
-------- msys-bash 必选，Bash (Bourne Again SHell)，脚本解释器。
-------- msys-bzip2 建议，bzip2 工具及开发库、运行库。
-------- msys-core 必选，MSYS 核心文件。
-------- msys-coreutils 必选，MSYS 核心工具。
-------- msys-diffutils 建议，文件差别比较工具。
-------- msys-dos2unix 可选，将 DOS (即 Windows) 换行符转换为 Unix 换行符。
-------- msys-file 可选，判断文件类型的工具。
-------- msys-findutils 建议，查找文件的工具。
-------- msys-gawk 建议，字符串型 (Pattern) 扫描和处理语言的解释器。
-------- msys-grep 建议，打印匹配型 (Pattern) 的字符串的工具。
-------- msys-gzip 建议，gzip 工具及开发库、运行库。
-------- msys-less 建议，命令行的文本查看器。
-------- msys-locate 可选，基于数据库的 'find' 工具。
-------- msys-m4 建议，GNU 宏处理器。
-------- msys-make 建议，GNU Make 工具。
-------- msys-patch 建议，文件打补丁工具。
-------- msys-sed 建议，GNU 流编辑器。
-------- msys-tar 建议，GNU Tar 文件打包工具。
-------- msys-termcap 建议，终端数据库。
-------- msys-texinfo 建议，显示帮助文件的工具。
-------- msys-tiny 可选，自动选择 MSYS 所需的最少 Package。
-------- msys-xz 建议，lzma 工具及开发库、运行库。
---- MinGW Developer Toolkit
-------- mingw-developer-toolkit 建议，自动选择 MSYS 环境下用于 MinGW 开发所需的 Package。
-------- msys-autogen 建议，简化程序的生成，配合 autotool 使用。
-------- msys-bison 建议，GNU 语法分析器生成器。
-------- msys-bsdcpio 可选，BDS 版的 cpio 工具。
-------- msys-bsdtar 可选，BSD 版的 tar 工具。
-------- msys-cvs 可选，CVS 版本控制工具。
-------- msys-diffstat 可选，diff 工具生成文件的查看器。
-------- msys-flex 建议，快速词汇分析器生成器，一般和 bison 一起使用。
-------- msys-guile 建议，Scheme 解释器和库。
-------- msys-help2man 可选，生成 man 页面。
-------- msys-inetutils 可选，通用网络客户端，包括 telnet ftp 等。
-------- msys-libopenssl 建议，OpenSSL 库。
-------- msys-lndir 可选，Xorg 递归目录符号链接工具。
-------- msys-mksh 可选，MirBSD Korn Shell，脚本解释器。
-------- msys-mktemp 可选，创建临时文件或目录。
-------- msys-openssh 建议，OpenSSH，SSH 客户端。
-------- msys-openssl 建议，OpenSSL 工具。
-------- msys-perl 建议，Perl 解释器。
-------- msys-rsync 建议，文件传输程序。
-------- msys-vim 可选，控制台下的文件编辑器。
---- MSYS System Builder
-------- 这个是用于编译用于 MSYS 系统的程序的编译器，一般不需要

```
