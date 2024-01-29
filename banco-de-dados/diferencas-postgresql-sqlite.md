# Principais diferenças entre PostgreSQL e SQLite
1. **Escalabilidade:**
   - **PostgreSQL:** Adequado para grandes volumes de dados e tráfego.
   - **SQLite:** Mais leve, ideal para projetos menores, móveis e embarcados.

2. **Arquitetura:**
   - **PostgreSQL:** Servidor cliente/servidor completo, com suporte a procedimentos armazenados e visões complexas.
   - **SQLite:** Banco de dados incorporado, opera no mesmo processo do aplicativo, mais simples e sem necessidade de servidor separado.

3. **Concorrência:**
   - **PostgreSQL:** Suporta operações concorrentes robustas.
   - **SQLite:** Suporta concorrência em grau menor, possíveis bloqueios em algumas operações.

4. **Tipos de Dados:**
   - **PostgreSQL:** Oferece variedade extensa de tipos e permite tipos de dados personalizados.
   - **SQLite:** Suporta conjunto menor de tipos em comparação com o PostgreSQL.

5. **Administração:**
   - **PostgreSQL:** Ferramentas avançadas, comunidade ativa, mais complexo em administração.
   - **SQLite:** Leve em administração, gerenciado por comandos SQL ou ferramentas simples.

6. **Uso:**
   - **PostgreSQL:** Para ambientes de produção com cargas intensivas e complexas.
   - **SQLite:** Comum em aplicativos móveis, embarcados e ambientes leves, enfatizando simplicidade e portabilidade.

## Diferença na sintaxe 

Embora o PostgreSQL e o SQLite compartilhem muitas semelhanças na sintaxe SQL padrão, há algumas diferenças específicas.

### Autoincremento de Colunas
   - **PostgreSQL:** Usa a sintaxe `SERIAL` para criar uma coluna autoincremento. Por exemplo: `id SERIAL PRIMARY KEY`.
   - **SQLite:** Utiliza a palavra-chave `INTEGER` com a restrição `AUTOINCREMENT`. Por exemplo: `id INTEGER PRIMARY KEY AUTOINCREMENT`.

### Funções de Data e Hora
   - **PostgreSQL:** Pode usar funções específicas, como `CURRENT_DATE`, `CURRENT_TIME`, `CURRENT_TIMESTAMP`, e possui uma variedade de funções de manipulação de data e hora.
   - **SQLite:** Usa funções como `date('now')`, `time('now')`, `datetime('now')` para obter valores de data e hora.

