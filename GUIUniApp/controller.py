import model

class UserController:
    def __init__(self):
        self.model = model.Database()
    
    def login(self, email, password):
        # returns the user if matches, otherwise returns None
        user = self.model.match(email,password)
        if user:
            # Logger.save(user)
            return user, f"Welcome {user.name}"
        else:
            return None, "Incorrect email or password"
        
class EnrolController:
    def __init__(self):
        self.repo = model.SubjectRepository()
        self.db = model.Database() 
        self.tempSelected = []   # 用list或set都可以

    def getSubjects(self):
        return self.repo.listAll()

    def enrol(self, user, subjectNum):   
        """临时验证 + 计数返回"""
        if len(subjectNum) == 4:
            # 合并已有和新选的
            for sid in subjectNum:
                user.subjects.append({"id": sid, "mark": None, "grade": ""})
                if sid not in self.tempSelected:
                    self.tempSelected.append(sid)
        else:
            # 如果超限，不添加本次勾选
            if len(self.tempSelected) != 4:
                # 把刚添加的撤回，防止越界
                for sid in subjectNum:
                    if sid in self.tempSelected:
                        self.tempSelected.remove(sid)
                return False, f"You must select FOUR subjects.", len(self.tempSelected)
        # 在此保存选课（写文件/数据库等）
        self.db.saveUser(user)

        # 成功：返回现在选了几门
        return True, "Enrolment successful.", len(self.tempSelected)
    
class SubjectController:
    def __init__(self):
        self.db = model.Database()

    def getEnrolledSubjects(self, user):
        return list(user.subjects)
    
    # def saveNewSubjects(self, user, selected_ids: list[str]):
    #     # 原有已选
    #     have = {rec.get("id") for rec in (user.subjects or [])}
    #     # 仅添加“新选择”的
    #     new_ids = [sid for sid in selected_ids if sid not in have]

    #     # 追加新课程，成绩/等级留空（None 或 "" 均可，这里用 None）
    #     for sid in new_ids:
    #         user.subjects.append({"id": sid, "mark": None, "grade": None})

    #     # 写回文件
    #     self.db.saveUser(user)
    #     return True, f"Enrolment successful. You now have {len(user.subjects)}/ FOUR subjects."