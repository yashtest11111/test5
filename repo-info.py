# importing the reqets library
import requests
# defining the api- endpo int
API_ENDPOINT = "http://115.115.91.60:5432/train"
#API_ENDPOINT = "http://b6a5-115-119-250-30.ngrok.io/train"
# data to be sent to api
data = {
	"url": "https://github.com/yashtest11111/test5.git",
	"branch_name": "master",
	"user_name": "yash3@gmail.com"
}
# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)
# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
