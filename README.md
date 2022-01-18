Pasos a seguir para probar mi proyecto:
- iniciar pipenv
- migrar django para generar la base de datos
- pagina principal link a paginas secundarias
- creacion vistas para crear elementos
- formularios para crear vecinos, mascotas y casas
- se agrego formato con js y css a las paginas
- creacion de super user --> admin, pass: 123
- registro de modelos en admin.py
- creacion de CRUD
- se creo el login y el logout
- usuario creado --> username: user, password: pass123456
- se creo un register
- se agregaron los forms correspondientes en archivo forms.py de registro, editar y avatar
- utilizacion de LoginRequiredMixin para vista de vecinos
- utilizacion de decoradores para eliminar datos


No funciona:
- el login no se muestra
- No se muestran las mascotas
- cuando se genera un vecino nuevo va a un page not found

Correcciones:
- Se arreglo el login. Ahora se muestra.
- Se muestran las mascotas
- se arreglaron los vecinos. Clases basadas en vistas. Se pueden ver detalles, editar y eliminar. (se implementó la clase basada en vista de edición de datos para vecinos)
- se agrego boton de registro
- apartado de mascotas funciona.
- al avatar se le agrego una imagen default.


Video explicativo:
https://drive.google.com/file/d/1ySLNoMOyX3PXpxtyGgeHEIPJgyF7LK0K/view?usp=sharing