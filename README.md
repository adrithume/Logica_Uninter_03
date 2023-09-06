# Lógica de Programação <img src="https://marcas-logos.net/wp-content/uploads/2020/11/Python-logo.png" width="10%" height="10%" align="right" valign="center"/> 
Projeto realizado na disciplina de Lógica de Programação do curso de Análise e Desenvolvimento de Sistemas, em linguagem Python, utilizando a IDE PyCharm.
## Enunciado: 
Imagina-se que você e sua equipe foram contratados por uma empresa de logística que acabou de entrar no ramo. Essa empresa trabalha com encomendas de pequeno e médio porte e opera somente entre 3 cidades.O valor que a empresa cobra por objeto é dado pela seguinte equação: "total = dimensões * peso * rota". Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:
### Dimensões x Valor
* volume < 1000 	- 10
* 1000   <= volume < 10000	- 20
* 10000 <= volume < 30000	- 30
* 30000 <= volume < 100000	- 50
* volume >= 100000 - 	Não é aceito
#### Peso x Multiplicador
* peso <= 0.1	- 1
* 0.1 <= peso < 1	- 1.5
* 1    <= peso < 10	- 2
* 10  <= peso < 30	- 3
* peso =>   30	- Não é aceito
##### Rota x Multiplicador
* RS - De Rio de Janeiro até São Paulo	- 1
* SR - De São Paulo até Rio de Janeiro	- 1
* BS - De Brasília até São Paulo	- 1.2
* SB - De São Paulo até Brasília	- 1.2
* BR - De Brasília até Rio de Janeiro	- 1.5
* RB - Rio de Janeiro até Brasília	- 1.5
########## Elabore um programa em Python que:
1.	Pergunte a altura (em cm), comprimento (em cm) e largura (em cm) do objeto. Se digitar um valor não numérico e/ou as dimensões passarem do limite aceito repetir a pergunta;
2.	Pergunte o peso do objeto (em kg). Se digitar um valor não numérico e/ou o peso passar do limite aceito repetir a pergunta;
3.	Pergunte a rota do objeto. Se digitar uma opção que não esteja na tabela repetir a pergunta;
4.	Encerre o total a ser pago com base na equação desse enunciado;	

