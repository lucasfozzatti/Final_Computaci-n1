class TemaMusical():
    def __init__(self, codigo=None, nombre=None, duracion=0, interprete=None):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        self.interprete = interprete
    #------------------------------------------
    #obtengo atributo
    @property
    def codigo(self):
        return self._codigo
    #seteo atributo
    @codigo.setter
    def codigo(self,val):
        if val == '':
            raise EmptyError('Codigo vacio...')
        else:
            self._codigo = val
    #------------------------------------------
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,val):
        if val == '':
            raise EmptyError('Nombre vacio...')
        else:
            self._nombre = val
    #------------------------------------------
    @property
    def duracion(self):
        return self._duracion
    
    @duracion.setter
    def duracion(self,val):
        if val < 0:
            raise ValueError('Duracion negativa...')
        else:
            self._duracion = val
    #------------------------------------------
    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self,val):
        if val == '':
            raise EmptyError('Interprete vacio...')
        else:
            self._interprete = val
    #------------------------------------------
    def __str__(self):
        songs = 'codigo: '+ self.codigo+'\n\tnombre: '+self.nombre +'\n\tduracion: '+ str(self.duracion)+'\n\tinterprete: ' +self.interprete+'\n'
        return(songs)
    #------------------------------------------
    def input(self,codigo=False):
        if codigo == True:
            self._codigo = self.codigo
        else:    
            c=input('Ingrese Codigo: ')
            self._codigo=c
        n=input('Ingrese Nombre: ')
        d=int(input('Ingrese Duracion: '))
        i=input('Ingrese Interprete: ')
        self._nombre=n
        self._duracion=d
        self._interprete=i
#Error
class EmptyError(ValueError):
    pass
