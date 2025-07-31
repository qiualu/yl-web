
Docker 项目


# github
* 克隆一个远程仓库到本地
git clone <repository-url>
* 查看当前仓库的工作树状态、暂存区状态和最近的提交记录
git status
* 将文件的变化添加到暂存区
* <file> 表示单个文件，使用 . 表示所有修改过的文件
git add <file>
git add *
* 提交暂存区的改动到本地仓库，并附上提交信息  
* 将本地的改动推送到远程仓库的指定分支
* <branch-name> 表示分支名，如果不指定则默认推送到当前分支
git push origin <branch-name> | git push
git push origin main

* 从远程仓库的指定分支拉取改动并合并到当前分支
* <branch-name> 表示分支名，如果不指定则默认拉取当前分支的更新
git pull origin <branch-name> | git pull
git pull origin main

* 显示提交历史
git log
* 创建一个新分支，但不会自动切换到新分支
git branch <branch-name>
* 切换到指定分支
git checkout <branch-name>
* 合并指定分支到当前分支
git merge <source-branch>
* 删除本地分支
* -d 是安全删除，如果分支未合并会失败；-D 是强制删除
git branch -d <branch-name> | git branch -D <branch-name>
* 删除远程分支
git push origin --delete <branch-name>
* 查看远程仓库的URL和分支信息
git remote -v
* 添加一个新的远程仓库
git remote add origin <repository-url>
* 列出所有本地和远程分支
git branch -a
* 基于远程分支创建一个新的本地分支并切换到该分支
git checkout -b <branch-name> origin/<branch-name>
* 撤销工作目录中文件的改动，回到最近一次git commit或git add时的状态
git checkout -- <file>
* 列出Git配置信息
git config --list
* 设置Git全局用户名和邮箱，这些信息会用于提交记录
git config --global user.name 'Your Name'
git config --global user.email 'your-email@example.com'

使用 git checkout <commit-hash> -- <file> 来检出该文件在特定提交中的版本。
git checkout main .gitignore 

CRLF 转换为 LF 在提交到仓库时，但检出时不会转换。false 则完全不做转换
git config --global core.autocrlf input
# 或者
git config --global core.autocrlf false



# 更改到 Gitee 

简易的命令行入门教程:
<!-- Git 全局设置: -->

git config --global user.name "美哉"
git config --global user.email "494436488@qq.com"
<!-- 创建 git 仓库: -->

mkdir xxx
cd xxx
git init 
touch README.md
git add README.md
git commit -m "first commit"
git remote add origin https://gitee.com/meizai55/yl-web.git
git push -u origin "master"
<!-- 已有仓库? -->

cd existing_git_repo
git remote add origin https://gitee.com/meizai55/yl-web.git
git push -u origin "master"


删除现有的 origin 远程仓库：
bash
git remote remove origin

