import random

from datetime import date, timedelta

nomes = [

"Rodrigo","Marcos","Lucas","Gabriel","Gustavo","Felipe","Rafael","Bruno","Thiago","Vinicius",
"Ana","Beatriz","Camila","Carla","Daniela","Fernanda","Gabriela","Juliana","Larissa","Leticia",
"Eduardo","Daniel","Matheus","Pedro","Caio","Vitor","Andre","Leandro","Diego","Renan",
"Mariana","Patricia","Renata","Sofia","Tatiana","Vanessa","Amanda","Bianca","Carolina","Claudia",
"Joao","Carlos","Fernando","Ricardo","Alexandre","Marcelo","Paulo","Fabio","Roberto","Sergio",
"Cristina","Eliana","Fabiana","Isabela","Jessica","Julia","Laura","Lara","Karoline","Paula",
"William","Antonio","Jorge","Luis","Mario","Ronaldo","Cesar","Samuel","Guilherme","Murilo",
"Regina","Simone","Sabrina","Tatiane","Viviane","Yasmin","Adriana","Aline","Bruna","Camila",
"Leonardo","Davi","Henrique","David","Igor","Victor","Teo","Valter","Breno","Claudio",
"Maria","Marlene","Luzia","Emilia","Janaina","Cristiane","Lorena","Michele","Helena","Raquel"

]

sobrenomes = [

"Mendes","Silva","Souza","Costa","Oliveira","Pereira","Lima","Gomes","Ribeiro","Almeida","Zanetti",
"Mendes Caetano","Souza Lima","Souza Neto","Neves Oliveira","Silva Costa","Pereira Rocha","Gomes Martins",
"da Silva","dos Santos","de Oliveira","da Costa","do Nascimento","da Rocha","de Souza","da Lima","dos Reis",
"Mendes Caetano Silva","Souza Lima Nunes","Neves Oliveira Pacheco","Silva Costa Mendes","Pereira Rocha Souza",
"Nascimento","Cardoso","Barbosa","Fernandes","Martins","Rocha","Dias","Carvalho","Moura","Azevedo","de Almeida",
"Cardoso Teixeira","Barbosa Moreira","Fernandes Melo","Martins Cavalcanti","Rocha Castro","Dias Freitas",
"de Moura","da Cunha","de Carvalho","da Fonseca","de Castro","da Matta","de Azevedo","da Cruz","de Figueiredo",
"Barbosa Moreira Ribeiro","Fernandes Melo Almeida","Martins Cavalcanti Zanetti","Rocha Castro Cardoso",  
"Rocha da Silva","Castro da Silva","Azevedo da Silva","Mendes da Silva","Souza da Silva","Pereira da Silva",
"Teixeira","Santos","Moreira","Melo","Cavalcanti","Figueiredo","Castro","Freitas","Pinto","Ramos","da Mota",

]

logradouros = [ "Rua", "Avenida", "Praça", "Alameda", "Travessa", "Estrada" ]

letras_end = [ "A","B","C","D","E","F","G","H","I","J" ]

bairros = [

"Boa Vista","Parque Novo","Centro","Vila Miranda","Jardim Gonçalves","Arizona","Vila Amorim","Jardim Luciana","Medina",
"Estação","Vila Almeida","Jardim Silvestre","Coqueiro","Altinópolis","Vila Jaú","Pedreira","Morro Branco","Jardim Maia",
"Macedo","Vila Augusta","Vila Galvão","Bela Vista","Bonfim","Santa Fé","Jardim Helena","Vila Mara","São João","Jardim Marinalva"

]

cidades = [

"São Paulo - SP", "Osaco - SP", "Arujá - SP", "Guararema - SP", "Itaquaquecetuba - SP", "Suzano - SP", "Poá - SP",
"Mogi das Cruzes - SP", "Ferraz - SP", "Guarulhos - SP", "Ribeirão Pires - SP", "Santo André - SP", "São Bernardo - SP",
"São Caetano - SP", "Diadema - SP", "Mauá - SP"

]

dominios_email = ["@gmail.com", "@yahoo.com", "@outlook.com", "@icloud.com"]

separadores = [ ".","_","-","",".x","_x","-x",".y","_y","-y",".z","_z","-z" ]

categorias = {

"Papelaria": {
"marcas": ["BIC", "Faber-Castell", "Tilibra", "Chamex", "Pentel"],
"itens": [
{"nome": "Produto 1", "min_p": 2.00, "max_p": 10.00, "min_est": 50, "max_est": 100},
{"nome": "Produto 2", "min_p": 15.00, "max_p": 35.00, "min_est": 40, "max_est": 80},
{"nome": "Produto 3", "min_p": 50.00, "max_p": 120.00, "min_est": 30, "max_est": 60}

]},

"Material Elétrico": {
"marcas": ["Schneider", "Tramontina", "Steck", "Prysmian", "Taschibra"],
"itens": [
{"nome": "Produto 1", "min_p": 5.00, "max_p": 15.00, "min_est": 40, "max_est": 80},
{"nome": "Produto 2", "min_p": 25.00, "max_p": 60.00, "min_est": 30, "max_est": 60},
{"nome": "Produto 3", "min_p": 150.00, "max_p": 500.00, "min_est": 10, "max_est": 30}

]},

"Ferramentas": {
"marcas": ["Bosch", "Makita", "Stanley", "Gedore", "Vonder"],
"itens": [
{"nome": "Produto 1", "min_p": 10.00, "max_p": 30.00, "min_est": 30, "max_est": 60},
{"nome": "Produto 2", "min_p": 40.00, "max_p": 90.00, "min_est": 20, "max_est": 40},
{"nome": "Produto 3", "min_p": 200.00, "max_p": 700.00, "min_est": 5, "max_est": 20}

]},

"Informática": {
"marcas": ["Logitech", "Dell", "Kingston", "Corsair", "Asus", "Samsung"],
"itens": [
{"nome": "Produto 1", "min_p": 20.00, "max_p": 50.00, "min_est": 20, "max_est": 40},
{"nome": "Produto 2", "min_p": 120.00, "max_p": 300.00, "min_est": 10, "max_est": 20},
{"nome": "Produto 3", "min_p": 800.00, "max_p": 2500.00, "min_est": 5, "max_est": 10}

]}}

# controle de unicidade

cpfs_gerados = set()
emails_gerados = set()

# funções geradoras

def gerar_nome() -> str:

	"""Gera um nome completo aleatório."""
	return f"{random.choice(nomes)} {random.choice(sobrenomes)}"

def calcular_digito(digitos) -> int :

    soma = sum(v * i for i, v in enumerate(digitos, start=1))
    resto = soma % 11
    return 0 if resto > 9 else resto

def gerar_cpf() -> str:

	"""Gera um CPF válido único fictício."""
	while True:

		nove_digitos = [random.randint(0, 9) for _ in range(9)]		# Gera os 9 primeiros dígitos aleatórios

		digito1 = calcular_digito(nove_digitos)		# Calcula o primeiro dígito verificador
		digito2 = calcular_digito(nove_digitos + [digito1])	# Calcula o segundo dígito verificador

		cpf_lista = nove_digitos + [digito1, digito2]	# Junta tudo formando a lista completa
		cpf = "".join(map(str, cpf_lista))

		if cpf not in cpfs_gerados:	# Garante que o CPF não se repete na memória
			cpfs_gerados.add(cpf)
			return cpf
	
def gerar_endereco() -> str:
	
	"""Gera um endereço brasileiro simulado."""
	logradouro = f"{random.choice(logradouros)} {random.choice(letras_end)}"
	numero = random.randint(1,999)
	bairro = random.choice(bairros)
	cidade = random.choice(cidades)
	return f"{logradouro}, {numero}, {bairro}, {cidade}"

def gerar_telefone() -> str:

	"""Gera um número celular formatado no padrão 119XXXXXXXX."""
	restante = "".join([str(random.randint(0, 9)) for _ in range(8)])
	return f"119{restante}"

def gerar_email(nome_completo: str) -> str:

	"""Gera um e-mail único com base no nome do cliente."""
	primeiro_nome = nome_completo.split()[0].lower()

	while True:
		separador = random.choice(separadores)
		sufixo_num = random.randint(1,999)
		dominio = random.choice(dominios_email)

		email = f"{primeiro_nome}{separador}{sufixo_num}{dominio}"

		if email not in emails_gerados:
			emails_gerados.add(email)
			return email

def gerar_data_nasc(idade_min: int = 18, idade_max: int = 80) -> str:

	"""Gera uma data de nascimento no formato YYYY-MM-DD mantendo a idade na faixa limite."""
	hoje = date.today()
	dias_min = idade_min * 365
	dias_max = idade_max * 365

	dias_aleatorios = random.randint(dias_min, dias_max)
	data_nascimento = hoje - timedelta(days=dias_aleatorios)

	return data_nascimento.strftime("%Y-%m-%d")

def gerar_cliente() -> dict:

	"""Gera um dicionário completo representando um cliente."""
	nome = gerar_nome()

	cliente = {

	"nome": nome,
	"cpf": gerar_cpf(),
	"endereco": gerar_endereco(),
	"telefone": gerar_telefone(),
	"email": gerar_email(nome),
	"data_nasc": gerar_data_nasc()

}

	return cliente

def gerar_produto() -> dict:

	categoria = random.choice(list(categorias.keys()))	# 1. Sorteia a categoria
	dict_categoria = categorias[categoria]

	item_base = random.choice(dict_categoria["itens"])	# 2. Sorteia o item e sua marca
	marca = random.choice(dict_categoria["marcas"])
	
	nome_completo = f"{item_base['nome']} {marca}"	# 3. Monta um nome completo

	preco = round(random.uniform(item_base["min_p"], item_base["max_p"]), 2) 	# 4. Gera preço realista com 2 casas decimais dentro do intervalo do item
	estoque = random.randint(item_base["min_est"], item_base["max_est"])	# 5. Gera estoque aleatório

	produto = {

		"nome": nome_completo,
		"categoria": categoria,
		"preco": preco,
		"estoque": estoque
}

	return produto

def gerar_pedido(quantidade_clientes) -> dict:

	"""Gera uma data de pedido no formato YYYY-MM-DD mantendo a data na faixa limite."""
	data_min = 0
	data_max = 5
	hoje = date.today()
	dias_min = data_min * 365
	dias_max = data_max * 365
	dias_aleatorios = random.randint(dias_min, dias_max)
	data_calc = hoje - timedelta(days=dias_aleatorios)
	data_pedido = data_calc.strftime("%Y-%m-%d")

	"""Gera um número aleatório min = 1 e max = quantidade_clientes"""
	id_cliente = random.randint(1, quantidade_clientes)	

	pedido = {
	
		"data_pedido": data_pedido,
		"id_cliente": id_cliente
}

	return pedido

def gerar_item_pedido(produtos, id_pedido) -> dict:
       
	indice_sorteado = random.randrange(len(produtos))
	produto_sorteado = produtos[indice_sorteado]
	id_produto = indice_sorteado + 1
	nome_produto = produto_sorteado["nome"]
	if "Produto 1" in nome_produto:
		quantidade = random.randint(1, 10)
	elif "Produto 2" in nome_produto:
		quantidade = random.randint(1, 5)
	else:
		quantidade = random.randint(1, 2)	
	valor_unitario = produto_sorteado["preco"]
	
	item_pedido = {

		"quantidade": quantidade,
		"valor_unitario": valor_unitario,
		"id_pedido": id_pedido,
		"id_produto": id_produto
}

	return item_pedido


# funções insert_tabela

def gerar_insert_cliente(cliente) -> str:

	return f"('{cliente['nome']}','{cliente['cpf']}','{cliente['endereco']}','{cliente['telefone']}','{cliente['email']}','{cliente['data_nasc']}')"

def gerar_insert_produto(produto):

	return f"('{produto['nome']}','{produto['categoria']}',{produto['preco']},{produto['estoque']})"

def gerar_insert_pedido(pedido) -> str:

	return f"('{pedido['data_pedido']}',{pedido['id_cliente']})"

def gerar_insert_item(item_pedido):

	return f"({item_pedido['quantidade']}, {item_pedido['valor_unitario']}, {item_pedido['id_pedido']}, {item_pedido['id_produto']})"

# define quantidades de registros

quantidade_clientes = int(input("Quantos clientes deseja gerar?: "))
while quantidade_clientes <= 0:
	print("Número inválido!")
	quantidade_clientes = int(input("Digite novamente, quantos clientes deseja gerar?: "))

quantidade_produtos = int(input("Quantos produtos deseja gerar?: "))
while quantidade_produtos <= 0:
	print("Número inválido!")
	quantidade_produtos = int(input("Digite novamente, quantos produtos deseja gerar?: "))

quantidade_pedidos = int(input("Quantos pedidos deseja gerar?: "))
while quantidade_pedidos <= 0:
	print("Número inválido!")
	quantidade_pedidos = int(input("Digite novamente, quantos pedidos deseja gerar?: "))

# Abre o arquivo inserts.sql

with open("inserts.sql", "w", encoding="utf-8") as arquivo:

	arquivo.write("INSERT INTO cliente (nome,cpf,endereco,telefone,email,data_nasc) VALUES\n")

	contador = 1

	while contador <= quantidade_clientes:
		cliente = gerar_cliente()
		sql = gerar_insert_cliente(cliente)
		if contador < quantidade_clientes:
			arquivo.write(sql + ",\n")
		else:
			arquivo.write(sql + ";\n\n")

		contador += 1

	arquivo.write("INSERT INTO produto (nome,categoria,preco,estoque) VALUES\n")

	produtos = []

	contador = 1

	while contador <= quantidade_produtos:

		produto = gerar_produto()
		produtos.append(produto)
		sql = gerar_insert_produto(produto)
		if contador < quantidade_produtos:
			arquivo.write(sql + ",\n")
		else:
			arquivo.write(sql + ";\n\n")

		contador += 1

	arquivo.write("INSERT INTO pedido (data_pedido,id_cliente) VALUES\n")

	pedidos = []

	contador = 1

	while contador <= quantidade_pedidos:
		pedido = gerar_pedido(quantidade_clientes)
		pedidos.append(pedido)
		sql = gerar_insert_pedido(pedido)
		if contador < quantidade_pedidos:
			arquivo.write(sql + ",\n")
		else:
			arquivo.write(sql + ";\n\n")

		contador += 1

	arquivo.write("INSERT INTO item_pedido (quantidade,valor_unitario,id_pedido,id_produto) VALUES\n")

	itens_pedido = []

	for indice, pedido in enumerate(pedidos):
		id_pedido = indice + 1

		quantidade_itens = random.randint(1, 5)

		for i in range(quantidade_itens):
			item = gerar_item_pedido(produtos, id_pedido)
			itens_pedido.append(item)

	for contador, item in enumerate(itens_pedido, start=1):
		sql = gerar_insert_item(item)

		if contador < len(itens_pedido):
			arquivo.write(sql + ",\n")
		else:
			arquivo.write(sql + ";")

# Mensagem final

print(f"{quantidade_clientes} clientes, {quantidade_produtos} produtos, {quantidade_pedidos} pedidos e {len(itens_pedido)} itens gerados com sucesso!")
print("Arquivo inserts.sql criado! :D")