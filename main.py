from pyrogram import Client, filters
from server import keep_alive
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Telegram API credentials
api_id = int(os.getenv("API_ID", "9193752"))  # Render pe environment variables use karna better hai
api_hash = os.getenv("API_HASH", "0f6b6ad425a7583b52193fbac0951254")
bot_token = os.getenv("BOT_TOKEN", "7579326245:AAHTZ1vimdjVTItEJuBB0viCYX57Ezqq-7g")

# Snapchat credentials
snapchat_username = os.getenv("yappuyadav")
snapchat_password = os.getenv("Suhaib.192123")

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Selenium Headless Chrome Setup
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--remote-debugging-port=9222")

# Render ke liye Custom Chrome aur Chromedriver path
chrome_options.binary_location = "/usr/bin/google-chrome"
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("Bot is Running 24/7!")
@app.on_message(filters.video & filters.private)
async def upload_to_spotlight(client, message):
    file_path = await client.download_media(message.video)
    file_path = os.path.abspath(file_path)  # Ensure absolute path
    await message.reply(f"Video mil gaya: {file_path}")

    try:
        # Open Snapchat
        driver.get("https://my.snapchat.com")
        time.sleep(3)

        # Login
        driver.find_element(By.ID, "username").send_keys(snapchat_username)
        driver.find_element(By.ID, "password").send_keys(snapchat_password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)  

        # Navigate to Spotlight Upload
        driver.get("https://my.snapchat.com/spotlight")
        time.sleep(3)

        # Upload Video
        upload_input = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_input.send_keys(file_path)
        time.sleep(5)  

        # Post Video
        driver.find_element(By.XPATH, "//button[text()='Post to Snapchat']").click()
        time.sleep(5)

        await message.reply("Video Snapchat Spotlight pe chadh gaya, bhai! Check kar le!")

    except Exception as e:
        await message.reply(f"Koi error aaya bhai: {str(e)}")

    finally:
        driver.quit()
keep_alive()
app.run()
