import requests
from bs4 import BeautifulSoup

class BitcoinCash():
  def __init__(self):
    """
    Incia o objeto conversor.
    """
    req = requests.get('https://dolarhoje.com/bitcoin-cash-hoje/')
    soup = BeautifulSoup(req.text, 'html.parser')
    i = soup.find_all('input', id="nacional")[0]
    self._quotation_str = i.get('value')
  

  def get_cotacao(self):
    """
    Retorna a cotação atual do bitcoin cash em https://dolarhoje.com/bitcoin-cash-hoje/ .
    Exemplo: 4.33
    """
    value = self._quotation_str.replace(',', '.')
    value = float(value)
    return value
  
  def get_cotacao_str(self):
    """"
    Retorna a cotação atual do bitcoin cash em String e adiciona formatação.
    Exemplo: R$514,48
    """
    str_value = 'R$' + self._quotation_str
    return str_value

  def converter(self, value: float):
    """
    Converte :value: de bitcoin cash para real.
    ₿C -> R$
    """
    result = value * self.get_cotacao()
    result = '{0:.2f}'.format(result)
    result = float(result)
    return result
  
  def converter_str(self, value:float):
    """
    Converte :value: de bitcoin cas para real em String e adiciona formatação.
    ₿C -> R$
    """
    value = self.converter(value)
    value = str(value)
    value = value.replace('.', ',')
    v = value.split(',')

    if len(v[1]) != 2:
      value = value + '0'
    value = 'R$' + value
    return value