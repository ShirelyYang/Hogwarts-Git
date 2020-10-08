from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = "Android"
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = "emulator-5554"
desired_caps['appPackage'] = "com.xueqiu.android"
desired_caps['appActivity'] = ".view.WelcomeActivityAlias"
desired_caps['dontStopAppOnReset'] = 'true'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.find_element(By.ID, "com.xueqiu.android:id/tv_search").click()
driver.find_element(By.ID, "com.xueqiu.android:id/search_input_text").send_keys("alibaba")
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]").click()
driver.back()
driver.quit()