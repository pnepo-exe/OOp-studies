from abc import ABC, abstractmethod

class ContaAbstrata(ABC):
   def __init__(self,numero:str)->None:
      self.__numero = numero
      self.__saldo = 0.0
   
   def creditar(self, valor:float)->None:
      self.__sald += valor
   
   @abstractmethod
   def debitar(self, valor:float) -> None:
      pass

   def get_numero(self) -> str:
       return self.__numero

   def get_saldo(self) -> float:
      return self.__saldo
      
   

class Conta(ContaAbstrata) :
   def __init__(self, numero):
      super().__init__(numero)
 
   def debitar(self, valor:float) -> None:
      self.__saldo -= valor
   
   

class ContaPoupança(Conta):
   def __init__(self, numero):
      super().__init__(numero)
   def render_juros(self, taxa:float) -> None:
      self.creditar(self.get_saldo * taxa)

class ContaEspecial(Conta):
   def __init__(self, numero):
      super().__init__(numero)
      self._bonus = 0
   def render_bonus(self):
      self.creditar(self._bonus)
      self._bonus = 0 

   def creditar(self, valor):
      self._bonus += valor * 0.01
      super().creditar(valor)

class ContaImposto(ContaAbstrata):
   def __init__(self, numero:str):
      super().__init__(numero)
      self.__taxa = 0.001
   
   def debitar(self, valor) -> None:
      self.__saldo = self.__saldo - (valor + (valor * self.__taxa))
   
   def get_taxa(self) -> float:
      return self.__taxa

   def set_taxa(self, new_taxa: float) -> None:
      self.__taxa = new_taxa
   

class Banco:
   def __init__(self,taxa_poupança: float, taxa_imposto:float):
      self.__taxa_poupança = taxa_poupança
      self.__taxa_imposto = taxa_imposto
      self.__contas = []

   def cadastrar(self, conta: Conta) -> None:
      self.__contas.append(conta)
      
   def procurar(self, numero:str) -> Conta:
      for conta in self.__contas:
         if conta.get_numero() == numero:
            return conta
      return None
   
   def creditar(self, numero:str, valor:float) -> None:
      conta = self.procurar(numero)
      if conta is not None:
         conta.creditar(valor)

   def debitar(self, numero:str, valor:float) -> None:
      conta = self.procurar(numero)
      if conta is not None:
         conta.debitar(valor)

   def saldo(self, numero:str) -> float:
      conta = self.procurar(numero)
      if conta is not None:
         return conta.get_saldo()
   
   def transferir(self, origem:str, destino:str, valor:float) -> None:
      conta1 = self.procurar(origem)
      conta2 = self.procurar(destino)
      conta1.debitar(valor)
      conta2.creditar(valor)

   def render_juros(self, num_conta:str) -> None:
      conta = self.procurar(num_conta)
      if isinstance(conta,ContaPoupança):
         conta.render_juros(self.__taxa)
      else:
         print("Apenas contas Poupanças podem render juros")

   def get_taxa_poupança(self) -> float:
      return self.__taxa_poupança
   
   def set_taxa_poupança(self, taxa=float) -> None:
      self.__taxa_poupança = taxa
   
   def get_taxa_imposto(self) -> float:
      return self.__taxa_imposto
   
   def set_taxa_imposto(self, taxa=float) -> None:
      self.__taxa_imposto = taxa

   def render_bonus(self, numero:str):
      conta = self.procurar(numero)
      if isinstance(conta, ContaEspecial):
         conta.render_bonus()
      else:
         print("Apenas contas Especiais podem render bonus")
