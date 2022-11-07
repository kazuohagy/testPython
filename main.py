from produto import Produto

# Instanciando o produto
p1 = Produto('Mario', 100)
print('NOME DO PRODUTO: ' + p1.nome + ' PRECO: ' + str(p1.preco))
# Criando o produto no banco de dados
p1.criarProduto()
# Atualizando o produto com desconto
print(p1.desconto(10))
p1.atualizarProduto(p1.desconto(10))
# Encontrando o produto
print('Encontrando o produto criado')
p1.encontrarProduto()
# Deletando o produto
p1.deletarProduto()
# Encontrando todos os produtos
print('Encontrando todos os produtos')
p1.encontrarTodosProdutos()
