from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5160588554:AAFNJkLlkprb1hrQBt2kHFI7-NN5s5MByXc"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001241675729,-1001881627229,-1001860656056,-1001877280212]# List of chat id's to forward messages from.
    TO_CHATS = [-1001971427097]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
