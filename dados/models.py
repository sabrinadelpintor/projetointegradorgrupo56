from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id_cliente = Column(String, primary_key=True) # Baseado no 'Customer ID'
    nome = Column(String)
    segmento = Column(String)

class Produto(Base):
    __tablename__ = 'produtos'
    id_produto = Column(String, primary_key=True) # Baseado no 'Product ID'
    nome = Column(String)
    categoria = Column(String)
    sub_categoria = Column(String)

class Venda(Base):
    __tablename__ = 'vendas'
    id_venda = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String)
    data_pedido = Column(Date)
    valor_venda = Column(Float)
    quantidade = Column(Integer)
    # Relacionamentos
    id_cliente = Column(String, ForeignKey('clientes.id_cliente'))
    id_produto = Column(String, ForeignKey('produtos.id_produto'))
  
