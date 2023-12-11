import paramiko
import logging

logging.basicConfig(level=logging.DEBUG)


# Criando uma chave SSH (client) usando o arquivo da chave privada
private_key = "/home/documentos/chave-will.pem"


key = paramiko.RSAKey.from_private_key_file(private_key)

# Criando um cliente SSH
ssh = paramiko.SSHClient()

# Adicionando a chave SSH ao cliente SSH
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Conectando ao servidor usando a chave SSH
   ssh.connect(hostname='IP-PUBLICO', username='ubuntu', pkey=key)
   print('Conectado ao servidor')
except paramiko.AuthenticationException:
    print('Falha na autenticação, por favor, verifique suas credenciais')
except paramiko.SSHException as sshException:
    print('Não é possível estabelecer a conexão SSH: ', sshException)
except paramiko.BadHostKeyException as badHostKeyException:
    print('Unable to verify server\'s host key: ', badHostKeyException)
except Exception as e:
    print('Exceção desconhecida:', e)
finally:
    ssh.close()