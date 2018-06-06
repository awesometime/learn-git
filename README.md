# learn-git
# 干货
  #空格就会以标题形式显示
  
  Tab缩进就会单独显示在一块区域，而且支持下表边拖动
# git学习目录

    Git简介
        |---Git的诞生
        |---集中式vs分布式
    安装Git
    创建版本库
    时光机穿梭
        |---版本回退
        |---工作区和暂存区
        |---管理修改
        |---撤销修改
        |---删除文件
    远程仓库
        |---添加远程库
        |---从远程库克隆
    分支管理
        |---创建与合并分支
        |---解决冲突
        |---分支管理策略
        |---Bug分支
        |---Feature分支
        |---多人协作
        |---Rebase
    标签管理
        |---创建标签
        |---操作标签
    使用GitHub
    使用码云
    自定义Git
        |---忽略特殊文件
        |---配置别名
        |---搭建Git服务器
    总结


 

初始化一个Git仓库，使用git init命令。

添加文件到Git仓库，分两步：
    1 使用命令git add <file>，注意，可反复多次使用，添加多个文件；
    2 使用命令git commit -m <message>，完成

要随时掌握工作区的状态，使用git status命令。

如果git status告诉你有文件被修改过，用git diff可以查看修改内容。

HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。

穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。

要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。


# 创建与合并分支

      查看分支：git branch

      创建分支：git branch <name>

      切换分支：git checkout <name>

      创建+切换分支：git checkout -b <name>

      合并某分支到当前分支：git merge <name>

      删除分支：git branch -d <name>

# 多人协作
    
        查看远程库信息，使用git remote -v；

        本地新建的分支如果不推送到远程，对其他人就是不可见的；

        从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；

        在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；

        建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；

        从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。
