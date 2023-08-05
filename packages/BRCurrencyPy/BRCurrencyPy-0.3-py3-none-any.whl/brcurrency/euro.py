import requests
from bs4 import BeautifulSoup

class Euro():
  def __init__(self):
    """
    Incia objeto conversor
    """
    req = requests.get('https://dolarhoje.com/euro-hoje/')
    soup = BeautifulSoup(req.text, 'html.parser')
    i = soup.find_all('input', id="nacional")[0]
    self._quotation_str = i.get('value')

  def get_cotacao(self):
    """"
    Retorna a cotação atual do euro em https://dolarhoje.com/euro-hoje/.
    Exemplo: 4.52
    """
    value = self._quotation_str.replace(',', '.')
    value = float(value)
    return value
  
  def get_cotacao_str(self):
    """"
    Retorna a cotação atual do euro em String e adiciona formatação.
    Exemplo: R$4,52
    """
    str_value = 'R$' + self._quotation_str
    return str_value

  def converter(self, value: float):
    """
    Converte :value: de euro para real.
    € -> R$
    """
    result = value * self.get_cotacao()
    result = '{0:.2f}'.format(result)
    result = float(result)
    return result
  
  def converter_str(self, value:float):
    """
    Converte :value: de euro para real em String e adiciona formatação.
    € -> R$
    """
    value = self.converter(value)
    value = str(value)
    value = value.replace('.', ',')
    v = value.split(',')

    # Verifica se termina com 0
    # Exemplo: se o value for R$45,5 , ele vai substituir para R$45,50.
    if len(v[1]) != 2:
      value = value + '0'
    value = 'R$' + value
    return value
