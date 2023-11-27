
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='Home'),

    path('paciente_login/', views.paciente_login, name='paciente_login'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('homePaciente/', views.homePaciente, name='homePaciente'),
    path('sucessoCadastro/', views.sucessoCadastroView, name='sucessoCadastro'),
    path('falhaCadastro/', views.falhaCadastroView, name='falhaCadastro'),
    path('homePaciente/exames/', views.exibir_exames, name='exibir_exames'),
    path('homePaciente/receituarios/',
         views.exibir_receituarios, name='exibir_receituarios'),
    path('homePaciente/exames/examehemograma/',
         views.examehemograma, name='examehemograma'),
    path('homePaciente/exames/exameurina/',
         views.exameurina, name='exameurina'),
    path('homePaciente/receituarios/receita', views.receita, name='receita'),
    path('homePaciente/booking/', views.booking, name='booking'),
    path('homePaciente/booking/booking-submit',
         views.bookingSubmit, name='bookingSubmit'),
    path('homePaciente/user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>',
         views.userUpdateSubmit, name='userUpdateSubmit'),
    path('staff-panel', views.staffPanel, name='staffPanel'),
    path('homePaciente/recibos/', views.exibir_recibos, name='exibir_recibos'),
    path('homePaciente/recibos/recibopag', views.recibopag, name='recibopag'),
    path('user-cancel/<int:id>', views.userCancel, name='userCancel'),
]
