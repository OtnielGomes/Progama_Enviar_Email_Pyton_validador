from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep
def criação_email():
    """
    criação_email: Faz a captação de dados para envio do email, e
    validação deles.
    :return: retorna o destinatário, assunto do email e o texto do email.
    """
    while True:
        while True:
            destinatário = str(input('Digite o destinatário para enviar o '
                                     'email: ')).strip().lower()
            if ' ' not in destinatário:
                if '@' and '.com' in destinatário:
                    break
            else:
                print('Email inválido. Digite novamente')
        while True:
            assunto = str(input('Digite o assunto de seu email: '))
            texto = str(input('Digite o texto de seu email: '))
            if len(assunto) >0 and len(texto) > 0:
                break
            else:
                print('Os campos de assunto ou texto não podem ser vazios')

        return destinatário, assunto, texto


def login():
    """
    login: faz a captação do endereço do email e a senha do usuário, e
    também faz a validação dessas informações.
    :return: faz o retorna do login e da senha
    """
    while True:
        while True:
            email = str(input('Digite o seu email: ')).strip().lower()
            if ' ' not in email:
                if '@' and '.com' in email:
                    break
            else:
                print('Email invalido')
        while True:
            senha = str(input('Digite sua senha: '))
            if len(senha) > 0:
                break
            else:
                print('Senha inválida.')
        return email, senha


def selecionar_servidor(user_email):
    """
    selecionar_servidor: verifica qual o servidor para fazer a conexão
    com o servidor adequando ao email do usuário.
    :param user_email:endereço de email
    :return:server para conexão do email para envio da mensagem
    """
    find_server = user_email.index('@')
    sever = f'smtp.{user_email[find_server+1:]}: 587'
    return sever


#Montagem e recebemento de informações para criar o email
try:
    msg = MIMEMultipart()
    msg['To'], \
    msg['Subject'], \
    texto_email = criação_email()
except:
    print('Erro ao criar email')
else:
    print('Email criado com sucesso.')
try:
    print('Efetuar login para enviar o email:')
    sleep(1)
    msg['From'], \
    senha = login()
    #montagem do corpo do email
    msg.attach(MIMEText(texto_email, 'plain'))
    server = smtplib.SMTP(selecionar_servidor(msg['From']))
    server.starttls()
    #Login na conta para envio
    server.login(msg['From'], senha)
except:
    print('Erro ao efetuar login')
else:
    print('Login efetuado com sucesso.')
try:
    print('Enviando mensagem...')
    sleep(2)
    #Envio da mensagem
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    # Encerramento do servidor
    server.quit()
except:
    print('Erro ao enviar mensagem.')
else:
    print('Mensagem enviado com sucesso!')