import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../src')

from Cliente import Cliente # type: ignore

cliente = Cliente('Jordana', 20, 1200)
cliente.mostrar_informacoes()
cliente.atualizar_saldo(500)  
cliente.mostrar_informacoes()