<p align="center">
  
  <h3 align="center">git<img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="" width=72 height=72></h3>

  <p align="center">
    学习，我是认真的.  
    <br>   
    <a href="https://github.com/awesometime/">awesometime的github主页</a>    
    <br> 
    <a href="http://git-scm.com/">git官网</a>
    <br> 
    <a href="https://www.git-tower.com/blog/git-cheat-sheet/">国外Git Cheat Sheet网址</a>
    <br> 
    <a href="https://blog.igevin.info/posts/git-cheat-sheet/">国内一个人的Git Cheat Sheet网址</a>
    <br> 
    <a href="https://github.com/flyhigher139/Git-Cheat-Sheet/">国内Git Cheat Sheet托管在GitHub上</a>
  </p>
</p>



- [Git Internal(初探git的内部实现)](https://changchen.me/blog/20180315/git-internal/)
- [test](#test)
- [干货](#干货)
- [git学习目录](#git学习目录)
- [git实践](#git实践)

## test
  三个网址如何换行显示
  加图片
  [![awesometime](https://github.com/awesometime/)](https://github.com/awesometime/)
  - **这里的字会加黑显示**. [gtignore](https://github.com/github/gitignore)`忽略文件的原则是`：
1忽略操作系统自动生成的文件，比如缩略图等；
2忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动
生成的文件就没必要放进版本库，比如Java编译产生的.class文件；
3忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。

1 忽略操作系统自动生成的文件，比如缩略图等；

2忽略编译生成的中间文件、可执行文件等，也就是如果一个文件是通过另一个文件自动生成的，那自动

生成的文件就没必要放进版本库，比如Java编译产生的.class文件；

3忽略你自己的带有敏感信息的配置文件，比如存放口令的配置文件。
# 干货
## 干货
### 干货
#### 干货
   
  [干货移步本页面哈哈](https://github.com/awesometime/learn-git/)  `我们称此界面为Edit file，展示给别人的为展示界面`
```
  #空格就会以标题形式显示
  
  隔一行就会换行显示，否则会跟在本行右边
  
  Tab缩进一次，就会无格式按你在Edit file中的样子（原来隔行现在也隔行显示）一模一样的显示出来
  
  Tab缩进两次，就会单独显示在一块区域，而且支持下边拖动
  
  Tab缩进两次后，此处的换行在展示界面不会换行，而是一直往右显示，可以拖动查看，想要换行使用enter
```
# github在线编辑
  github上只能删除仓库,却无法删除文件夹或文件, 所以只能通过命令来解决
  [github上怎么删除一个文件夹](https://zhidao.baidu.com/question/2270316787503627828.html)

# git学习目录

    1 Git简介
        1.1---Git的诞生
        1.2---集中式vs分布式
    2 安装Git
    3 创建版本库
    4 时光机穿梭
        4.1---版本回退
        4.2---**工作区和暂存区**
        4.3---管理修改
        4.4---撤销修改
        4.5---删除文件
    5 远程仓库
        5.1---添加远程库
        5.2---从远程库克隆
    6 分支管理
        6.1---创建与合并分支
        6.2---解决冲突
        6.3---分支管理策略
        6.4---Bug分支
        6.5---Feature分支
        6.6---多人协作
        6.7---Rebase
    7 标签管理
        7.1---创建标签
        7.2---操作标签
    8 使用GitHub
    9 使用码云
    10 自定义Git
        10.1---忽略特殊文件
        10.2---配置别名
        10.3---搭建Git服务器
    11 总结


 

初始化一个Git仓库，使用git init命令。

添加文件到Git仓库，分两步：
    1 使用命令git add <file>，注意，可反复多次使用，添加多个文件；
    2 使用命令git commit -m <message>，完成

要随时掌握工作区的状态，使用git status命令。

如果git status告诉你有文件被修改过，用git diff可以查看修改内容。

HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。

穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。

要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

# 4.1版本回退
   
    HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。

    穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本，git log命令显示从最近到最远的提交日志。

    要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

# 6.1创建与合并分支

  查看分支：git branch             

  创建分支：git branch <name>

  切换分支：git checkout <name>

  创建+切换分支：git checkout -b <name>

  合并某分支到当前分支：git merge <name>

  删除分支：git branch -d <name>

# 6.6多人协作
    
    查看远程库信息，使用git remote -v；
    
    本地新建的分支如果不推送到远程，对其他人就是不可见的；

    从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；

    在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；

    建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；

    从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。
# 6.7Rebase
    $ git log --graph --pretty=oneline --abbrev-commit
    * d1be385 (HEAD -> master, origin/master) init hello      Git用(HEAD -> master)和(origin/master)标识出当前分支的HEAD和远程origin的位置分别是582d922 add author和d1be385 init hello，本地分支比远程分支快两个提交。   
    *   e5e69f1 Merge branch 'dev'
    |\  
    | *   57c53ab (origin/dev, dev) fix env conflict
    | |\  
    | | * 7a5e5dd add env
    | * | 7bd91f1 add new env
    | |/  
    * |   12a631b merged bug fix 101
    |\ \  
    | * | 4c805e2 fix bug 101
    |/ /  
    * |   e1e9c68 merge with no-ff
    |\ \  
    | |/  
    | * f52c633 add merge
    |/  
    *   cf810e4 conflict fixed
    
# 7.1创建标签
    命令git tag <tagname>用于新建一个标签，默认为HEAD，也可以指定一个commit id；

    命令git tag -a <tagname> -m "blablabla..."可以指定标签信息；

    命令git tag可以查看所有标签。
    
    注意：标签总是和某个commit挂钩。如果这个commit既出现在master分支，又出现在dev分支，那么在这两个分支上都可以看到这个标签。
    
# 7.2操作标签
    命令git push origin <tagname>可以推送一个本地标签；  
    
    命令git push origin --tags可以推送全部未推送过的本地标签；

    命令git tag -d <tagname>可以删除一个本地标签；

    命令git push origin :refs/tags/<tagname>可以删除一个远程标签。
# 8 使用GitHub
    在GitHub上，可以任意Fork开源仓库；fork your own copy of 要克隆的项目名 to your account

    自己拥有Fork后的仓库的读写权限；

    可以推送pull request给官方仓库来贡献代码。

例子
如何参与一个开源项目呢？比如人气极高的bootstrap项目，这是一个非常强大的CSS框架，你可以访问它的项目主页https://github.com/twbs/bootstrap，点“Fork”就在自己的账号下克隆了一个bootstrap仓库，然后，从自己的账号下clone：

git clone git@github.com:自己账号/bootstrap.git
一定要从自己的账号下clone仓库，这样你才能推送修改。如果从bootstrap的作者的仓库地址git@github.com:twbs/bootstrap.git克隆，因为没有权限，你将不能推送修改。
希望bootstrap的官方库能接受你的修改，你就可以在GitHub上发起一个pull request


有空学习一下bootstrap这个界面

## 10.2 配置别名
 用st表示status，co表示checkout，ci表示commit，br表示branch：

    git config --global alias.st status
    git config --global alias.co checkout
    git config --global alias.ci commit   
    git config --global alias.br branch

 配置一个git last，让其显示最后一次提交信息：
    
    git config --global alias.last 'log -1'

    git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

 配置Git的时候，加上--global是针对**当前用户**起作用的，如果不加，那只针对**当前仓库**起作用。
 
 每个仓库的Git配置文件都放在.git/config文件中
 
 当前用户的Git配置文件放在用户主目录下的一个隐藏文件.gitconfig中


# git实践
- [git 教程](https://www.yiibai.com/git/git_push.html)
- [通过pycharm使用git[图文详解]](http://www.cnblogs.com/caseast/p/6085837.html)
- [Git安装和初次使用](https://www.cnblogs.com/ximiaomiao/p/7140456.html)

要有**本地仓库**和**远程仓库**两个概念

本地有```master分支```                 对应远程有```origin/master分支```

如 ```master  -> origin/master```     表示本地master分支上传到远程origin/master分支


**@linuix MINGW64 ~**

**$ cd /G:/PyCharm/PythonProjects/cmdb**

**@linuix MINGW64 /G/PyCharm/PythonProjects/cmdb (master|MERGING)**

**$ git status**
    
    On branch master
    Your branch and 'origin/master' have diverged,
    and have 1 and 9 different commits each, respectively.
      (use "git pull" to merge the remote branch into yours)

    All conflicts fixed but you are still merging.
      (use "git commit" to conclude merge)

    Changes to be committed:

            modified:   README.md
            new file:   cmdb/settings.py
            new file:   cmdb_dashboard.png

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            Client/__pycache__/
            Client/bin/__pycache__/
            Client/conf/__pycache__/
            Client/core/__pycache__/
            Client/plugins/__pycache__/
            Client/plugins/windows/__pycache__/
            assets/__pycache__/
            assets/migrations/__pycache__/


**@linuix MINGW64 /G/PyCharm/PythonProjects/cmdb (master|MERGING)**

**$ git log**
    
    commit 061c1b12c6c7946e3f63d31bbf2687924e81ced9 (HEAD -> master)
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Mon Sep 17 11:28:13 2018 +0800

        add some annotations

    commit d47c87973692f62be228dae500b3d8afdb25ee24
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Wed Sep 12 13:13:41 2018 +0800

        Initial commit

**@linuix MINGW64 /G/PyCharm/PythonProjects/cmdb (master|MERGING)**

**$ git branch**
    
    * master

**@linuix MINGW64 /G/PyCharm/PythonProjects/cmdb (master|MERGING)**

**$ git pull origin master**

    error: You have not concluded your merge (MERGE_HEAD exists).
    hint: Please, commit your changes before merging.
    fatal: Exiting because of unfinished merge.

    如果之前已经正确clone后，可以通过git pull进行同步代码，可指定分支

    git pull                     # 是pull当前分支的最新代码

    git pull origin dev          # 表示fetch origin 的dev分支到当前目录,并与当前分支合并,相当于git fetch origin dev

    && git merge origin dev,取下来再合并

    git pull origin dev:master   # 表示从远端origin dev取下代码，并与本地的master分支合并（非当前分支）

    git branch                   # 查看当前分支

    git reset --hard 08b07fd34cba9c8a69f72da09d142409baf81cee  # 回滚代码到08b..这个版本（此版本可从gitlab获取到）


**@linuix MINGW64 /G/PyCharm/PythonProjects/cmdb (master|MERGING)**

**$ git commit**          

    [master da554bc] Merge remote-tracking branch 'remotes/origin/master'

    git commit                  将暂存区里的改动给提交到**本地的版本库**
    git commit -m “message”     这种是比较常见的用法，-m 参数表示可以直接输入后面的“message”，如果不加 -m参数，
    那么是不能直接输入message的，而是**会调用一个编辑器一般是vim**来让你输入这个message，
    message即是我们用来简要说明这次提交的语句


**@linuix MINGW64 /G/PyCharm/PythonProjects/cmdb (master)**

**$ git status**
    
    On branch master
    Your branch is ahead of 'origin/master' by 2 commits.
      (use "git push" to publish your local commits)

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

            Client/__pycache__/
            Client/bin/__pycache__/
            Client/conf/__pycache__/
            Client/core/__pycache__/
            Client/plugins/__pycache__/
            Client/plugins/windows/__pycache__/
            assets/__pycache__/
            assets/migrations/__pycache__/

    nothing added to commit but untracked files present (use "git add" to track)

**@linuix MINGW64 /G/PyCharm/PythonProjects/cmdb (master)**

**$ git log**

    commit da554bc4c4314e7ec94aac53dbaf7002a6c71f12 (HEAD -> master)
    Merge: 061c1b1 9c3a780
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Mon Sep 17 13:31:33 2018 +0800

        Merge remote-tracking branch 'remotes/origin/master'

    commit 061c1b12c6c7946e3f63d31bbf2687924e81ced9
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Mon Sep 17 11:28:13 2018 +0800

        add some annotations

    commit 9c3a7801e13d567fa773f8f7a97c0b1b921d14e5 (origin/master)
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Fri Sep 14 21:38:31 2018 +0800

        Update info_collection.py

    commit a3db96bd23bfaf4e8cc5043cc082592e36e3df4a
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Fri Sep 14 21:13:08 2018 +0800

        Update main.py

    commit 7e99012d2152e727417df53c82daa54690d21ad2
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Fri Sep 14 21:11:32 2018 +0800

        Update handler.py

    commit ccace8878bfa78eb3c58d1cd29daa9df7c427f39
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Fri Sep 14 21:10:53 2018 +0800

        Update handler.py

    commit a57fa8b6b84900cd7e01db3de2ed77e247e6362b
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Fri Sep 14 21:05:32 2018 +0800

        Update handler.py

    commit a96e39f3150d24a598ef3c97261aa0714078f85f
    Author: awesometime <31882243+awesometime@users.noreply.github.com>
    Date:   Wed Sep 12 13:27:48 2018 +0800

        Add files via upload


**@linuix MINGW64 /G/PyCharm/PythonProjects/cmdb (master)**

**$ git push origin master**

    Enumerating objects: 70, done.
    Counting objects: 100% (55/55), done.
    Delta compression using up to 4 threads.
    Compressing objects: 100% (24/24), done.
    Writing objects: 100% (26/26), 7.52 KiB | 145.00 KiB/s, done.
    Total 26 (delta 15), reused 0 (delta 0)
    remote: Resolving deltas: 100% (15/15), completed with 14 local objects.
    To https://github.com/awesometime/CMDB.git
       9c3a780..da554bc  master -> master

    git push origin master       将**本地的master分支**推送到**origin主机的master分支**。如果master不存在，则会被新建。


**@linuix MINGW64 /g/pycharm/pythonprojects/cmdb (master)**

**$ git log --graph --pretty=oneline --abbrev-commit**

    *   da554bc (HEAD -> master, origin/master) Merge remote-tracking branch 'remotes/origin/master'
    |\
    | * 9c3a780 Update info_collection.py
    | * a3db96b Update main.py
    | * 7e99012 Update handler.py
    | * ccace88 Update handler.py
    | * a57fa8b Update handler.py
    | * a96e39f Add files via upload
    | * b79a87f Update settings.py
    | * bb58c8d Add files via upload
    | * 5ec097c Update README.md
    * | 061c1b1 add some annotations
    |/
    * d47c879 Initial commit

```






