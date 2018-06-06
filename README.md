# learn-git
# 干货
  #空格就会以标题形式显示
  
  隔一行就会换行显示，否则会跟在本行右边
  
  Tab缩进就会单独显示在一块区域，而且支持下表边拖动
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
    * d1be385 (HEAD -> master, origin/master) init hello
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
