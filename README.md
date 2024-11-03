# Sistema de Vendas

Este mini sistema de vendas foi desenvolvido em Python com interface gráfica em Tkinter e banco de dados MySQL. Ele é uma solução prática e acessível para iniciantes que desejam aprender a criar sistemas comerciais básicos. Com uma interface intuitiva e funcionalidades essenciais, ele permite desde o cadastro de produtos até a geração de relatórios de vendas.

## Funcionalidades Principais

1. **Tela de Login**: Sistema de autenticação de usuários, garantindo segurança e controle de acesso ao sistema. Cada usuário precisa inserir suas credenciais para acessar as funcionalidades.

   ![Tela de Login](https://github.com/user-attachments/assets/b38bad11-4fb5-4ff5-b443-328876d42fce)

2. **Cadastro de Usuário**: Tela para registro de novos usuários no sistema, com campos para inserir nome, usuário e senha, permitindo a criação de usuários administradores ou vendedores.

   ![Cadastro de Usuário](https://github.com/user-attachments/assets/47fac3c2-f46e-4507-b117-5eb24ec808b0)

3. **Cadastro de Clientes**: Área para registrar as informações dos clientes, incluindo nome, e-mail e telefone. Essas informações são essenciais para o acompanhamento e gestão de vendas.

   ![Cadastro de Clientes](https://github.com/user-attachments/assets/bb609bfa-6ca4-4950-92c2-129438f5210b)

4. **Cadastro de Produtos**: Tela onde o administrador pode adicionar novos produtos ao sistema, preenchendo campos como nome, descrição, preço, e código de barras. Cada produto cadastrado é armazenado no banco de dados e pode ser gerenciado posteriormente.

   ![Cadastro de Produtos](https://github.com/user-attachments/assets/331a80f5-63ff-4b6a-bf10-176de39ffb1a)

5. **Vendas de Produtos**: Funcionalidade para realizar vendas, onde o vendedor pode selecionar o produto e a quantidade desejada. O sistema calcula automaticamente o valor total com base no preço e na quantidade, e registra a venda no banco de dados.

   ![Vendas de Produtos](https://github.com/user-attachments/assets/abafd026-2735-4150-919f-5d0b50357869)

6. **Relatórios de Vendas**: Geração de relatórios com uma lista detalhada de todas as vendas realizadas, incluindo ID do produto, quantidade e valor total. Isso permite uma análise fácil e rápida das vendas no sistema.

   ![Tela de Relatórios de Vendas](https://github.com/user-attachments/assets/3361cdd5-b166-4609-a183-adaaad4db8b4)

## Banco de Dados

Utilizando o DBeaver como ferramenta de visualização e gerenciamento, o sistema é conectado a um banco de dados MySQL que armazena todas as informações, incluindo:
- **Usuários**: Armazena dados dos usuários que acessam o sistema, incluindo tipo de usuário (admin ou vendedor).
- **Clientes**: Armazena informações dos clientes cadastrados.
- **Produtos**: Contém dados dos produtos, como nome, descrição, preço, código de barras e estoque.
- **Vendas**: Registra cada venda realizada, permitindo o controle detalhado do histórico de transações.

   ![Tela de Banco de Dados no DBeaver](https://github.com/user-attachments/assets/4f9ade3d-2c6d-4264-a4b6-bd9a8249c68d)

Este sistema é ideal para pequenos negócios ou para uso educacional, pois apresenta funcionalidades essenciais de um sistema de vendas com uma implementação acessível e clara para iniciantes.
