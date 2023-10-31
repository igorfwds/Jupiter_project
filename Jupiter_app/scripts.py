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

#para mais palavras cruzadas, acesse: https://oglobo.globo.com/jogos/palavras-cruzadas/

receita.save()

#altere conforme necessário

from Jupiter_app.models import Appointment

# Para excluir um agendamento específico (substitua 'id_do_agendamento' pelo ID real do agendamento)
agendamento = Appointment.objects.get(id=id_do_agendamento)
agendamento.delete()

# Para excluir todos os agendamentos que atendam a determinados critérios (por exemplo, todos os agendamentos de um paciente específico)
Appointment.objects.filter(user=paciente).delete()
