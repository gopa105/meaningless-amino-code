sid=""
comID=""
import amino
import aminos
client=aminos.ClientSid()
'''
login
'''
client.sssid(sid=sid)
sub=amino.SubClient(comID=comID,profile=client.profile)
print(sub.get_recent_blogs(start=0,size=25).title)
