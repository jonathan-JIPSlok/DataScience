from pymongo import MongoClient
import pymongo

Connection = MongoClient("localhost", 27017)
#Faz a conexao com o banco de dados

db = Connection.Dados
#Cria um banco de dados com o nome passado no final

Collection = db.Dados
#Colletion e um grupo de documentos armazenados no MongoDB

"""
    Dados no MongoDb são representados (e armazenados) usando documentos Json.
    Com o pyMongo usamos dicionarios para representar documentos.
"""

post1 = {"ID" :18378283,
                "Nome_Produto":"Geladeira",
                "Marcas": ["Brastemp", "Consul", "Eletrolux"],
                "Data_Cadastro":2021}
                
collection = db.posts
#post_id = collection.insert_one(post1)
#Insere dados no banco

#post_id.inserted_id
#id da colecao

#find retorna um cursor
for post in collection.find():
    print(post)

print()
print(db.name) #mostra o nome do banco

print()
print(db.list_collection_names()) #lista as conexoes disponiveis

#_______ RETORNANDO DADOS NO MONGODB_______#

client_con = pymongo.MongoClient()
#Se nao passar nada como parametro, ele usa a conexao disponivel

client_con.list_database_names()
#Lista de banco de dados disponiveis

db = client_con.Dados #Dados é o nome do nosso banco de dados
#Objeto para navegar no banco de dados

#db.create_collection("MyCollection")
#cria uma nova coleção

#db.MyCollection.insert_one({"Nome":"Jonathan"})
#Inserindo dados na nova coleção

db.MyCollection.find_one()
#Retorna o documento criado

col = db["MyCollection"]
#Conecta a uma coleção

print()
col.estimated_document_count()
print("Total de documentos ", col.estimated_document_count())
#Conta os documentos em uma coleção

print()
doc = col.find_one()
print("Documento ",doc)
#retorna o documento