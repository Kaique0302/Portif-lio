"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    print("Função 1 rodando")
    
    return budget / exchange_rate
    
    """ A Função exchange_money está retornando uma estimativa de valor
    """

    # This is the docstring the resposible function

    


def get_change(budget, exchanging_value):



    return  budget - exchanging_value
    """
    
    calculo de subtração
    """

   


def get_value_of_bills(denomination, number_of_bills):
    
    """

        Calculo de valor de notas no return

    """

    return denomination * number_of_bills
  
    


def get_number_of_bills(amount, denomination):

    """
        Função para numero de notas
    """
    
    return amount // denomination


    
   

    


def get_leftover_of_bills(amount, denomination):


    return amount % denomination

    
    """
        funcção de restantes

    """

    pass


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
        função de calculo após troca
    """
    spread_decimal = spread / 100
    taxa_com_spread = exchange_rate + (exchange_rate * spread_decimal ) 
    valor = budget / taxa_com_spread
    
    return int (valor - (valor % denomination))
  

    
