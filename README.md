# S.O.L.I.D
Repositório para apoio ao estudo dos princípios S.O.L.I.D usando a linguagem Python.

## 1. SRP – Single Responsibility Principle (Princípio da Responsabilidade Única)
### Definição:
Uma classe deve ter apenas uma razão para mudar, ou seja, ela deve ter uma única responsabilidade bem definida.

### Objetivo:
Separar responsabilidades distintas em classes diferentes para manter o código mais organizado, testável e de fácil manutenção.

## 2. OCP – Open/Closed Principle (Princípio Aberto/Fechado)
### Definição:
Classes devem estar abertas para extensão, mas fechadas para modificação.

### Objetivo:
Evitar alterações diretas em código existente. Permitir adicionar funcionalidades herdando ou usando composição, e não modificando.

## 3. LSP – Liskov Substitution Principle (Princípio da Substituição de Liskov)

### Definição:
Subtipos devem ser substituíveis por seus tipos base sem quebrar a lógica do programa.

### Objetivo:
Garantir que heranças respeitem o comportamento esperado, sem efeitos colaterais

## 4. ISP – Interface Segregation Principle (Princípio da Segregação de Interface)

### Definição:
Nenhuma classe deve ser forçada a implementar métodos que não utiliza.
### Objetivo:
Evitar interfaces grandes e genéricas. Criar interfaces específicas para cada tipo de cliente.

## 5. DIP – Dependency Inversion Principle (Princípio da Inversão de Dependência)
### Definição:
NDependa de abstrações, e não de implementações concretas.
### Objetivo:
Permitir que classes sejam reutilizáveis, testáveis e de baixo acoplamento.