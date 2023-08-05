import requests
from bs4 import BeautifulSoup

class Neo():
  def __init__(self):
    """
    Incia o objeto conversor.
    """
    req = requests.get('https://criptoeconomia.com.br/cotacoes/neo-neo/')
    soup = BeautifulSoup(req.text, 'html.parser')
    i = soup.find_all('span', class_="number")[0]
    i = float(i.text.replace('R$ ', '').replace(',', '.'))
    i = '{0:.2f}'.format(i)
    i = str(i).replace('.', ',')
    self._quotation_str = i
  

  def get_cotacao(self):
    """
    Retorna a cotação atual do neo em https://criptoeconomia.com.br/cotacoes/neo-neo/ .
    Exemplo: 4.33
    """
    value = self._quotation_str.replace(',', '.')
    value = float(value)
    return value
  
  def get_cotacao_str(self):
    """"
    Retorna a cotação atual do neo em String e adiciona formatação.
    Exemplo: R$514,48
    """
    str_value = 'R$' + self._quotation_str
    return str_value

  def converter(self, value: float):
    """
    Converte :value: de neo para real.
    NEO -> R$
    """
    result = value * self.get_cotacao()
    result = '{0:.2f}'.format(result)
    result = float(result)
    return result
  
  def converter_str(self, value:float):
    """
    Converte :value: de neo para real em String e adiciona formatação.
    NEO -> R$
    """
    value = self.converter(value)
    value = str(value)
    value = value.replace('.', ',')
    v = value.split(',')

    if len(v[1]) != 2:
      value = value + '0'
    value = 'R$' + value
    return value