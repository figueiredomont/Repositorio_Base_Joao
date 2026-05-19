import pyautogui as pg

pg.mouseInfo

pg.moveTo(100,150, duration=1.5)
pg.moveTo(100,150, duration=1.5)

pg.press("win")

pg.sleep(1)

pg.write("chrome", interval= 0.5)

pg.press("enter")
pg.sleep(2)
pg.write("www.youtube.com")
pg.press('enter')


pg.moveTo(702,119, duration=1)
pg.sleep(4)
pg.click()

pg.write("drake - Massive ", interval=0.5)
pg.press("enter")

pg.moveTo(685,703)
pg.click()
