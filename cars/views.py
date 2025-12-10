from cars.models import Car
from cars.forms import CarForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class CarsListView(ListView):
    '''
    Classe para listagem de carros usando a classe ListView do Django
    ListView é uma classe genérica do Django que já possui métodos para listagem de objetos
    model = Car é o modelo que será listado
    template_name = 'cars.html' é o template que será renderizado
    context_object_name = 'cars' é o nome do objeto que será passado para o template
    '''

    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        '''
        Filtro de pesquisa
        super é usado para chamar o método da classe pai
        '''
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(
                model__icontains=search
            )
        return cars


class CarDetailView(DetailView):
    '''
    Classe para detalhes de um carro usando a classe DetailView do Django
    DetailView é uma classe genérica do Django que já possui métodos para detalhes de um objeto
    model = Car é o modelo que é detalhado
    template_name = 'car_detail.html' é o template que é renderizado
    context_object_name = 'car' é o nome do objeto que é passado para o template
    '''
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    '''
    Classe para criar um carro usando a classe CreateView do Django
    CreateView é uma classe genérica do Django que já possui métodos para criar objetos
    model = Car é o modelo que será criado
    form_class = CarForm é o formulário que será usado para criar o objeto
    template_name = 'new_car.html' é o template que será renderizado
    success_url = '/cars/' é a URL que será redirecionada após a criação do objeto
    '''
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    '''
    Classe para atualizar um carro usando a classe UpdateView do Django
    UpdateView é uma classe genérica do Django que já possui métodos para atualizar um objeto
    model = Car é o modelo que é atualizado
    form_class = CarForm é o formulário que é usado para atualizar o objeto
    template_name = 'car_update.html' é o template que é renderizado
    success_url = '/cars/' é a URL que é redirecionada após a atualização do objeto
    '''
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'
    success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    '''
    Classe para deletar um carro usando a classe DeleteView do Django
    DeleteView é uma classe genérica do Django que já possui métodos para deletar um objeto
    model = Car é o modelo que é deletado
    template_name = 'car_delete.html' é o template que é renderizado
    success_url = '/cars/' é a URL que é redirecionada após a exclusão do objeto
    '''
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
