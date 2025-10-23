import tkinter as tk
import controller as cl
from tkinter import ttk, messagebox as mb

class LoginFrame(tk.LabelFrame):
    def __init__(self,parent):
        super().__init__(parent, text="Login In", fg="#333",
                         padx=50, pady=50, font="Helvetica 10 bold")
        self.parent = parent
        self.controller = cl.UserController()
        self.pack(fill="both", expand=True)

        self.columnconfigure(0, weight=1) # 自适应
        self.columnconfigure(1, weight=1)

        # create widgets
        self.email = tk.Label(self,text="Email",justify="left",fg="#333",
                        font="Helvetica 12 bold")
        self.email.grid(column=0,row=0,padx=5,pady=5,sticky="e")

        self.password = tk.Label(self,text="Password",fg="#333",
                            font="Helvetica 12 bold")
        self.password.grid(column=0,row=1,padx=5,pady=5,sticky="e")

        self.emailText = tk.StringVar()
        self.emailField = tk.Entry(self,textvariable=self.emailText)
        self.emailField.grid(column=1,row=0,padx=5,pady=5,sticky="we")
        self.emailField.focus()

        self.passwordText = tk.StringVar()
        self.passwordField = tk.Entry(self,textvariable=self.passwordText,show="*")
        self.passwordField.grid(column=1,row=1,padx=5,pady=5,sticky="we")

        self.cancelBtn = tk.Button(self,text="Cancel", command=self.clear)
        self.cancelBtn.grid(column=1,row=3,sticky="W",padx=5,pady=5)
        self.loginBtn = tk.Button(self,text="Login",command=self.login)
        self.loginBtn.grid(column=1,row=3,sticky="E",padx=5,pady=5)

        self.pack(padx= 5, pady=5)

    def clear(self):
        self.emailField.delete(0,tk.END)
        self.passwordField.delete(0,tk.END)
    
    def login(self):
        email = self.emailText.get()
        password = self.passwordText.get()

        print(f"Trying to log in with: {email}, {password}")

        user, message = self.controller.login(email, password)
        print("Controller returned:", user, message)

        if user:
            self.destroy()   # 销毁当前的登录框
            SubjectFrame(self.parent, user)
        else:
            mb.showerror(title="Login Error", message=message)
        self.clear()

class SubjectFrame(tk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.parent = parent 
        self.user = user # 保存当前用户
        self.ctrl = cl.SubjectController()

        # 页面骨架
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)

        # Top title: left: Weclome user, right logout
        header = ttk.Frame(self)
        header.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        header.grid_columnconfigure(0, weight=1)  # fullfill left
        header.grid_columnconfigure(1, weight=0)

        label = tk.Label(header, text=f"Welcome {user.name}!",
                        fg="#ffc107", font="Helvetica 16 bold")
        label.grid(row=0, column=0, sticky="w")   # left top corner

        studentID = ttk.Label(header, text=f"student ID: {user.id}")
        studentID.grid(row=0, column=1, sticky="e")  # right top corner

        # Subjects List
        self.enSub = ttk.Frame(self)
        self.enSub.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.enSub.grid_columnconfigure(0, weight=0)  # ID 列
        self.enSub.grid_columnconfigure(1, weight=0)  # mark 列
        self.enSub.grid_columnconfigure(2, weight=1)  # grade 列可拉伸

        # 表头
        # hdr_style = dict(fg="#333", font="Helvetica 12 bold")
        ttk.Label(self.enSub, text="ID").grid(row=0, column=0, sticky="n", padx=(0,10))
        ttk.Label(self.enSub, text="mark").grid(row=0, column=1, sticky="n", padx=(0,10))
        ttk.Label(self.enSub, text="grade").grid(row=0, column=2, sticky="w")

        rows = self.ctrl.getEnrolledSubjects(self.user) 

        if rows:
            for r, rec in enumerate(rows,start=1):
                # v = tk.BooleanVar(value=False)
                # ID
                stuID = ttk.Label(self.enSub, text=str(rec["id"]))
                stuID.grid(row=r, column=0, sticky="w", padx=(0,10))
                # mark
                studentName = ttk.Label(self.enSub, text=str(rec["mark"]))
                studentName.grid(row=r, column=1, sticky="w", pady=4)
                # grade
                studentName = ttk.Label(self.enSub, text=str(rec["grade"]) )
                studentName.grid(row=r, column=2, sticky="w", pady=4)
        else: 
            ttk.Label(self.enSub, text="No enrolled subjects found.").grid(row=1, column=0, columnspan=3, sticky="w")

        #footer
        footer = ttk.Frame(self)
        footer.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        footer.grid_columnconfigure(0, weight=1)  # fullfill left
        footer.grid_columnconfigure(1, weight=0)

        self.enrolBtn = ttk.Button(footer, text="enroll new subjects", command = self.newSubject)
        self.enrolBtn.grid(row=2, column=0, sticky="e", padx=10, pady=(0,10))

    def newSubject(self):
        self.destroy()   # 销毁当前页面
        EnrollFrame(self.parent,self.user)

class EnrollFrame(tk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.user = user # 保存当前用户
        self.subController = cl.EnrolController() # 构建 subjects 表时，使用 controller 提供的数据

        # Top title
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)   # 下面“列表区域”可拉伸
        self.grid_columnconfigure(0, weight=1)

        # Top title: left: Weclome user, right logout
        header = ttk.Frame(self)
        header.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        # header.grid_columnconfigure(0, weight=1)  # fullfill left
        # header.grid_columnconfigure(1, weight=0)

        label = tk.Label(header, text=f"Welcome {user.name}!",
                        fg="#ffc107", font="Helvetica 16 bold")
        label.grid(row=0, column=0, sticky="w")   # left top corner

        logoutBtn = ttk.Button(header, text="Logout", command=parent.destroy)
        logoutBtn.grid(row=0, column=1, sticky="e" ,padx=(10,0))  # right top corner

        # Subjects List
        self.subjectsList = ttk.Frame(self)
        self.subjectsList.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.subjectsList.grid_columnconfigure(0, weight=0)  # checkbox 列
        self.subjectsList.grid_columnconfigure(1, weight=0)  # ID 列
        self.subjectsList.grid_columnconfigure(2, weight=1)  # Name 列可拉伸

        # 表头
        # hdr_style = dict(fg="#333", font="Helvetica 12 bold")
        ttk.Label(self.subjectsList, text="Select").grid(row=0, column=0, sticky="n", padx=(0,10))
        ttk.Label(self.subjectsList, text="ID").grid(row=0, column=1, sticky="n", padx=(0,10))
        ttk.Label(self.subjectsList, text="Name").grid(row=0, column=2, sticky="w")

        # subList = ["python", "java","javascript", "HTML", "php", "C++"]
        subList = self.subController.getSubjects()
        self._rows = subList  # 与 self._subjectVars 对齐，收集 ID
        self._subjectVars = []
        checks = []

        # Subjects list with checkbox
        for r, subj in enumerate(subList,start=1):
            v = tk.BooleanVar(value=False)
            # checkbox
            chk = ttk.Checkbutton(self.subjectsList, variable=v)
            chk.grid(row=r, column=0, sticky="we", pady=4)
            # ID
            subID = ttk.Label(self.subjectsList, text=str(subj.sid))
            subID.grid(row=r, column=1, sticky="e", padx=(0,10))
            # Subject name
            subName = ttk.Label(self.subjectsList, text=subj.name, anchor="w")
            subName.grid(row=r, column=2, sticky="ew")

            self._subjectVars.append(v)
            checks.append(chk)
        
        # self._rows = subList   # 与 self._subject_vars 对齐，收集 ID

        # self.selectedLabel = ttk.Button(self, text="Selected (0)", command=self.show_selected)
        # self.selectedLabel.grid(row=2, column=0, sticky="w", padx=10, pady=(0,10))

        self.enrolBtn = ttk.Button(self, text="enrol", command = self._enrol)
        self.enrolBtn.grid(row=2, column=0, sticky="e", padx=10, pady=(0,10))

    def _enrol(self):
        selectedIds = [row.sid for row, var in zip(self._rows, self._subjectVars) if var.get()]
        ok, msg, total = self.subController.enrol(self.user, selectedIds)  # 传真实 user
        detail = f"\nYou now have {total} subjects selected."
        if ok:
            mb.showinfo("Enrol Success", msg + detail)
            # 成功后跳回成绩页
            self.destroy()
            SubjectFrame(self.master, self.user)
        else:
            mb.showerror("Enrol Fail", msg + f"\n(You currently have {total}.)")
