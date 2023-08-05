from colorama import Style


# Classe Base dos Errors
class __Error(Exception):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return repr(self.string)


# Classe de erros Inputs
class __InputError(__Error):
    pass


# Classe do Menu
class Menu:
    """
        Atributos
        ----------
        option : dict
            Dicionario com as opções e os comandos
        question : str
            Pergunta para o topo do menu
        response : str
            Pergunta para o final do menu
    """
    def __init__(self, option, question, qchoice):
        self.option = option  # Parametro das opções
        self.question = question  # Parametro das opções
        self.response = qchoice  # Parametro da pergunta da escolha

        self.reset = Style.RESET_ALL  # Resetar os atributos
        self.bold = Style.BRIGHT  # Setaar os atributos como BOLD

    def __start(self):
        # Verifica se o parametro das opções tem a opção de Sair
        if 'Sair' in self.option:
            # Se tiver a opção remove, ela (será adicionado novamente)
            self.option.pop('Sair')
        elif 'sair' in self.option:
            self.option.pop('sair')

        while True:
            # Printa o cabeçalho do Menu
            print(f'{self.bold}-' * 37)
            print(f'{self.question.center(37)}')
            print('-' * 37)

            toption = len(self.option)  # Size do option
            numero = 0  # Variavel para contagem dos números de atributos

            for opcao in self.option:
                numero += 1
                print(f'{self.reset} [ {numero} ] - {opcao}')  # Printa a opção

            print(f' [ {toption + 1} ]{self.reset} - Sair{self.reset}')  # Sair
            print(f'{self.bold}-' * 37)  # Separador com estilização BOLD

            resposta = input(f'{self.reset} {self.response}')  # input opção
            resposta = int(resposta)
            print('\n')  # Pula linha

            # Verifica se o usuario escolheu uma opção valida
            if resposta > toption + 1 or resposta < 1:
                print(f'Error: Escolha um número válido...')  # Print erro
            else:
                contagem = 0  # Contagem para Verificar a opção escolhida

                for opcao in self.option:
                    contagem += 1
                    if resposta == contagem:

                        try:  # Tenta executar o código do usuario
                            # Executa comando do usuário
                            eval(self.option[opcao])

                        # Se o código do usuario for uma def customizada
                        except NameError:
                            # Retorna o código para a def display
                            return(self.option[opcao])

                    elif resposta == toption + 1:  # Escolheu Sair
                        print(f'{self.bold} Até mais...{self.reset}\n')
                        exit()

    # Verificar erros
    def display(self):
        """
            Mostra o menu para o usuario
        """
        if(type(self.option) != dict):  # Verifica se o atributo é um dict
            raise __InputError('O atributo OPTION deve ser do tipo <dict>')

        elif(type(self.question) != str):  # Verifica se o atributo é uma str
            raise __InputError('O atributo QUESTION deve ser do tipo <str>')

        elif(type(self.response) != str):  # Verifica se o atributo é uma str
            raise __InputError('O atributo QCHOICE deve ser do tipo <str>')

        else:  # Iniciar o código
            return(self.__start())
