from selenium import webdriver
from selenium.webdriver.common.by import By

# Iniciar driver de Chrome
driver = webdriver.Chrome();

# Navegar a posadas.lastipas.com.ar
driver.get("https://posadas.lastipas.com.ar");

# Se espera a que cargue la pagina 5s
driver.implicitly_wait(5)

# Se selecciona la lista contenedora de peliculas
movies_list = driver.find_elements(By.ID, 'listaCartelera');
movie = driver.find_elements(By.CLASS_NAME, 'col-sm-6');

# Se itera la lista de elementos para imprimir cada uno de ellos
for movie in movies_list:
    print(movie.text);

# Cerrar la ventana
driver.quit();
