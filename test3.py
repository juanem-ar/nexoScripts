from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Iniciar Google Chrome
driver = webdriver.Chrome();

# Navegar a www.docusign.com
driver.get("https://www.docusign.com");

# Se borran todas las cookies del sitio y se aguarda 3 segundos hasta que cargue el div con el mensaje de "Aceptar cookies"
driver.delete_all_cookies();
time.sleep(3);

# Se selecciona el botón de cookies y hacemos click en él
button_cookies = driver.find_element(By.ID,'onetrust-accept-btn-handler');
button_cookies.click();
time.sleep(3);

# Se selecciona el botón de "Free Trial o Try for free" y hacemos click en él
button_try = driver.find_element(By.CLASS_NAME,'css-x91yru.ep5kedm0');
button_try.click();

# Se espera a que el sistema cambie de pantalla
time.sleep(3);

# Se selecciona el input Email y se le agrega un contenido
input_email = driver.find_element(By.ID,'email');
input_email.send_keys("test@test.com");

# Se selecciona el botón "Comenzar" y se hace click en él
button_start = driver.find_element(By.CLASS_NAME, "css-1b2deny");
button_start.click();

# Se espera a que el sistema cambie de pantalla
time.sleep(6);

# Imprimir título y URL
print('Título: ', driver.title);
print('URL: ', driver.current_url);

# Se seleccionan los inputs y se completan los campos del formulario
input_name = driver.find_element(By.ID,'fname');
input_name.send_keys("Jhon");
time.sleep(1);
input_lname = driver.find_element(By.ID,'lname');
input_lname.send_keys("Smith");
time.sleep(1);
input_phone = driver.find_element(By.ID,'phone');
input_phone.send_keys("123123");
time.sleep(1);

# Se selecciona el botón "Siguiente" y se hace click en él para validar los campos
button_validate = driver.find_element(By.CLASS_NAME, "css-u170zz");
button_validate.click();
time.sleep(6);

# Validar título y URL
print('Título: ', driver.title);
print('URL: ', driver.current_url);

# Se finaliza la prueba y se cierra la ventana
driver.quit();
