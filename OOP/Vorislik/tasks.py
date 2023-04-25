# class Talaba:
#     def __init__(self, name, group):
#         self.name = name
#         self.group = group
#         self.subjects = []

#     def subjects_count(self):
#         return len(self.subjects)
    

# t1 = Talaba('Baxtiyor', '213')
# print(t1.subjects_count())


# 2
# class Fan:
#     def __init__(self, name) -> None:
#         self.name = name

#     def get_info(self):
#         return self.name

# fan1 = Fan('Matematika')
# fan2 = Fan('Fizika')

# 7
class Foydalanuvchi:
    def __init__(self, name):
        self.name = name
    
class Admin(Foydalanuvchi):
    def __init__(self, name):
        super().__init__(name)
        self.ban_users = []

    def ban_user(self, obj):
        self.ban_users.append(obj.name)
        print(f"{obj.name} foydalanuvchi bloklandi")

    def is_ban(self, obj):
        return f"{obj.name} foydalanuvchi bloklangan" if obj.name in self.ban_users else f"{obj.name} foydalanuvchi bloklanmagan"
    
f1 = Foydalanuvchi('Baxtiyor')
f2 = Foydalanuvchi('Baxtiyor2')
f3 = Foydalanuvchi('Baxtiyor3')

admin = Admin('Admin')
admin.ban_user(f3)
print(admin.is_ban(f3))

print(admin.ban_users)