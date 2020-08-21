class CountOneBinary:

    def __init__(self, decimal:int, binary:int = '1'):
        self.decimal = decimal
        self.binary = binary


    def main(self, decimal, binary):
        return count_one_binary(decimal, binary)


    def decimal_to_binary(self, decimal:int) -> str:
        '''
        Função que retorna um número binario a partir de um decimal
        :param decimal: Número inteiro positivo
        :return: Número binário em formato de string
        '''

        self.decimal = decimal

        if decimal >= 0:
            binary = bin(decimal)
            return binary
        else:
            print('O decimal precisa ser positivo')


    def count_one_binary(self, decimal:int, binary:str = '1') -> int:
        '''
        Função que retorna a contagem de números '1' em um número binário
        :param binary: Recebe uma string (str) de um binario
        :return: Retorna um inteiro com a contagem de números '1'
        '''

        self.decimal = decimal
        self.binary = binary

        return decimal_to_binary(decimal).count(binary)