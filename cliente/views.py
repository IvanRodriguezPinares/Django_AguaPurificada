from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Producto

def index(request):
    return render(request, 'cliente/indexBefine.html')

def crud(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente/clientes_list.html', context)

def clientes_add(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre_completo', '')
        apellido = request.POST.get('apellido', '')
        telefono = request.POST.get('telefono', '')
        email = request.POST.get('email', '')
        direccion = request.POST.get('direccion', '')

        nuevo_cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email,
            direccion=direccion
        )
        nuevo_cliente.save()

        return redirect('crud')

    return render(request, 'cliente/clientes_add.html')

def clientes_del(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('crud')
    return render(request, 'cliente/clientes_del.html', {'cliente': cliente})


def nosotros(request):
    return render(request, 'cliente/nosotros.html')

def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'cliente/productos.html', context)

def productos_list(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'cliente/productos_list.html', context)

def producto_add(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        nuevo_producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        nuevo_producto.save()

        return redirect('productos_list')

    return redirect('productos_list')

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.save()
        return redirect('productos_list')

    productos = Producto.objects.all()
    context = {'productos': productos, 'producto': producto}
    return render(request, 'cliente/productos_list.html', context)

def producto_del(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('productos_list')

def servicios(request):
    return render(request, 'cliente/servicios.html')

def contacto(request):
    return render(request, 'cliente/contacto.html')

def recarga(request):
    return render(request, 'cliente/recarga.html')
