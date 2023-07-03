from user import User
from adminprivileges import Admin, Privileges

# Create a new instance of an admin and their privileges
user_07 = Admin('mario', 'gomez', 50, 'mario70', 'palermo', 'italy')
user_07_privileges = [
    'can add post',
    'can delete post',
    'can ban user', 
    'can restrict user activity'
]

user_07.privileges.privileges = user_07_privileges

user_07.describe_user()
user_07.privileges.show_privileges()