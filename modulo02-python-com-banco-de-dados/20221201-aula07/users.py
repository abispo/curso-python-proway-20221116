1
from database import engine, Base, session
from models import User, UserProfile


def list_users():
    # SELECT * FROM tb_users
    return session.query(User).all()


def create_user(email, password):
    # Instanciamos a model que queremos salvar
    user = User(email=email, password=password)

    # Adicionar esse objeto à sessão
    session.add(user)

    # Salvando o objeto na tabela
    session.commit()

    return user


def create_profile(user, first_name, last_name):

    profile = UserProfile(
        id=user.id, first_name=first_name, last_name=last_name
    )

    session.add(profile)

    session.commit()

    return profile


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

            else:
                for user in users:
                    # O método get() retorna um registro de acordo com a chave primária
                    # Ou seja: SELECT * FROM tb_users_profiles WHERE id = ?
                    # profile = session.query(UserProfile).get(user.id)

                    print(f"{user.profile.first_name} {user.profile.last_name} ({user.email})")
                print("-"*50)

        elif option == 2:
            email = input("Informe o email do novo usuário: ")
            password = input("Informe a senha do novo usuário: ")
            first_name = input("Informe o seu nome: ")
            last_name = input("Informe o seu sobrenome: ")

            user = create_user(email, password)
            profile = create_profile(user, first_name, last_name)

            print(f"Usuário {profile.first_name} ({user.email}) salvo com sucesso.")

        elif option == 3:
            pass

        elif option == 4:
            pass

        elif option == 5:
            print("Saindo...")
            break

        else:
            print(f"OPÇÃO DESCONHECIDA: {option}.")
