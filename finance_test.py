from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class finance__tests():

    def __init__(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def navigate_page(self,url):
        self.driver.get(url)

    def search_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)
    
    def search_class(self, classname):
        return self.driver.find_element(By.CLASS_NAME, classname)

    def login(self,user,password):
        #self.search_xpath("")
        try:
            login_username = self.search_xpath("/html/body/main/form/div[1]/input")
            login_username.send_keys(user)
            
            login_password = self.search_xpath("/html/body/main/form/div[2]/input")
            login_password.send_keys(password)
            
            login_button = self.search_xpath("/html/body/main/form/button")
            login_button.click()
            time.sleep(3)
            
            texto_exito = "Welcome back " + user;
            texto = self.search_class("alert").text
            texto_error_uno = "invalid username and/or password"
            texto_error_dos = "You must provide a password"
            texto_error_tres = "You must provide a username"

            if texto==texto_exito:
                print("Login exitoso")
            elif texto == texto_error_uno:
                print("Usuario o contraseña incorrectos")
            elif texto == texto_error_dos:
                print("Ingrese la contraseña")
            elif texto == texto_error_tres:
                print("Ingrese el usuario")
            else:
                print("Error en el login")
        except:
            print("Error de ejecución")
    
    def register(self,name,last_name,user,email,password,phone,birthday,cc,exp,cvv):
        try:
            register_link = self.search_xpath("/html/body/nav/div/ul/li[1]/a")
            register_link.click()

            register_fname = self.search_xpath("/html/body/main/form/div[1]/div[1]/input")
            register_fname.send_keys(name)
            
            register_lname = self.search_xpath("/html/body/main/form/div[1]/div[2]/input")
            register_lname.send_keys(last_name)
            
            register_username =self.search_xpath("/html/body/main/form/div[2]/div[1]/input")
            register_username.send_keys(user)
            
            register_email = self.search_xpath("/html/body/main/form/div[2]/div[2]/input")
            register_email.send_keys(email)
            
            register_password = self.search_xpath("/html/body/main/form/div[3]/div[1]/input")
            register_password.send_keys(password)
            
            register_rpassword = self.search_xpath("/html/body/main/form/div[3]/div[2]/input")
            register_rpassword.send_keys(password)
            
            register_phone = self.search_xpath("/html/body/main/form/div[4]/div[1]/input")
            register_phone.send_keys(phone)
            
            register_birthday = self.search_xpath("/html/body/main/form/div[4]/div[2]/input")
            register_birthday.send_keys(birthday)
            
            register_cc = self.search_xpath("/html/body/main/form/div[5]/div[1]/input")
            register_cc.send_keys(cc)
            
            register_expiration = self.search_xpath("/html/body/main/form/div[5]/div[2]/input")
            register_expiration.send_keys(exp)
            
            register_cvv = self.search_xpath("/html/body/main/form/div[5]/div[3]/input")
            register_cvv.send_keys(cvv)
            
            register_button = self.search_xpath("/html/body/main/form/button")
            register_button.click()

            print("Registro exitoso")
            
            time.sleep(3)
        except:
            print('Error de registro')
        
        time.sleep(5)
    
    def quote(self,symbol):
        sym = symbol
        quote_link = self.search_xpath("/html/body/nav/div/ul[1]/li[1]/a")
        quote_link.click()
        
        try:
            imput_symbol = self.search_xpath("/html/body/main/form/div/input")
            imput_symbol.send_keys(sym)
            boton_quote = self.search_xpath("/html/body/main/form/button")
            boton_quote.click()
            time.sleep(4)
            
            try:
                self.driver.find_element(By.CLASS_NAME, "alert")
                print("\n" + sym + " no es un Symbol válido")
            except:
                main_mensaje = self.search_xpath("/html/body/main")
                texto = main_mensaje.text
                text_error = "Symbol '"+sym.upper()+"' does not exist."
                
                if(texto == text_error):
                    print("\nSymbol " + sym + " no existe")
                elif(texto != text_error):
                    if((texto.find(sym.upper()))>0):
                        print("\nExito, se encontró la acción")
                    else:
                        print("\nNo se encontró acción")
                else:
                    print("Error")
        except:
            print("\nError")
        
        time.sleep(5)
    
    def buy(self,symbol,qty):
        sym = symbol
        qty = qty
        
        buy_link = self.search_xpath("/html/body/nav/div/ul[1]/li[2]/a")
        buy_link.click()
        
        try:
            imput_symbol = self.search_xpath("/html/body/main/form/div[1]/input")
            imput_symbol.send_keys(sym)
            
            input_quantity = self.search_xpath("/html/body/main/form/div[2]/input")
            input_quantity.send_keys(qty)
            
            boton_buy = self.search_xpath("/html/body/main/form/button")
            boton_buy.click()
            time.sleep(4)
            
            try:
                alert_mensaje = self.driver.find_element(By.CLASS_NAME, "alert")
                texto = alert_mensaje.text
                text_error = sym +" does not exist"
                text_num_neg = "You must enter a number greater than 0"
                texto_short = "short for this transaction"
                text_exito = "You bought " + str(qty) + " share(s) from " + sym
                
                if texto == text_exito:
                    print("\nCompra exitosa")
                elif texto == text_error:
                    print("\nSymbol " + sym + " no existe")
                elif texto == text_num_neg:
                    print("\nIngrese un número positivo")
                elif (texto.find(texto_short))>0:
                    print("\nNo se tiene suficiente dinero")
                else:
                    print("\nError en la compra(2)")
            except:
                print("\nError en la compra(1)")
        except:
            print("\nError en la ejecución")
        
        time.sleep(5)

    def sell(self,symbol, qty):
        
        sym = symbol.upper()
        qty = qty
        
        sell_link = self.search_xpath("/html/body/nav/div/ul[1]/li[3]/a")
        sell_link.click()
        
        try:
            select_symbol = Select(self.search_xpath("/html/body/main/form/div[1]/select"))
            select_symbol.select_by_visible_text(sym)
            
            input_quantity = self.search_xpath("/html/body/main/form/div[2]/input")
            input_quantity.send_keys(qty)
            
            boton_sell = self.search_xpath("/html/body/main/form/button")
            boton_sell.click()
            time.sleep(4)
            
            try:
                alert_mensaje = self.driver.find_element(By.CLASS_NAME, "alert")
                texto = alert_mensaje.text
                text_num_neg = "You need to select a positive number"
                texto_short = "You can't sell "+ str(qty) + " shares"
                text_exito = "You sold "+ str(qty) + " share(s) from " + sym
                
                if texto == text_exito:
                    print("\nVenta exitosa")
                elif (texto.split("."))[0] == texto_short:
                    print("\nNo tiene suficientes acciones")
                elif texto == text_num_neg:
                    print("\nIngrese un número positivo")
                else:
                    print("\nError en la venta(2)")
            except:
                print("\nError en la venta(1)")
        except:
            print("\nError en la ejecución")
        
        time.sleep(5)
    
    def logout(self):
        logout_link = self.search_xpath("/html/body/nav/div/ul[2]/li/a")
        logout_link.click()
        time.sleep(5)
    
    def navigate_end(self):
        self.driver.close()
