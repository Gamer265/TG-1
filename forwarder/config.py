from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5160588554:AAFNJkLlkprb1hrQBt2kHFI7-NN5s5MByXc"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001792784756,-1001366147158,-1001169241764,-1001721377011,-1001241675729,-1001881627229,-1001860656056,-1001877280212,-1001502705198,-1001749139811,-1001688333632,-1001797256809]# List of chat id's to forward messages from.
    TO_CHATS = [-1001623801020]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 32
   
    
