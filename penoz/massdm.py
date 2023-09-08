def massdm(headers):
    cheneel = requests.get("https://discord.com/api/v9/users/@me/channels",headers=headers).json()
    for channel in cheneel:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',headers=headers,json={'content':mesage})           
            print('Channel Id:'+channel[id])
        except Exception as e:
            print(f'Failed to send message, error: {e}')
    print(cheneel)
