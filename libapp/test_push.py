from gcm import *

gcm = GCM("AIzaSyBOUrsenRnqXBuoC4uhqwS2vOxsZYUwYsI")
data = {'the_message': 'You have x new friends', 'param2': 'value2'}

reg_id = 'cY2q_1xCrUk:APA91bHHdRtaBwI9z-bfKBXHGtvNypTq3NEND8zNQUpy9E9vBCJpI2un2-NNjCoSgcRaGXR26nb-glsAIs8KHVQBO5WlTk2PlCUdW6Nzu5jmFyi60XT6A2xQJfcm2V7re8XEajRgHb1v'

gcm.plaintext_request(registration_id=reg_id, data=data)