from selenium import webdriver

# Iniciar driver de Chrome
driver = webdriver.Chrome();

# Navegar a posadas.lastipas.com.ar
driver.get("https://posadas.lastipas.com.ar");

# Maximizar la ventana
driver.maximize_window();

# Imprimir el título y la URL
print("Título de la página:", driver.title);
print("URL de la página:", driver.current_url);

# Cerrar la ventana
driver.quit()
