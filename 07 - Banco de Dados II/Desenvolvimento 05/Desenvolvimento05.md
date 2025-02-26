# 📜 Desenvolvimento 05

## 🎯 Descrição do Projeto 

Após uma varredura rápida no sistema de banco de dados de uma empresa de vendas, identificamos a necessidade de melhorar a segurança dessas informações. 

Por isso, será necessário desenvolver um novo banco para armazenar os dados mais importantes, como detalhes dos clientes, valores faturados diariamente e informações sobre os produtos, além de outros. 

Sendo assim, explique quais são os pilares da segurança de dados que devem ser seguidos para que o novo banco seja bem projetado e funcione corretamente

## 🛠️ Resolução

### 🔐 Pilares da Segurança de Dados

#### 1️⃣ Confidencialidade 🔒
Garante que apenas pessoas autorizadas tenham acesso aos dados sensíveis.

- **Criptografia**: Protege informações como dados dos clientes e valores faturados.  
- **Controle de acesso**: Uso de **roles (funções)** e **permissões** no banco, como `GRANT` e `REVOKE`.  
- **Autenticação e Autorização**: Uso de **senhas fortes**, **autenticação de dois fatores (2FA)** e integração com **sistemas de login seguros**.  


#### 2️⃣ Integridade 🛠️
Garante que os dados não sejam alterados ou corrompidos de forma indevida.

- **Constraints (restrições)**: Uso de `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK` para evitar inconsistências.  
- **Backup e Logs**: Implementação de **backups automáticos** e auditoria de alterações (`LOG` e `TRIGGER`).  
- **Transações seguras**: Uso de **ACID** (*Atomicidade, Consistência, Isolamento e Durabilidade*) para garantir que as operações no banco sejam confiáveis.  


#### 3️⃣ Disponibilidade ✅
Garante que o banco de dados esteja sempre acessível e funcional.

- **Redundância e Replicação**: Uso de **servidores de backup** e **replicação de dados** para evitar perda em caso de falhas.  
- **Monitoramento e Manutenção**: Ferramentas de **monitoramento de desempenho** para detectar falhas antes que afetem os usuários.  
- **Escalabilidade**: Implementação de estratégias como **sharding** e **load balancing** para suportar um grande volume de acessos.  


#### 4️⃣ Autenticidade 🆔
Garante que os dados vêm de fontes confiáveis e não foram manipulados.

- **Registro de atividades**: Logs detalhados para **rastrear alterações** e detectar acessos suspeitos.  
- **Assinatura digital e hashing**: Proteção contra adulterações através de **verificações de integridade**.  


#### 🚀 Conclusão  
Ao seguir esses pilares, o novo banco de dados será **seguro, confiável e eficiente**, protegendo informações críticas da empresa contra ataques, falhas e acessos não autorizados.
