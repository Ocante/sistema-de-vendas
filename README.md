# Sistema de Vendas

Este mini sistema de vendas foi desenvolvido em Python com interface gráfica em Tkinter e banco de dados MySQL. Ele é uma solução prática e acessível para iniciantes que desejam aprender a criar sistemas comerciais básicos. Com uma interface intuitiva e funcionalidades essenciais, ele permite desde o cadastro de produtos até a geração de relatórios de vendas.

## Funcionalidades Principais

1. **Tela de Login**  
   Sistema de autenticação de usuários, garantindo segurança e controle de acesso ao sistema. Cada usuário precisa inserir suas credenciais para acessar as funcionalidades.

   <img width="397" alt="image" src="https://github.com/user-attachments/assets/dcdafb0c-8e77-4746-92d5-8618bf188fb2">

2. **Cadastro de Usuário**  
   Tela para registro de novos usuários no sistema, com campos para inserir nome, usuário e senha, permitindo a criação de usuários administradores ou vendedores.

  <img width="398" alt="image" src="https://github.com/user-attachments/assets/e20ef6f9-a357-4077-9ac9-da421ee325dd">

3. **Cadastro de Clientes**  
   Área para registrar as informações dos clientes, incluindo nome, e-mail e telefone. Essas informações são essenciais para o acompanhamento e gestão de vendas.

   <img width="398" alt="image" src="https://github.com/user-attachments/assets/04d1ad37-4efe-42ab-a5ed-864c171f462f">

4. **Cadastro de Produtos**  
   Tela onde o administrador pode adicionar novos produtos ao sistema, preenchendo campos como nome, descrição, preço e código de barras. Cada produto cadastrado é armazenado no banco de dados e pode ser gerenciado posteriormente.

   <img width="398" alt="image" src="https://github.com/user-attachments/assets/0bb11889-9b23-4f8f-a43e-4c2ac011dd3b">

5. **Vendas de Produtos**  
   Funcionalidade para realizar vendas, onde o vendedor pode selecionar o produto e a quantidade desejada. O sistema calcula automaticamente o valor total com base no preço e na quantidade, e registra a venda no banco de dados.

   <img width="397" alt="image" src="https://github.com/user-attachments/assets/b78746eb-6209-4dd1-b5ee-53362a68ce01">

6. **Relatórios de Vendas**  
   Geração de relatórios com uma lista detalhada de todas as vendas realizadas, incluindo ID do produto, quantidade e valor total. Isso permite uma análise fácil e rápida das vendas no sistema.

    <img width="398" alt="image" src="https://github.com/user-attachments/assets/14d3e14b-f4ae-4b3c-a71f-33beb7989999">

## Banco de Dados

Utilizando o DBeaver como ferramenta de visualização e gerenciamento, o sistema é conectado a um banco de dados MySQL que armazena todas as informações, incluindo:

- **Usuários**: Armazena dados dos usuários que acessam o sistema, incluindo tipo de usuário (admin ou vendedor).
- **Clientes**: Armazena informações dos clientes cadastrados.
- **Produtos**: Contém dados dos produtos, como nome, descrição, preço, código de barras e estoque.
- **Vendas**: Registra cada venda realizada, permitindo o controle detalhado do histórico de transações.

   <img width="953" alt="image" src="https://github.com/user-attachments/assets/bd58e755-eb39-4c5f-a959-110fa17b7eeb">

Este sistema é ideal para pequenos negócios ou para uso educacional, pois apresenta funcionalidades essenciais de um sistema de vendas com uma implementação acessível e clara para iniciantes.
