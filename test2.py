from selenium import webdriver
from selenium.webdriver.common.by import By

# Iniciar driver de Chrome
driver = webdriver.Chrome();

# Navegar a posadas.lastipas.com.ar
driver.get("https://posadas.lastipas.com.ar");
driver.implicitly_wait(5)

movies_list = driver.find_elements(By.ID, 'listaCartelera');
movie = driver.find_elements(By.CLASS_NAME, 'col-sm-6');

for movie in movies_list:
    print(movie.text);

driver.quit();