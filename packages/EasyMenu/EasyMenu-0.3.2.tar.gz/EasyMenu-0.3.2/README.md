# EasyMenu.py

Uma biblioteca feita para facilitar o desenvolvimento de menu interativo no Python 3.6.x  
*Visite [EasyMenu Documentation](https://nvrsantos.github.io/easymenu.py/) para uma documentação completa!*

## Como Instalar

Usando o gerenciador de pacotes [pip](https://pypi.org/) para instalar o *EasyMenu*.

```bash
pip install EasyMenu
```

## Como Usar

```python
from EasyMenu import menu, menu_nocolor

option = {
    "Sim": "print('Hello, World!')",
    "Não": "exit()"
}

menu = menu_nocolor.Menu(option=option, question='Deseja continuar ?', qchoice='Escolha uma opção: ')
eval(menu.display())

```

## Menu Final

> Menu Com Cor

![](https://i.imgur.com/sQFMTv9.png)

> Menu Sem Cor

![](https://i.imgur.com/vRV2lnJ.png)

## Contribuição
Solicitações de contribuições são bem-vindas. Sempre mantendo a beleza do código e a facilidade de usar.\
Para grandes mudanças, abra um problema primeiro para discutir o que você gostaria de mudar.

## License
[MIT](https://github.com/nvrsantos/easymenu.py/blob/master/LICENSE)
