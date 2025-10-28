# Fundamental Software Development assignment
2025 S2 32555 Group #3-Cmp1-01
## Team members
25739703 – Xinyue An\
25605561 – Yinglan Li\
13154719 – Fanke Qin\
25629573 – Yuzhe Zheng

## How to start
Requirements
    Python 3.7 or above
    Required packages:
    `pip install colorama`

Project Structure

This project includes two main parts:
    1.CLIUniApp — Command-line version.
    2.GUIUniApp — Graphical version built with Tkinter.
    Do not separate the two folders. The GUI part depends on files from the CLI part.

Run CLI Application
In the CLIUniApp directory, run: `main.py`
This will start the command-line version of the UniApp system.

Run GUI Application
After ensuring the CLI files are intact, go to GUIUniApp and run:`main.py`
The GUI version will launch automatically, providing login and enrolment windows.

## Contributions
| Member               | Responsibilities                                                                                                                                                                             | Notes                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Yinglan Li**         | Implemented core data management and file persistence (`storage.py`, `student.json`), utility modules (`utils.py`, `student_system.py`, `admin_system.py`), and overall project integration. | Designed the JSON-based storage system to replace the original `database.py` (deprecated). |
| **Yuzhe Zheng** | Developed `admin_controller.py` and initial `database.py` structure for data handling.                                                                                                       | The original `database.py` concept guided the later `storage.py` redesign.                 |
| **Fanke Qin**           | Implemented `student_controller.py` and corresponding model `student.py`.                                                                                                                    | Focused on student login, validation, and enrolment logic.                                 |
| **Anxin Yue**             | Implemented `subject_controller.py` and model `subject.py`.                                                                                                                                  | Focused on subject display and enrolment integration.                                      |



## git指令
git中分为本地项目，暂存区，本地仓库，远程仓库
![git workflow](<git workflow.png>)

以下为一般默认流程
#### 一
先在 命令指示符上 输入git账号信息\
`git config --global user.name"xxxx"` \
`git config --global user.email"xxxxx@gmail.com"`\
（没有成功也不要紧）

#### 二
在本地项目目录创建本地仓库\
`git init`\
输入完命令后项目目录会有一个隐藏的.git文件夹

#### 三
上传所有代码到本地仓库\
`git add .` (注:这个点指当前所有代码)\
也可以 git add 文件名.py 只上传部分文件

#### 四
代码上传到本地仓库后执行提交命令\
`git commit -m "项目名称" ` \
(引号里的字符串为备注，你可以写任何内容，尽量清楚一点，让别人也能看懂)

#### 五
关联本地仓库并上传代码\
`git remote add origin https://github.com/xxx.git ` (就是共享的SSH地址)\
如果之前`git config`没有成功登录，这时会跳出来网页让你再次登录验证一下

#### 六
最后执行上传推送命令\
`git push origin 支线的名字` (一般是main或者master)\
但是便于代码的修改，一般不建议直接上传到主线
可以自己先在本地创建一个分支，再上传分支，审查后再合并

## 分支管理
Git 分支管理是 Git 强大功能之一，能够让多个开发人员并行工作，开发新功能、修复 bug 或进行实验，而不会影响主代码库。
![alt text](git-brance.png)

#### 创建分支
创建新分支并切换到该分支：\
`git checkout -b branchname`  \
切换分支命令: \
`git checkout branchname`
#### 查看分支
查看所有分支：\
`git branch` \
查看远程分支：\
`git branch -r` \
查看所有本地和远程分支： \
`git branch -a `
#### 删除分支
删除本地分支：\
`git branch -d branchname` \
强制删除未合并的分支：\
`git branch -D branchname` \
删除远程分支： \
`git push origin --delete branchname `

#### 克隆代码
如果你觉得别人的代码特别好，或者需要修改别人的代码，也可以直接克隆下来修改
`git clone git@github.com:yinglan-Linda/FSD-assignment.git `