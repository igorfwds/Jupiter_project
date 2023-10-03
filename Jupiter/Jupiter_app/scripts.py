#para iniciar o processo de alimentação de dados na mão, navegue pelo terminal até o manage.py
#digite 'py manage.py shell'
#insira os comandos abaixo:

from django.contrib.auth.models import User
from Jupiter_app.models import Exame, Receituario

#para add exames:

user = User.objects.get(username='jvfg@cesar.school')

exame = Exame(usuario=user, nome='Ultrassonografia de esôfago', data_realizacao='2023-10-03', resultado='Gastrite')

exame.save()

# para add receituários:

user = User.objects.get(username='jvfg@cesar.school')

receita = Receituario(usuario=user, nome='Receita de Garasone', data_emissao='2023-10-02', conteudo='Aplicar 3 gotas em cada narina 4x ao dia')

receita.save()

#altere conforme necessário