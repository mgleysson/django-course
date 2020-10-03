class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return 'Credentials: ' + self.username + ' - ' + self.password

    def login(self):
        print('Login done by "%s".' % self.username)


felipe = User(username='felipe', password='pass_user')
print(felipe)
felipe.login()


class Admin(User):

    def __init__(self, username, password, phone, email):
        super().__init__(username, password)
        self.phone = phone
        self.email = email
        self.user = None

    def remove_user_account(self, user):
        self.user = user
        print(f'%s removeu conta do usuário "%s"' % (self.username, self.user.username))

    def accept_user_account(self, user):
        self.user = user
        print('%s aceitou conta do usuário "%s"' % (self.username, self.user.username))


admin = Admin(username='marcos', password='pass_admin', phone='9999-9999', email='admin@admin.com')
print(admin)
admin.login()
print(admin.phone)
print(admin.email)
admin.remove_user_account(felipe)

joao = User(username='joao', password='123')

admin.accept_user_account(joao)

