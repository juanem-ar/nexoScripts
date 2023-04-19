from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Iniciar Google Chrome
driver = webdriver.Chrome();

# Navegar a www.docusign.com
driver.get("https://www.docusign.com");

driver.delete_all_cookies();
time.sleep(3);

button_cookies = driver.find_element(By.ID,'onetrust-accept-btn-handler');
button_cookies.click();
time.sleep(3);

button_try = driver.find_element(By.CLASS_NAME,'css-x91yru.ep5kedm0');
button_try.click();
time.sleep(3);

input_email = driver.find_element(By.ID,'email');
input_email.send_keys("test@test.com");

button_start = driver.find_element(By.CLASS_NAME, "css-1b2deny");
button_start.click();
time.sleep(6);

# Imprimir título y URL
print('Título: ', driver.title);
print('URL: ', driver.current_url);

# Completar campos del formulario
input_name = driver.find_element(By.ID,'fname');
input_name.send_keys("Jhon");
time.sleep(1);
input_lname = driver.find_element(By.ID,'lname');
input_lname.send_keys("Smith");
time.sleep(1);
input_phone = driver.find_element(By.ID,'phone');
input_phone.send_keys("123123");
time.sleep(1);

button_validate = driver.find_element(By.CLASS_NAME, "css-u170zz");
button_validate.click();
time.sleep(6);

# Validar título y URL
print('Título: ', driver.title);
print('URL: ', driver.current_url);
