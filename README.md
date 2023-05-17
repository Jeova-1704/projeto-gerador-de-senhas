# Gerador de Senhas

<div align="center">
  <img src=https://github.com/Jeova-1704/projeto-gerador-de-senhas/assets/127805808/1cd0d84a-3147-4c11-accc-2727190360f7
</div>
<div align="center">
  <img src=https://github.com/Jeova-1704/projeto-gerador-de-senhas/assets/127805808/25f2e690-5082-4e56-862d-012b725ee036</img>
  <img src=https://github.com/Jeova-1704/projeto-gerador-de-senhas/assets/127805808/0dd693e6-49f7-4518-8c8b-9efc382874aa</img>
</div>



Este é um programa desenvolvido por Jeova Bezerra ([@Jeova-1704](https://github.com/Jeova-1704)) e Pierre Monteiro ([@pierreOF](https://github.com/pierreOF)) para gerar senhas aleatórias com base nas preferências do usuário. O código foi implementado utilizando programação orientada a objetos (POO) em Python, o mesmo sendo transformado em um arquivo executável(.exe) para instalar e testar em sua maquina.

## Funcionalidades:
<h4>O programa possui as seguintes funcionalidades:</h4>
<ul>
  <li>Geração de senhas aleatórias: o usuário pode definir o número de caracteres desejados, bem como escolher quais tipos de caracteres incluir na senha (letras maiúsculas, letras minúsculas, números e caracteres especiais).</li>
  <li>Avaliação de segurança da senha: o programa avalia a segurança da senha gerada com base em critérios como comprimento, presença de letras maiúsculas, letras minúsculas, números e caracteres especiais. A segurança é classificada como "Senha Fraca", "Senha Intermediária" ou "Senha Forte".</li>
  <li>Copiar senha para a área de transferência: o programa permite copiar a senha gerada para a área de transferência, facilitando sua utilização em outros aplicativos.</li>
</ul>

## Arquivos
<h4>O código está dividido em dois arquivos principais:

### `back.py`
<h4>Este arquivo contém a implementação do backend do programa. Ele foi feito com POO e define a classe `GeradorSenha`, responsável por gerar senhas aleatórias, avaliar a segurança das senhas e copiá-las para a área de transferência.</h4>
<h4>A classe GeradorSenha possui os seguintes métodos:</h4>
<ul>
  <li>"gerar_senha(n_caracteres, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_especiais)": Este método recebe como parâmetros o número de caracteres desejados para a senha e quais tipos de caracteres devem ser incluídos (maiúsculas, minúsculas, números e caracteres especiais). A partir desses parâmetros, o método gera uma senha aleatória e a retorna.</li>
  <li>"avaliar_senha(senha)": Este método recebe uma senha como parâmetro e avalia sua segurança, atribuindo uma classificação de "Senha Fraca", "Senha Intermediária" ou "Senha Forte". A avaliação é baseada em critérios como comprimento da senha, uso de caracteres especiais, letras maiúsculas e números.</li>
</ul>
  <h4>Além disso, o programa define as seguintes funções:</h4>
  <ul>
  <li>verificar_credenciais(usuario, senha): Esta função recebe um nome de usuário e uma senha como parâmetros e verifica se as credenciais são válidas. Neste exemplo, as credenciais válidas são "Admin" para o nome de usuário e "Admin" para a senha. A função retorna True se as credenciais forem válidas e False caso contrário.</li>
  </ul>
  <h4>Você pode adicionar mais métodos à classe GeradorSenha ou funções adicionais ao arquivo back.py de acordo com suas necessidades. O uso de classes e métodos ajuda a organizar o código e facilita a reutilização de funcionalidades em diferentes partes do programa. Certifique-se de instalar as bibliotecas necessárias para executar o programa, como mencionado anteriormente, e siga as instruções fornecidas na seção anterior para executar o programa. Lembre-se de que este programa é um exemplo simples e pode ser aprimorado e adaptado de várias maneiras para atender às suas necessidades específicas.</h4>
  
  
### `front.py`
<h4>Este arquivo contém a implementação do frontend do programa, utilizando a biblioteca PySimpleGUI para criar a interface de usuário. Ele define duas janelas: uma janela de login e uma janela principal. A janela de login é exibida inicialmente e permite que o usuário entre com suas credenciais. Após o login bem-sucedido, a janela principal é exibida, onde o usuário pode gerar senhas e realizar outras ações.</h4>
<h4>A janela de login possui os seguintes elementos:</h4>  
<ul>
  <li>Campos de entrada: há dois campos de entrada para o usuário digitar seu nome de usuário e senha.</li>
  <li>Botão "Entrar": ao clicar neste botão, o programa verifica se as credenciais fornecidas estão corretas e exibe a janela principal em caso de sucesso ou exibe uma mensagem de erro em caso de falha no login </li>
</ul>
<h4>A janela principal possui os seguintes elementos:</h4>
<ul>
  <li>Campos de configuração da senha: o usuário pode definir o número de caracteres desejados para a senha e escolher quais tipos de caracteres incluir na senha (letras maiúsculas, letras minúsculas, números e caracteres especiais).</li>
  <li>Botão "Gerar Senha": ao clicar neste botão, o programa utiliza a classe GeradorSenha do arquivo back.py para gerar uma senha aleatória com base nas configurações definidas pelo usuário. </li>
  <li>Área de exibição da senha gerada: a senha gerada é exibida neste campo após o usuário clicar no botão "Gerar Senha".</li>
  <li>Botão "Avaliar Senha": ao clicar neste botão, o programa utiliza a classe GeradorSenha do arquivo back.py para avaliar a segurança da senha gerada, exibindo uma classificação de "Senha Fraca", "Senha Intermediária" ou "Senha Forte".</li>
  <li>Botão "Copiar para Área de Transferência": ao clicar neste botão, o programa copia a senha gerada para a área de transferência do sistema operacional.</li>
</ul>

<h4>Além disso, o programa define as seguintes funções:</h4>  
<ul>
  <li>janela_login(): exibe a janela de login e verifica as credenciais fornecidas pelo usuário.</li>
  <li>janela_principal(): exibe a janela principal após o login bem-sucedido, permitindo ao usuário gerar senhas, avaliar a segurança das senhas e copiá-las para a área de transferência.</li>
</ul>
 
## Como executar o programa:
<h4>1-Certifique-se de ter o Python instalado em seu ambiente. Você pode baixar o Python em https://www.python.org/downloads/</h4>
<h4>2-instale as bibliotecas necessárias executando o seguinte comando no terminal:</h4>
  <pre>pip install PySimpleGUI</pre>
  <pre>pip install pyperclip</pre>
<h4>3-Baixe os arquivos back.py e front.py e salve-os em uma pasta.</h4>
<h4>4-Execute o arquivo front.py para iniciar o programa. Você</h4>
<h4>5-A janela de login será exibida. Insira as credenciais (usuário: "Admin", senha: "Admin") e clique no botão "Entrar".</h4>
<h4>6-A janela principal será exibida. Agora você pode gerar senhas, avaliar a segurança das senhas e copiá-las para a área de transferência.</h4>
  
## Considerações finais
<h4>A interface de usuário do Gerador de Senhas foi desenvolvida utilizando programação orientada a objetos (POO) para organizar e estruturar o código. Essa abordagem permite uma melhor separação de responsabilidades e facilita a manutenção e extensão do programa.</h4>
<h4>Junto com os arquivos do projeto segue um arquivo executavél do mesmo, para caso de você não tenha o python instalado me sua maquina ou deseja ter o nosso projeto em seu computador.</h4>
  
  
  
