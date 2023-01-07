import telegram
import os
# Get TOKEN from environment variable
TOKEN = os.environ.get('TOKEN')
print(TOKEN)
#Define main function
def main():
 
    WEBHOOK_URL = 'https://echo1bot-wphitu67ya-uc.a.run.app/'
    #Create an instance of the telegram.Bot class
    bot = telegram.Bot(token=TOKEN)
    # #Delete webhook
    print(bot.deleteWebhook())
    # #Set webhook
    print(bot.setWebhook(WEBHOOK_URL))
    #Check if webhook is set
    print(bot.getWebhookInfo())

#Run main function
if __name__ == '__main__':
    main()