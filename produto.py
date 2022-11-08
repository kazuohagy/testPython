import pymongo
cluster = pymongo.MongoClient(
    "mongodb+srv://root:280700@cluster0.vyupbdb.mongodb.net/test?retryWrites=true&w=majority")

db = cluster.get_database("python")

collection = db.get_collection("test")


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco - (self.preco * (percentual / 100))

    def criarProduto(self):
        dado = {
            'nome': self.nome,
            'preco': self.preco
        }
        collection.insert_one(dado)

    def deletarProduto(self):
        collection.delete_one({'nome': self.nome})

    def atualizarProduto(self, preco):
        collection.update_one({'nome': self.nome}, {
                              '$set': {'preco': preco}})

    def encontrarProduto(self):
        resultado1 = collection.find_one({'nome': self.nome})
        if resultado1:
            print(resultado1)
        else:
            print('nao encontrado')

    def encontrarTodosProdutos(self):
        resultado = collection.find({})
        for i in resultado:
            print(i)

    def __str__(self):
        return f'Produto: {self.nome} Preço: {self.preco}'
