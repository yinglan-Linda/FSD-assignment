import json
import random

class User:
    def __init__(self,name,email,password, id=None, subjects=None):
        self.name = name 
        self.email = email
        self.password = password
        self.id = id or ""
        self.subjects = list(subjects or [])

    def match(self,email,password):
        return self.email == email and self.password == password
    
# class Student:
#     def __init__(self, student_id: str, name: str, email: str, subjects: list):
#         self.student_id = student_id
#         self.name = name
#         self.email = email
#         # subjects: [{"id":"311","mark":81,"grade":"D"}, ...]
#         self.subjects = subjects or []

class Database:
    def __init__(self):
        self.users = self.loadData()
        self._json_path = "./CLIUniApp/data/student.json"
    
    def loadData(self):
        with open("./CLIUniApp/data/student.json", "r") as f:
            data = json.load(f)
        # return [User(s["name"], s["email"], s["password"])
        #         for s in data.get("student", [])]
        users = []
        for s in data.get("student", []):
            users.append(User(
                name=s.get("name", ""),
                email=s.get("email", ""),
                password=s.get("password", ""),
                id=s.get("ID") or s.get("id") or "",     # ← 并入到 User
                subjects=s.get("subject", [])                    # ← 并入到 User
                )
            )
        return users
        
    def match(self,email,password):
        for user in self.users:
            if user.match(email,password):
                return user
        return None
    
    # 将当前内存中的 users 写回 JSON
    def saveAllUsers(self):
        payload = {"student": []}
        for u in self.users:
            payload["student"].append({
                "name": u.name,
                "email": u.email,
                "password": u.password,
                "ID": u.student_id,
                "subject": u.subjects,  # [{"id": "3xx", "mark": ..., "grade": ...}]
            })
        with open(self._json_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    # 仅更新某个 user 后保存
    def saveUser(self, user):
        # 这里按 email 对齐更新（也可以按 ID）
        for i, u in enumerate(self.users):
            if u.email == user.email:
                self.users[i] = user
                break
        self.saveAllUsers()
    
class Subject:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name

class SubjectRepository:
    def __init__(self):
        # 先写死，后面可以换成从 ./CLIUniApp/data/subjects.json 读取
        self._subjects = []
        self._usedIDs = set()
        # 预生成 300~399 的所有ID并打乱，逐个弹出使用
        self._pool = [f"3{i:02d}" for i in range(100)]
        random.shuffle(self._pool)
        self._init_default_subjects()

    def popSubID(self) -> str:
        if not self._pool:
            raise ValueError("No more IDs in 300-399 range")
        return self._pool.pop()
    
    def _init_default_subjects(self):
        names = ["Python", "Java", "JavaScript", "HTML", "PHP", "C++"]
        for nm in names:
            sid = self.popSubID()
            self._subjects.append(Subject(sid, nm))

    def listAll(self):
        return list(self._subjects)