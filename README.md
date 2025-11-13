# Projeto exemplo com GitHub Actions

Este repositório demonstra como configurar um pequeno projeto em Python com testes automatizados e integração contínua via GitHub Actions executando em múltiplos sistemas operacionais e versões da linguagem.

## Estrutura

- `src/`: código-fonte da aplicação (`math_utils.py`).
- `tests/`: testes unitários escritos com Pytest.
- `.github/workflows/ci.yml`: pipeline de CI que executa em Ubuntu, macOS e Windows, usando uma matriz de versões do Python.

## Pré-requisitos locais

1. Criar e ativar um ambiente virtual (opcional porém recomendado).
2. Instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Executar os testes localmente:
   ```bash
   pytest
   ```

## Workflow do GitHub Actions

O arquivo `ci.yml` já está pronto para ser incluído no repositório. Ele é disparado a cada `push` ou `pull_request`, instalando as dependências e executando `pytest` em:

- Sistemas operacionais: Ubuntu, macOS e Windows.
- Versões do Python: 3.10 e 3.11.

Após o primeiro push, navegue até a aba **Actions** no GitHub para acompanhar as execuções. Para submissão no Moodle, copie o link do último workflow com status *success*.



