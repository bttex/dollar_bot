# Notificador de Cotação do Dólar via Telegram

Este projeto monitora a cotação do dólar em relação ao real e envia uma notificação via Telegram quando o valor do dólar atinge ou fica abaixo de um valor de referência configurado.

## Funcionalidades

- Obtém a cotação do dólar utilizando a API Open Exchange Rates.
- Envia notificações para um chat específico do Telegram usando o bot configurado.
- Monitora continuamente a cotação do dólar em intervalos definidos.

## Requisitos

- Python 3.7+
- Conta no Telegram para criar um bot e obter o token de acesso.
- Dependências: `pyTelegramBotAPI`, `requests`, `python-dotenv`

## Configuração

1. **Crie um arquivo `.env` no diretório do projeto:**

   ```
   TOKEN=<seu_token_do_bot>
   CHAT_ID=<id_do_chat>
   API_URL=https://open.er-api.com/v6/latest/USD
   ```

   - Substitua `<seu_token_do_bot>` pelo token do seu bot no Telegram.
   - Substitua `<id_do_chat>` pelo ID do chat onde deseja receber as notificações.
   - Certifique-se de que a URL da API está correta.

2. **Instale as Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Execute o script para iniciar o monitoramento:

```bash
python dolar_bot.py
```

O bot ficará rodando continuamente, monitorando a cotação do dólar e enviando notificações ao atingir ou ficar abaixo do valor de referência configurado.

## Estrutura do Projeto

```
.
├── dolar_bot.py       # Script principal
├── .env               # Variáveis de ambiente
├── requirements.txt   # Dependências do projeto
```

## Exemplo de Notificação

```
O valor do dólar baixou para 4.98!
```

## Notas

- O intervalo entre as verificações está configurado para 8 horas (28800 segundos). Você pode ajustar esse valor na função `verificar_cotacao`.
- Certifique-se de que o bot possui permissão para enviar mensagens no chat configurado.

## Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie um Pull Request para revisão.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

