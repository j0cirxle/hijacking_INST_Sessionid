import asyncio
import websockets
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Selenium 설정
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/")

T = True

# 🟢 ping 전송 (keep-alive용)
async def keep_alive(websocket):
    while True:
        try:
            await websocket.send("ping")
            print(">>> Sent ping")
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Ping failed: {e}")
            break

# 🟢 메시지 전송 함수
async def send_message():
    uri = "ws://yourIP"
    async with websockets.connect(uri) as websocket:
        # 🔁 keep-alive task 실행
        asyncio.create_task(keep_alive(websocket))

        # 첫 메시지 테스트
        message = "Test send"
        print(f"Sending message: {message}")
        await websocket.send(message)

        response = await websocket.recv()
        print(f"Received response: {response}")

        cookies = driver.get_cookies()
        print("Cookies:")
        for cookie in cookies:
            print(f"Name: {cookie['name']}, Value: {cookie['value']}")

        # sessionid 찾기 루프
        while T:
            for cookie in cookies:
                message = f"{cookie['name']}={cookie['value']}"

                if "sessionid" in cookie['name']:
                    await websocket.send(message)

                    print(f">>> Sent sessionid cookie: {message}")
                    response = await websocket.recv()
                    print(f"<<< Received response: {response}")

                    driver.quit()
                    return  # or break if you want to keep_alive

            cookies = driver.get_cookies()
            await asyncio.sleep(2)

        await asyncio.Future()  # keep alive 유지

if __name__ == "__main__":
    asyncio.run(send_message())
