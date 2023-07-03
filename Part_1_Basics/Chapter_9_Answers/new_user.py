from user_classes import Admin

# Create a new admin to show import statement is working
user_06 = Admin('felix', 'jones', 25, 'felix25', 'san luis', 'mexico')
user_06_privileges = [
    'can add post',
    'can delete post',
    'can ban user', 
    'can restrict user activity'
]

user_06.privileges.privileges = user_06_privileges
user_06.describe_user()
print("\n")
user_06.privileges.show_privileges()