# telegram-tracker
Mini version Telegram tracker, to found a site https://discord-tracker.com/, a design from https://marketplace.tonnel.network/


<h1>Installation</h1>

1. After cloning the repository, you need to install the necessary libraries. For this, specify **pip install -r requirements.txt**
2. In the file **settings.py** find the **TELEGRAM_BOT_TOKEN** variable and paste your bot's token there (obtained from @BotFather)
3. Next, using the ngrok utility or another technology for transferring from the local network to the global network, get the domain and paste your domain into @BotFather **/setdomain**.
4. Then go to the website https://core.telegram.org/widgets/login register your bot there, select the redirect URL and replace the resulting JS code with what is in the file. login/templates/login/index.html <script></script>
