

class Mensajes:
    
    men = {}

    texto_idioma = '''
    Idioma / Language:
    1. Español(spanish)
    2. Ingles(english)
    Seleccione / Select an option: '''

    español = {
    'menu' : '''
    Menú
    1. Menu Usuarios
    2. Menu Chefs
    3. Menu Calificaciones
    4. Menu Datos
    5. Menu Idiomas
    6. Menu Recetas
    7. Menu Productos
    8. Salir
    ''',
    'menu_producto' : '''
    Menú Productos
    1. Ver producto
    2. Agregar producto
    3. Modificar producto
    4. <-Atras
    ''',
    'ver_producto' : '''
    1. Buscar producto por código
    2. Buscar producto por nombre
    3. <-Atras
    ''',
    'menu_usuario' : '''
    Menú Usuarios
    1. Ver usuario
    2. Agregar usuario
    3. Modificar usuario
    4. Eliminar usuario
    5. <-Atras
    ''',
    'menu_chef' : '''
    Menú Chefs
    1. Ver chef
    2. Agregar chef
    3. Modificar chef
    4. Eliminar chef
    5. <-Atras
    ''',
    'menu_calificacion' : '''
    Menú Calificaciónes
    1. Ver calificación
    2. Agregar calificación
    3. Modificar calificación
    4. Eliminar calificación
    5. <-Atras
    ''',
    'menu_datos' : '''
    Menú Datoss
    1. Agregar datos ficticios
    2. <-Atras
    ''',
    'menu_idioma' : '''
    Menú Idiomas
    1. Cambiar idioma
    2. <-Atras
    ''',
    'opcion' : 'Ingrese una opcion: ',
    'opcionNoValida': '{0} no es una opcion valida',
    'salir' : 'Chaito',
    'id' : 'Digite el numero de identificación: ',
    'userNotFound' : 'Usuario no encontrado',
    'formatoUsuario' : '''
    Tipo usuario: %s
    Nombre: %s
    Identificación: %d
    Fecha nacimiento: %s
    ''',
    'formatoProducto' : '''
    Código: %s
    Nombre: %s
    Cantidad: %d %s
    Necesario: %s
    ''',
    'nombre' : 'Digite el nombre: ',
    'fecha_nac' : 'Digite la fecha de nacimiento(dd/mm/yyyy): ',
    'contrasena' : 'Digite la contraseña: ',
    'idFound' : 'Identificación existente',
    'editar_usuario' : '''
    Opciones
    1. Cambiar nombre
    2. Cambiar fecha nacimiento
    3. Cambiar Contraseña
    4. <-Atras
    ''',
    'oldContrasena' : 'Ingrese la vieja contraseña: ',
    'newContrasena' : 'Ingrese la nueva contraseña: ',
    'wrongContrasena' : 'Contraseña incorrecta',
    'yesNo' : '''
    Esta seguro?
    1. Si
    2. No
    ''',
    'opcionesVerReceta' : '''
    1. Buscar por código
    2. Buscar por nombre
    3. <-Atras
    ''',
    'tiempo' : 'Ingrese el tiempo de preparacion: ',
    'opcionesDetalleReceta' :'''
    1. Agregar Ingrediente
    2. Editar Ingrediente
    3. 

    '''
    }

    ingles = {
    'menu' : '''
    Menu
    1. Menu Users
    2. Menu Chefs
    3. Menu Ratings
    4. Menu Data
    5. Menu Language
    6. Exit
    ''',
    'menu_usuario' : '''
    Menu Users
    1. View user
    2. Add user
    3. Update user
    4. Delete user
    5. <-Back
    ''',
    'menu_chef' : '''
    Menu Chefs
    1. View chef
    2. Add chef
    3. Update chef
    4. Delete chef
    5. <-Back
    ''',
    'menu_calificacion' : '''
    Menu Ratings
    1. View rating
    2. Add rating
    3. Update rating
    4. Delete rating
    5. <-Back
    ''',
    'menu_datos' : '''
    Menu Data
    1. Add ficticious data
    2. <-Back
    ''',
    'menu_idioma' : '''
    Menu Languages
    1. Change Language
    2. <-Back
    ''',
    'opcion' : 'Enter an option: ',
    'opcionNoValida' : '{0} is not a correct option',
    'salir' : 'Bye Bye',
    'id' : 'Enter the identification number: ',
    'userNotFound' : 'User not found',
    'formatoUsuario' : '''
    User type: %s
    Name: %s
    identification: %d
    Born date: %s
    ''',
    'formatoProducto' : '''
    Code: %s
    Name: %s
    Quantity: %d %s
    Required: %s
    ''',
    'nombre' : 'Enter the name: ',
    'fecha_nac' : 'Enter the born date(dd/mm/yyyy): ',
    'contrasena' : 'Enter the password: ',
    'idFound' : 'Identification found',
    'editar_usuario' : '''
    Options
    1. Change name
    2. Change born date
    3. Change password
    4. <-Back
    ''',
    'oldContrasena' : 'Enter the old password: ',
    'newContrasena' : 'Enter the new password: ',
    'wrongContrasena' : 'Wrong password',
    'yesNo' : '''
    Are you sure?
    1. Yes
    2. No
    ''',
    'opcionesVerReceta' :'''
    1. Search by code
    2. Search by name
    3. <-Back
    ''',
    'tiempo': 'Enter the preparation time: '
    }