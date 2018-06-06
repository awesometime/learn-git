<p align="center">
  
  <h3 align="center">learn-git</h3>

  <p align="center">
    学习，我是认真的.    
    <br>   
    <a href="https://github.com/awesometime/">awesometime的github主页</a>    
    
  </p>
</p>

- [干货](#干货)
- [git学习目录](#git学习目录)
- [What's included](#whats-included)

# 干货
## 干货
### 干货
  我们称此界面为Edit file，展示给别人的为展示界面
  
  -#空格就会以标题形式显示
  
  -隔一行就会换行显示，否则会跟在本行右边
  
  -Tab缩进一次，就会无格式按你在Edit file中的样子（原来隔行现在也隔行显示）一模一样的显示出来
  
  -Tab缩进两次，就会单独显示在一块区域，而且支持下边拖动
  
  -Tab缩进两次后，此处的换行在展示界面不会换行，而是一直往右显示，可以拖动查看
# git学习目录

    1 Git简介
        1.1---Git的诞生
        1.2---集中式vs分布式
    2 安装Git
    3 创建版本库
    4 时光机穿梭
        4.1---版本回退
        4.2---工作区和暂存区
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
