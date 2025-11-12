# 📚 Exercícios de Busca Binária

> 🎯 Objetivo: dominar a lógica da busca binária, identificar erros comuns (ex: `return` mal posicionado), e aplicar o algoritmo em contextos reais.

---

## ✅ Parte 1: Exercícios Básicos (Lógica Pura)

1. **Busca Simples**  
   Implemente `busca_binaria(lista, alvo)` que retorna o **índice** do `alvo` em `lista` (ordenada), 
   ou `None` se não encontrado.  
   Teste com: `lista = [2, 4, 6, 8, 10]`, alvo = `6` → deve retornar `2`.

2. **Contagem de Iterações**  
   Modifique sua função para também retornar o número de iterações realizadas.  
   Ex: `busca_binaria_com_contador([1,3,5,7,9], 7)` → `(3, 2)` *(índice 3, 2 iterações)*.

3. **Versão Recursiva**  
   Implemente `busca_binaria_recursiva(lista, alvo, baixo=0, alto=None)` sem usar `while`.

4. **Primeira Ocorrência**  
   Dada uma lista com duplicatas ordenadas: `[1, 2, 2, 2, 3, 4]`, retorne o **menor índice** onde `alvo = 2` aparece (`→ 1`).

5. **Última Ocorrência**  
   Na mesma lista `[1, 2, 2, 2, 3, 4]`, retorne o **maior índice** onde `alvo = 2` aparece (`→ 3`).

---

## 🌍 Parte 2: Exemplos Reais (Ilustração — Não são exercícios)

> ✅ Estes servem para inspirar os próximos exercícios. Leia com atenção!

### Exemplo 1: `git bisect`  
O comando `git bisect` faz busca binária no histórico de commits para localizar o commit que introduziu um bug. Em vez de testar 1000 commits sequencialmente, ele testa ~10 (`log₂(1000) ≈ 10`).

### Exemplo 2: Índices em Bancos de Dados  
Quando uma coluna é indexada (ex: CPF), o SGBD não faz *scan* completo. Ele usa estruturas baseadas em busca binária (ex: árvores B) para localizar registros em **O(log n)**.

### Exemplo 3: Dicionários e Catálogos  
Um dicionário impresso ou digital com 200.000 palavras permite busca quase instantânea graças à ordenação + busca binária (≤ 18 comparações).

---

## 🧩 Parte 3: Exercícios Avançados com Contexto Real

6. **ISBN em Catálogo**  
   Dada uma lista de ISBNs **ordenados lexicograficamente** (ex: `["978-0-1", "978-0-2", ..., "978-9-9"]`), implemente `buscar_isbn(isbns, alvo)` retornando `True`/`False`.  
   *Dica: strings em Python são comparáveis com `<`, `>`, `==`.*

7. **Temperatura Acima de Limite**  
   Um sensor registra temperaturas a cada minuto em ordem crescente:  
   `temperaturas = [20.5, 20.8, 21.0, 22.3, ..., 45.1]`.  
   Crie `primeiro_acima(temperaturas, limite)` que retorna o **primeiro índice** onde `temp > limite`. Se nenhuma, retorne `None`.

8. **Roteamento por Prefixo de IP**  
   Dada uma lista de IPs ordenados:  
   `ips = ["10.0.0.1", "10.0.0.5", "10.0.1.0", ..., "192.168.255.254"]`,  
   implemente `gateway_mais_proximo(ips, ip_alvo)` que retorna o **maior IP ≤ ip_alvo**.  
   *Use `ipaddress.IPv4Address` do módulo `ipaddress` para comparação segura.*

9. **Posição em Ranking Decrescente**  
   Um ranking de jogadores está ordenado em **ordem decrescente** de pontos:  
   `pontos = [10000, 9800, 9500, ..., 500]`.  
   Implemente `posicao_no_ranking(pontos, nova_pontuacao)` que retorna o índice (0-based) onde a nova pontuação se encaixaria.  
   *Dica: adapte a condição de comparação (`>` vira `<`).*

10. **Busca em Logs por Timestamp**  
    Um sistema de log tem entradas com timestamps ISO 8601 ordenados:  
    `logs = ["2025-11-10T08:00:00", "2025-11-10T08:05:12", ..., "2025-11-13T15:30:00"]`.  
    Implemente `primeiro_log_apos(logs, data_iso)` que retorna o índice da primeira entrada **≥** `data_iso`.  
    *Use `datetime.fromisoformat()`.*

11. **Página de Usuário em API Paginada**  
    Uma API retorna 100 usuários por página, com IDs contínuos e ordenados (`1..100` na pág 1, `101..200` na pág 2, etc.).  
    Dado `user_id = 12345`, calcule **em qual página** ele está, **sem percorrer todas as páginas**.  
    *Dica: simule acesso à página `k` retornando o menor e maior ID dela.*

12. **Versão de Software**  
    Dada uma lista de versões ordenadas **semanticamente**:  
    `versoes = ["1.0.0", "1.0.1", "1.1.0", "2.0.0", "2.0.1"]`,  
    implemente `buscar_versao(versoes, alvo)` retornando o índice, ou `None`.  
    *Dica: crie uma função `comparar_versoes(v1, v2)` usando `list(map(int, v.split('.')))`.*

13. **Código de Barras no Supermercado**  
    Produtos são armazenados como lista de tuplas ordenadas por código de barras:  
    `produtos = [(7890000000001, "Arroz"), (7890000000002, "Feijão"), ...]`.  
    Implemente `buscar_produto(produtos, codigo)` retornando o nome ou `"Não encontrado"`.

14. **Próximo Ônibus**  
    Horários de saída (em minutos após 00:00):  
    `horarios = [360, 390, 420, 450, ..., 1320]` (6h, 6h30, 7h, ..., 22h).  
    Dado `agora = 750` (12h30), retorne o índice do **próximo ônibus** (primeiro `≥ agora`). Se for depois do último, retorne `None`.

15. **Coordenada Geográfica Mais Próxima**  
    Lista de latitudes ordenadas: `lats = [-23.55, -23.54, -23.53, ..., -22.0]`.  
    Dada `alvo = -23.525`, encontre o índice do valor **mais próximo**, usando busca binária + verificação dos vizinhos (`meio-1`, `meio`, `meio+1`).

16. **Encontrar Ponto de Virada**  
    Uma lista está **ordenada em duas partes**: primeiro crescente, depois decrescente (ex: `[1,3,5,7,6,4,2]`).  
    Use busca binária modificada para encontrar o **índice do pico** (`7` → índice `3`).  
    *Condição: `lista[i-1] < lista[i] > lista[i+1]`.*

17. **Raiz Quadrada Inteira**  
    Dado `n ≥ 0`, encontre o maior inteiro `x` tal que `x² ≤ n`, usando busca binária (sem `math.sqrt`).  
    Ex: `n = 10` → `x = 3` (pois `3²=9 ≤ 10`, `4²=16 > 10`).

---

## 💡 Dicas para Resolver

- ✅ Sempre verifique se a lista está **ordenada**.
- ⚠️ Cuidado com `return` dentro de `while` — é o erro mais comum!
- 📏 Use `print(f"baixo={baixo}, alto={alto}, meio={meio}")` para debugar.
- 🔁 Teste casos extremos: vazio, 1 elemento, primeiro, último, inexistente.
- 🧪 Para strings/datas/versões: garanta que a comparação funciona como esperado.

> ✨ **Desafio final**: implemente todos os exercícios em Python e me envie seu código — posso revisar e dar feedback!