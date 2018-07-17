from selenium import webdriver
from selenium.webdriver import ActionChains

def test_dragNdrop():
    driver = webdriver.Chrome("DriverJars/chromedriver.exe")
    driver.maximize_window()
    driver.get("http://jqueryui.com/resources/demos/droppable/default.html");
    source = driver.find_element_by_xpath(".//*[@id='draggable']")
    destination = driver.find_element_by_xpath(".//*[@id='droppable']")
    actions = ActionChains(driver)
    actions.drag_and_drop(source, destination).perform()
    assert 1 == 1
    driver.quit()
