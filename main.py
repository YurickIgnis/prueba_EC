import input

class Ordenamiento():
    def __init__(self):
        self.datos = input.data
        self.prioridad = ("highest","high","medium","low","lowest")  
        self.nivel = ("zero","one","two","three","four","five")    
        self.is_ordenado = False
    def ordenar(self):
        for k,v in self.datos.items():
            v["level"] = self.nivel.index(v["level"].lower())
            v["priority"] = self.prioridad.index(v["priority"].lower())
            for k,v in v.items():
                if isinstance(v,dict):
                    v["level"] = self.nivel.index(v["level"].lower())
                    v["priority"] = self.prioridad.index(v["priority"].lower())
                    for k,v in v.items():
                        if isinstance(v,dict):
                            v["level"] = self.nivel.index(v["level"].lower())
                            v["priority"] = self.prioridad.index(v["priority"].lower())
                                  
        self.datos = dict(sorted(self.datos.items(), key = lambda x: x[1]['priority'])) 
        self.datos = dict(sorted(self.datos.items(), key = lambda x: x[1]['level'])) 
        self.is_ordenado = True    

  

    def show(self):
        if not self.is_ordenado:
            self.ordenar()
        for k,v in self.datos.items():
            print("->",v["name"])
            for k,v in v.items():
                if isinstance(v,dict):
                    print("--->",v["name"])
                    for k,v in v.items():
                        if isinstance(v,dict):
                            print("------>",v["name"])
        return "OK"                    
                    
    def addData(self, data):
        self.datos["nuevo_dato"] = data
        self.ordenar()
        self.show()
        return "OK"


class VocalesClass():
    def __init__(self, frase):
        self.frase = frase
        self.vocales = ("a","e","i","o","u")
    def contar_vocales(self):
        vocales_list = list(self.frase)
        contador = 0
        for i in range(len(vocales_list)):
            if vocales_list[i] in self.vocales:
                contador += 1
                vocal_reemplazo = self.vocales[0] if vocales_list[i] == self.vocales[-1] else self.vocales[int(self.vocales.index(vocales_list[i]))+1]
                vocales_list[i] = vocal_reemplazo
        self.frase = "".join(vocales_list)
        return (contador,self.frase)
        




if __name__ == '__main__':
    data = {
            "name": "One nameE",
            "level": "One",
            "priority": "Highest"
    }
    
    print(VocalesClass("envio click").contar_vocales()) 
    Ordenamiento().show()

