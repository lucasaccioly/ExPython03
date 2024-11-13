def fazer_login(login, senha):
    login_padrao = "lxcvs"
    senha_padrao = "555"
    if login == login_padrao and senha == senha_padrao:
        return "logado"
    else:
        return "login ou senha incorretos"
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")
resultado = fazer_login(login, senha)
print(resultado)