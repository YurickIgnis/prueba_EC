
import main 

class TestClass():
    def test_vocales1(self):
        assert main.VocalesClass("hello world").contar_vocales() == (3, 'hillu wurld')

    def test_vocales2(self):
        assert main.VocalesClass("envio click").contar_vocales() == (4, 'invou clock')    

    def test_ordenamiento_addData(self):
        data = {
            "name": "One nameE",
            "level": "One",
            "priority": "Highest"
        }
        assert main.Ordenamiento().addData(data) == "OK"
