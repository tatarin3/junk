import socialdbmenu

if __name__ == '__main__':
    while True:
        username = socialdbmenu.login_menu()
        while socialdbmenu.menu(username):
            pass
