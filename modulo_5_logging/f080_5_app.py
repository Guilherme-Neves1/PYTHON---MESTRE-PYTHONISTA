# Logging => Manter o histórico do que está acontecendo e do que já aconteceu.

import logging
'''
Níveis de logging:

debug    - Só estou passando informações para devs.
info     - Só estou informando algo que está acontecendo no programa, mas que não é um erro.
warning  - Só estou alertando sobre algo que está acontecendo, possívelmente fora do esperado, que ainda não é um erro mas pode gerar um futuramente.
error    - Um erro que ocorreu na aplicação
critical - Um erro com consequências graves que acaba de ocorrer na aplicação
'''

# Logging só exibe mensagens do nível warning pra cima por padrão.
# Para burlar isso usamos basicConfig

logging.basicConfig(level=logging.DEBUG, filename='f080_app.log', filemode='a', format='%(levelname)s - %(message)s') # Setar o nível
logging.debug("Logging nível debug")
logging.info("Logging nível info")

logging.warning("Logging nível warning")
logging.error("Logging nível error")
logging.critical("Logging nível critical")
