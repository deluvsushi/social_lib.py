import requests

class SocialLib:
	def __init__(self):
		self.api = "https://lib.social"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
		self.csrf_token = self.get_csrf_token()["csrf"]

	def get_csrf_token(self):
		return requests.get(
			f"{self.api}/_refresh-token",
			headers=self.headers).json()

	def upload_image(self, file: bytes):
		data = {"file": ("image.jpg", file, "image/jpeg")}
		return requests.post(
			f"{self.api}/upload/image",
			files=data,
			headers=self.headers).json()

	def login(
			self,
			email: str,
			password: str,
			remember: str = "on"):
		data = {
			"_token": self.csrf_token,
			"from": "https://accounts.youtube.com/",
			"email": email,
			"password": password,
			"remember": remember
		}
		return requests.post(
			f"{self.api}/login",
			data=data,
			headers=self.headers).json()

	def reset_password(
			self,
			email: str,
			password: str,
			token: str):
		data = {
			"_token": self.csrf_token,
			"token": token,
			"email": email,
			"password": password,
			"password_confirmation": password
		}
		return requests.post(
			f"{self.api}/password/reset",
			data=data,
			headers=self.headers).json()

	def chat_auth(self, auth: bool = True):
		return requests.get(
			"{self.api}/chat?auth={auth}",
			headers=self.headers).json()

	def get_chat_message(self, message_id: int):
		return requests.get(
			"{self.api}/message?id={message_id}",
			headers=self.headers).json()

	def change_password(
			self,
			old_password: str,
			new_password: str):
		data = {
			"_token": self.csrf_token,
			"old_password": old_password,
			"new_password": new_password,
			"new_password_confirmation": new_password
		}
		return requests.post(
			f"{self.api}/settings/password?{self.user_id}",
			data=data,
			headers=self.headers).json()

	def get_notifications(
			self,
			page: int = 1,
			type: str = "all",
			ajax: bool = True,
			get_counts: bool = True):
		return requests.get(
			f"{self.api}notification?page={page}&type={type}&ajax={ajax}&getCounts={get_counts}",
			headers=self.headers).json()

	def get_user_bookmark(self, user_id: int):
		return requests.get(
			f"{self.api}/bookmark/{user_id}",
			headers=self.headers).json()

	def follow_user(self, user_id: int):
		data = {"follower_id": user_id}
		return requests.post(
			f"{self.api}/follow",
			data=data,
			headers=self.headers).json()

	def block_user(self, user_id: int):
		data = {"block_id": user_id}
		return requests.post(
			f"{self.api}/block",
			data=data,
			headers=self.headers).json()

	def get_discussions(
			self,
			category: str = "all",
			subscription: int = 0,
			page: int = 1,
			sort: str = "newest"):
		return requests.get(
			f"{self.api}/api/forum/discussion?category={category}&subscription={subscription}&page={page}&sort={sort}",
			headers=self.headers).json()

	def search_discussion(
			self,
			title: str,
			category: str = "all",
			subscription: int = 0,
			page: int = 1,
			sort: str = "newest"):
		return requests.get(
			f"{self.api}/api/forum/discussion?category={category}&title={title}&subscription={subscription}&page={page}&sort={sort}",
			headers=self.headers).json()

	def get_user_discussions(
			self,
			user_id: int,
			subscription: int = 0,
			page: int = 1,
			sort: str = "newest"):
		return requests.get(
			f"{self.api}/api/forum/discussion?user_id={user_id}&subscription={subscription}&page={page}&sort={sort}",
			headers=self.headers).json()

	def get_subscriptions(
			self,
			page: int = 1,
			sort: str = "newest"):
		return requests.get(
			f"{self.api}/api/forum/discussion?subscription=1&page={page}&sort={sort}",
			headers=self.headers).json()

	def follow_discussion(self, discussion_id: int):
		return requests.post(
			f"{self.api}/api/forum/discussion/{discussion_id}/notification",
			headers=self.headers).json()

	def comment_discussion(self, discussion_id: int, text: str):
		data = {
			"body": {
				"ops": [
					{
						"insert": text
					}
				]
			},
			"chatter_discussion_id": discussion_id
		}
		return requests.post(
			f"{self.api}/api/forum/posts",
			data=data,
			headers=self.headers).json()

	def check_chat_online(self, users: list):
		data = {"users": users}
		return requests.post(
			f"{self.api}/chat/check-online",
			data=data,
			headers=self.headers).json()

	def search_user(self, query: str):
		return requests.get(
			f"{self.api}/search?type=user&q={query}",
			headers=self.headers).json()

	def get_updates(self, page: int = 1):
		return requests.get(
			f"{self.api}/user/updates?page={page}",
			headers=self.headers).json()

	def send_message(self, text: str, before: int):
		data = {
			"text": text,
			"before": before
		}
		return requests.post(
			f"{self.api}/chat",
			data=data,
			headers=self.headers).json()

	def edit_profile(
			self,
			username: str = None,
			email: str = None,
			gender: int = 0,
			about: str = None):
		data = {
			"_token": self.csrf_token,
			"gender": gender
		}
		if username:
			data["username"] = username
		if email:
			data["email"] = email
		if about:
			data["about"] = about
		return requests.post(
			f"{self.api}/user/{self.user_id}/save",
			data=data,
			headers=self.headers).json()

	def edit_comment(self, comment_id: int, text: str):
		data = {
			"body": {
				"ops": [
					{
						"insert": text
					}
				]
			}
		}
		return requests.put(
			f"{self.api}/api/forum/posts/{comment_id}",
			data=data,
			headers=self.headers).json()

	def delete_comment(self, discussion_id: int, post_ids: list):
		data = {
			"postIds": post_ids,
			"chatter_discussion_id": discussion_id
			}
		return requests.delete(
			f"{self.api}/api/forum/posts",
			data=data,
			headers=self.headers).json()

	def get_discussion(self, discussion_id: int):
		return requests.get(
			f"{self.api}/api/forum/discussion/{discussion_id}",
			headers=self.headers).json()

	def lock_discussion(self, discussion_id: int):
		data = {"actionType": "locked"}
		return requests.post(
			f"{self.api}/api/forum/discussion/{discussion_id}/action",
			data=data,
			headers=self.headers).json()

	def create_discussion(
			self, 
			title: str, 
			description: str, 
			category_id: int,
			yaoi: bool = False,
			image: str = None):
		data = {
			"title": title,
			"body": {
				"ops": [
					{
						"insert": {
							"image": {
								"src": "https://lib.social/forum/undefined",
								"width": 0,
								"height": 0
							}
						}
					},
				{
					"insert": description
				}
			]
		},
		"chatter_category_id": category_id,
		"yaoi": yaoi
		}
		if image:
			data["body"]["ops"][0]["insert"]["image"]["src"] = image
		return requests.post(
			f"{self.api}/api/forum/discussion",
			data=data,
			headers=self.headers).json()
