# 🔮 Heroku Dyno Switcher

Another Heroku dyno Switcher for you.

## ⚙️ Usage/Examples

This is example of JSON, if u want add more app, don't forget to add JSON object like examples below.

```add JSON format like below to github secret with name DATAS or clone this repository and put your api key & app name into datas.json ```

```JSON
{
	"datas": [
		{
			"proc": "web",
			"app": {
				"api_a":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
				"name_a":"app1_a",
				"api_b":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
				"name_b":"app1_b"
			}
		},
		{
			"proc": "web",
			"app": {
				"api_a":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
				"name_a":"app2_a",
				"api_b":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
				"name_b":"app2_b"
			}
		}
	]
}
```

## 😎 Authors

- [@noobzhax](https://www.github.com/noobzhax)

## 💡 Inspiration & References

 - [HerokuDynoSwitcher](https://github.com/tiararosebiezetta/HerokuDynoSwitcher) for my Inspiration.
 - [HEROKU3 PIP](https://pypi.org/project/heroku3/) Heroku library for python.
 - [HEROKU](https://heroku.com) for best free service.

