import unittest
from billetera_app.app import app

class BilleteraAppTests(unittest.TestCase):
    
    def setUp(self):
        # Configuración común para las pruebas
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        # Limpiar después de cada prueba si es necesario
        pass

    # Caso de prueba de éxito para /billetera/contactos
    def test_obtener_contactos_exitoso(self):
        response = self.app.get('/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)
        self.assertIn("123", response.get_data(as_text=True))

    # Caso de prueba de éxito para /billetera/pagar
    def test_realizar_pago_exitoso(self):
        response = self.app.get('/billetera/pagar?minumero=21345&numerodestino=123&valor=100')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Transaccion exitosa", response.get_data(as_text=True))

    # Caso de prueba de error para /billetera/historial (cuenta no encontrada)
    def test_obtener_historial_cuenta_no_encontrada(self):
        response = self.app.get('/billetera/historial?minumero=999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Cuenta no encontrada", response.get_data(as_text=True))

    # Caso de prueba de error para /billetera/pagar (saldo insuficiente)
    def test_realizar_pago_saldo_insuficiente(self):
        response = self.app.get('/billetera/pagar?minumero=123&numerodestino=456&valor=90000')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Saldo insuficiente", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
