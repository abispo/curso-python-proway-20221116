
from database import engine, Base, session
from models import User


def list_users():
    # SELECT * FROM tb_users
    return session.query(User).all()


def create_user(email, password):
    pass
    


if __name__ == "__main__":

    # Cria as tabelas definidas no módulo models.py
    Base.metadata.create_all(engine)

    while True:

        output = """
        INFORME A OPÇÃO DESEJADA:
        
        1 - Mostrar usuários cadastrados
        2 - Inserir um novo usuário
        3 - Atualizar as informações de um usuário
        4 - Apagar um usuário
        5 - Sair
        """

        print(output)
        option = int(input("Informe a opção: "))

        if option == 1:
            users = list_users()

            if len(users) == 0:
                print("NÃO EXISTEM USUÁRIOS CADASTRADOS")

        elif option == 2:
            pass

        elif option == 3:
            pass

        elif option == 4:
            pass

        elif option == 5:
            print("Saindo...")
            break

        else:
            print(f"OPÇÃO DESCONHECIDA: {option}.")