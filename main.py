import requests
import flet as ft
import requests
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.types import FontWeight, MainAxisAlignment, CrossAxisAlignment


def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # listar
    def listar_usuario_get():
        url = f'http://10.135.232.21:5000/listar_usuario'
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            print(f'usuario: \n{dados["usuario"]}\n')
            return dados
        else:
            print(f'erro :{response.status_code}')
            print(response.json())
            #no parentece de exeplo eu posso escolhar o numero que eu quero
    #listar_usuario_get()

    def cadastra_usuario(e):
        progress.visible = True
        page.update()

        if nome.value == "" or cpf.value or endereco.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados = listar_usuario_get()
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                nome.value = dados["Nome"]
                cpf.value = dados["Cpf"]
                endereco.value = dados["Endereço"]
                page.go("/usuario")

                nome.value = ""
                cpf.value = ""
                endereco.value = ""
                msg_sucesso.content = ft.Text("Nome Valido")
                msg_sucesso.content = ft.Text("Cpf Valido")
                msg_sucesso.content = ft.Text("Endereço Valido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()

    def listar_livro_get():
        url = f'http://10.135.232.21:5000/listar_livro'
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            print(f'dados do livro:\n {dados["livro"]}\n')
            return dados
        else:
            print(f'erro :{response.status_code}')
            print(response.json())
            #no parentece de exeplo eu posso escolhar o numero que eu quero
    #listar_livro_get(1)

    def lista_livro():
        progress.visible = True
        page.update()

        if titulo_livro.value == "" or nome_autor.value or isbn.value or resumo.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados = listar_livro_get()
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                titulo_livro.value = dados["Titulo do livro"]
                nome_autor.value = dados["Nome do autor"]
                isbn.value = dados["Isbn"]
                resumo.value = dados["Resumo"]
                page.go("/livro")

                titulo_livro.value = ""
                nome_autor.value = ""
                isbn.value = ""
                resumo.value = ""
                msg_sucesso.content = ft.Text("Titulo do livro   Valido")
                msg_sucesso.content = ft.Text("Nome do autor  Valido")
                msg_sucesso.content = ft.Text("Isbn Valido")
                msg_sucesso.content = ft.Text("Resumo Valido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()

    def listar_emprestimo_get(id):
        url = f'http://10.135.232.21:5000/emprestimo'
        response = requests.get(url)

        if response.status_code == 200:
            dados_get_postagem = response.json()
            print(f'Emprestimo: \n{dados_get_postagem["emprestimo"]}\n')
            return dados_get_postagem
        else:
            print(f'erro :{response.status_code}')
            print(response.json())
            #no parentece de exeplo eu posso escolhar o numero que eu quero
    #listar_emprestimo_get(1)

    def lista_emprestimo():
        progress.visible = True
        page.update()

        if data_prevista.value == "" or data_devolucao.value or id_livro.value or id_usuario.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados = listar_emprestimo_get(id)
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                data_prevista.value = dados["Data de prevista"]
                data_devolucao.value = dados["Data de devolucao"]
                id_livro.value = dados["Id do livro"]
                id_usuario.value = dados["Id do usuario"]
                page.go("/emprestimo")

                data_prevista.value = ""
                data_devolucao.value = ""
                id_livro.value = ""
                id_usuario.value = ""
                msg_sucesso.content = ft.Text("Data prevista Valido")
                msg_sucesso.content = ft.Text("Data de devolução Valido")
                msg_sucesso.content = ft.Text("Id do livro Valido")
                msg_sucesso.content = ft.Text("Id do usuarioValido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()
    #  cadastra

    def  cadastrar_usuario_post(e):
        url =f'http://10.135.232.21:5000/usuario/cadastrar'
    #pode usar do 1 ao 100
        nova  = {
            'nome': nome.value,
            'cpf': cpf.value,
            'endereco': endereco.value,
        }
        response = requests.post(url, json=nova)
        if response.status_code == 201:
            dados_post = response.json()
            print(f'usuario: {dados_post["mensagem"]}\n')
            return dados_post

        else:
            print(f'erro :{response.status_code}')
            print(response.json())
            # no parentece de exeplo eu posso escolhar o numero que eu quero
    #cadastrar_usuario_post()

    def usuario_cadastra(e):
        progress.visible = True
        page.update()

        if nome.value == "" or cpf.value or endereco.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados =  cadastrar_usuario_post(e)
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                nome.value = dados["Nome"]
                cpf.value = dados["Cpf"]
                endereco.value = dados["Endereço"]
                page.go("/usuario")

                nome.value = ""
                cpf.value = ""
                endereco.value = ""
                msg_sucesso.content = ft.Text("Nome Valido")
                msg_sucesso.content = ft.Text("Cpf Valido")
                msg_sucesso.content = ft.Text("Endereço Valido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()

    def cadastrar_livro_post(e):
        url = f'http://10.135.232.21:5000/cadastrar/livro'
        # pode usar do 1 ao 100
        postagem = {
            'titulo_livro': titulo_livro.value,
            'nome_autor': nome_autor.value,
            'isbn': isbn.value,
            'resumo': resumo.value,
        }
        response = requests.post(url, json=postagem)

        if response.status_code == 201:
            dados_post = response.json()
            print(f'livro: \n {dados_post["mensagem"]}\n')
            return dados_post

        else:
            print(f'erro :{response.status_code}')
            print(response.json())

    def cadastrado_livro(e):
        progress.visible = True
        page.update()

        if titulo_livro.value == "" or nome_autor.value or isbn.value or resumo.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados = cadastrar_livro_post(e)
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                titulo_livro.value = dados["Titulo do livro"]
                nome_autor.value = dados["Nome do autor"]
                isbn.value = dados["Isbn"]
                resumo.value = dados["Resumo"]
                page.go("/livro")

                titulo_livro.value = ""
                nome_autor.value = ""
                isbn.value = ""
                resumo.value = ""
                msg_sucesso.content = ft.Text("Titulo do livro   Valido")
                msg_sucesso.content = ft.Text("Nome do autor  Valido")
                msg_sucesso.content = ft.Text("Isbn Valido")
                msg_sucesso.content = ft.Text("Resumo Valido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()
    #cadastrar_livro_post()

    def cadastrar_emprestimo_post(e):
        url ='http://10.135.232.21:5000/emprestimo/cadastrar'
        print('teste')
    #pode usar do 1 ao 100
        nova_postagem  = {
            'data_emprestimo': data_prevista.value,
            'data_devolucao': data_devolucao.value,
            'id_livro': id_livro.value,
            'id_usuario': id_usuario.value
        }

        response = requests.post(url, json=nova_postagem)
        if response.status_code == 201:
            dados_post = response.json()
            print(f'emprestimo: {dados_post["mensagem"]}\n')
            return dados_post

        else:
            print(f'erro :{response.status_code}')
            print(response.json())
    #cadastrar_emprestimo_post()

    def emprestimo_cadastrar(e):
        progress.visible = True
        page.update()

        if data_prevista.value == "" or data_devolucao.value or id_livro.value or id_usuario.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados = cadastrar_emprestimo_post(e)
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                data_prevista.value = dados["Data de prevista"]
                data_devolucao.value = dados["Data de devolucao"]
                id_livro.value = dados["Id do livro"]
                id_usuario.value = dados["Id do usuario"]
                page.go("/emprestimo")

                data_prevista.value = ""
                data_devolucao.value = ""
                id_livro.value = ""
                id_usuario.value = ""
                msg_sucesso.content = ft.Text("Data prevista Valido")
                msg_sucesso.content = ft.Text("Data de devolução Valido")
                msg_sucesso.content = ft.Text("Id do livro Valido")
                msg_sucesso.content = ft.Text("Id do usuarioValido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()

    def atualizar_usuario_put(id):
        url=f'http://10.135.232.21:5000/usuario/atualizar/{id}'

        nova_postagem = {
            'id': id,
            'nome': 'nome',
            'cpf': '100',
            'endereco': 'endereco'
        }
        response = requests.put(url, json=nova_postagem)

        if response.status_code == 200:
            dados = response.json()
            print(f'usuario: {dados["mensagem"]}\n')
            return dados
        else:
            print(f'erro :{response.status_code}')

    def atualiza_usuario(e):
        progress.visible = True
        page.update()

        if nome.value == "" or cpf.value or endereco.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados = atualizar_usuario_put(id)
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                nome.value = dados["Nome"]
                cpf.value = dados["Cpf"]
                endereco.value = dados["Endereço"]
                page.go("/usuario")

                nome.value = ""
                cpf.value = ""
                endereco.value = ""
                msg_sucesso.content = ft.Text("Nome Valido")
                msg_sucesso.content = ft.Text("Cpf Valido")
                msg_sucesso.content = ft.Text("Endereço Valido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()
    #atualizar_usuario_put(1)

    def atualizar_livro_put(id):
        url=f'http://10.135.232.21:5000/livro/atualizar/{id}'

        nova_postagem = {
            'id': id,
            'titulo_livro': 'iss',
            'nome_autor': 'ieu',
            'isbn': '34',
            'resumo': 'Resumo ',
        }
        response = requests.put(url, json=nova_postagem)

        if response.status_code == 200:
                dados = response.json()
                print(f'livro: {dados["mensagem"]}\n')
                return dados
        else:
            print(f'erro :{response.status_code}')
    #atualizar_livro_put(1)

    def atualizar_livro(e):
        progress.visible = True
        page.update()

        if  id or titulo_livro.value == "" or nome_autor.value or isbn.value or resumo.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados = atualizar_livro_put(id)
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                titulo_livro.value = dados["Titulo do livro"]
                nome_autor.value = dados["Nome do autor"]
                isbn.value = dados["Isbn"]
                resumo.value = dados["Resumo"]
                page.go("/livro")

                titulo_livro.value = ""
                nome_autor.value = ""
                isbn.value = ""
                resumo.value = ""
                msg_sucesso.content = ft.Text("Titulo do livro   Valido")
                msg_sucesso.content = ft.Text("Nome do autor  Valido")
                msg_sucesso.content = ft.Text("Isbn Valido")
                msg_sucesso.content = ft.Text("Resumo Valido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()

    def atualizar_emprestimo_put(id):
        url=f'http://10.135.232.21:5000/emprestimo/atualizar/{id}'

        nova_postagem = {
            'id': id,
            'data_emprestimo': 'data_emprestimo',
            'data_devolucao': 'data_devolucao',
            'id_livro': 'id_livro',
            'id_usuario': 'id_usuario',
        }
        response = requests.put(url, json=nova_postagem)

        if response.status_code == 200:
                dados = response.json()
                print(f'emprestimo: {dados["mensagem"]}\n')
                return dados
        else:
            print(f'erro :{response.status_code}')

    def atualiza_emprestimo(e):
        progress.visible = True
        page.update()

        if data_prevista.value == "" or data_devolucao.value or id_livro.value or id_usuario.value:
            msg_error.content = ft.Text("")
            page.overlay.append(msg_error)
            msg_error.open = True
        else:
            # chamar a função para pegar o JSON
            dados = atualizar_livro_put(id)
            progress.visible = False
            page.update()

            # Verificar se a API retornou erro
            if "erro" in dados:
                page.overlay.append(msg_error)
                msg_error.open = True
            else:
                data_prevista.value = dados["Data de prevista"]
                data_devolucao.value = dados["Data de devolucao"]
                id_livro.value = dados["Id do livro"]
                id_usuario.value = dados["Id do usuario"]
                page.go("/emprestimo")

                data_prevista.value = ""
                data_devolucao.value = ""
                id_livro.value = ""
                id_usuario.value = ""
                msg_sucesso.content = ft.Text("Data prevista Valido")
                msg_sucesso.content = ft.Text("Data de devolução Valido")
                msg_sucesso.content = ft.Text("Id do livro Valido")
                msg_sucesso.content = ft.Text("Id do usuarioValido")
                page.overlay.append(msg_sucesso)
                msg_sucesso.open = True

        page.update()

    #atualizar_emprestimo_put(1)
    # def gerencia_rotas(e):
    #     page.views.clear()
    #     if page.route == "/usuario":
    #         page.views.append(e)
    #     elif page.route == "/livro":
    #         page.views.append(e)
    #     elif page.route == "/devolucao":
    #         page.views.append(e)
    #     page.update()


    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Biblioteca"), bgcolor="#f4976e"),

                    # exemplo 2 (cancelar sempre na esquerda)
                    ft.Container(
                        ft.Image(src="Design sem nome.png", width=450, height=350), ),
                    ft.ElevatedButton("Cadastrar Livro", on_click=lambda _: page.go("/livro"), bgcolor="#f4976e",
                                      color=Colors.WHITE),

                    ft.ElevatedButton("Cadastrar Usuario", on_click=lambda _: page.go("/usuario"), bgcolor="#f4976e",
                                      color=Colors.WHITE),

                    ft.ElevatedButton("Cadastrar Emprestimo", on_click=lambda _: page.go("/emprestimo"), bgcolor="#f4976e",
                                      color=Colors.WHITE),
                ],
                bgcolor='#61aeb0',
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            )
        )
        if page.route == "/usuario":
            page.views.append(
                View(
                    "/usuario",
                    [
                        AppBar(title=Text("usuario"), bgcolor=Colors.SECONDARY_CONTAINER),
                        nome,
                        cpf,
                        endereco,
                        # Botão da direita
                        ft.FilledButton(
                            text="Concluido",
                            on_click=lambda _: cadastrar_usuario_post(e),
                            col=6
                        ),
                    ],
                )
            )

        page.update()
        if page.route == "/livro":
            page.views.append(
                View(
                    "/livro",
                    [
                        AppBar(title=Text("livro"), bgcolor=Colors.SECONDARY_CONTAINER),
                        titulo_livro,
                        nome_autor,
                        isbn,
                        resumo,
                        # Botão da direita
                        ft.FilledButton(
                            text="Concluido",
                            on_click=lambda _: cadastrar_livro_post(e),
                            col=6
                        ),
                    ],
                )
            )

        page.update()
        if page.route == "/emprestimo":
            page.views.append(
                View(
                    "/emprestimo",
                    [
                        AppBar(title=Text("emprestimo"), bgcolor=Colors.SECONDARY_CONTAINER),
                        data_prevista,
                        data_devolucao,
                        id_livro,
                        id_usuario,
                        ft.FilledButton(
                            text="Concluido",
                            on_click=lambda _: cadastrar_emprestimo_post(e),
                            col=6
                        ),
                    ],
                )
            )

        page.update()
        if page.route == "/Pagina":
            page.views.append(
                View(
                    "/Pagina",
                    [
                        AppBar(title=Text("Resposta"), bgcolor=Colors.BLACK),
                        Text(value=f'Nome "{nome.value}"'),
                        Text(value=f'Endereço "{endereco.value}"'),
                        Text(value=f'Cpf"{cpf.value}"'),
                        Text(value=f'Nome do autor "{nome_autor.value}"'),
                        Text(value=f'Titulo do Livro "{titulo_livro.value}"'),
                        Text(value=f'Isbn "{isbn.value}"'),
                        Text(value=f'Resumo "{resumo.value}"'),
                        Text(value=f'Data prevista "{data_prevista.value}"'),
                        Text(value=f'Data devolução "{data_devolucao.value}"'),
                        Text(value=f'Id usuario "{id_usuario.value}"'),
                        Text(value=f'Id livro "{id_livro.value}"'),
                        txt_resultado,
                    ],
                    bgcolor='#44803F',
                )
            )

    def voltar(e):
        print("Views", page.views)
        removida = page.views.pop()
        print(removida)
        top_view = page.views[-1]
        print(top_view)
        page.go(top_view.route)



    # Componentes

    progress = ft.ProgressRing(visible=False)
    txt_resultado = ft.Text()
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Concluido com Sucesso"),
        bgcolor=Colors.GREEN
    )
    msg_error = ft.SnackBar(
        content=ft.Text("Não foi Concluido"),
        bgcolor=Colors.RED
    )

    nome = ft.TextField(
        label="Nome",
        hint_text="Ex: Fran"
    )
    cpf = ft.TextField(
        label="CPF",
        hint_text="Ex: 1427586523"
    )
    endereco = ft.TextField(
        label="Endereço",
        hint_text="Ex: Rua tal de asis"
    )

    # L       I       V        R         O
    titulo_livro = ft.TextField(
        label="Titulo",
        hint_text="Ex: esse..."
    )
    nome_autor = ft.TextField(
        label="Nome do autor",
        hint_text="Ex: geoger."
    )
    isbn = ft.TextField(
        label="Isbn",
        hint_text="Ex:123.."
    )
    resumo = ft.TextField(
        label="Resumo",
        hint_text="Ex: entre isso.."
    )
    #  E       M    P    R     E    S    T    I     M   O
    data_prevista = ft.TextField(
        label="Data Prevista",
        hint_text="Ex: 16/12/2007"
    )
    data_devolucao = ft.TextField(
        label="Data Devolução",
        hint_text="Ex: 14/12/2007"
    )
    id_livro = ft.TextField(
        label="Id Livro",
        hint_text="Ex:123.."
    )
    id_usuario = ft.TextField(
        label="Id Usuario",
        hint_text="Ex: 325.."
    )

    # U        S          U             A         R       I             O
    nome = ft.TextField(label='Nome', focused_border_color=Colors.BLACK)
    cpf = ft.TextField(label='CPF', focused_border_color=Colors.BLACK)
    endereco = ft.TextField(label='Endereço', focused_border_color=Colors.BLACK)

     # L      I        V       R         O
    titulo_livro = ft.TextField(label='Titulo do Livro', focused_border_color=Colors.BLACK)
    nome_autor = ft.TextField(label='Nome do Autor', focused_border_color=Colors.BLACK)
    isbn = ft.TextField(label='ISBN', focused_border_color=Colors.BLACK)
    resumo = ft.TextField(label='Resumo', focused_border_color=Colors.BLACK)

    #  E       M    P    R     E    S    T    I     M   O
    data_prevista = ft.TextField(label='Data Prevista', focused_border_color=Colors.BLACK)
    data_devolucao = ft.TextField(label='Data Devolução', focused_border_color=Colors.BLACK)
    id_livro = ft.TextField(label='Id Livro', focused_border_color=Colors.BLACK)
    id_usuario = ft.TextField(label='Id Usuario', focused_border_color=Colors.BLACK)


#Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)
