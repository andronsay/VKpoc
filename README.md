# VKpoc - vk api, вконтакте, vkontakte, python
VKpoc (VK piece of code) - это простые и быстрые функции для работы с API ВКонтакте стандартными библиотеками Python. Все функции разделяются строго по функционалу.

# Как это работает
1. Создаете приложение в консоли разработчика ВКонтакте.
2. Получаете access_token для вашего приложения используя официальную документацию API ВКонтакте (https://vk.com/dev/manuals), а так же ID группы и версию API ВКонтакте.
2. Используете необходимую функцию для решения определенной задачи.

# Какие функции существуют
1. vkpoc_wp_im() - Публикация поста на стене группы (сообщества) с изображением(ями) и сообщением.

# vkpoc_wp_im()
Пример
```
vkpost_id = vkpoc_wp_im('04b0b956c9f1ad40100c154b477131ce57d0f491576f15151c6d7184b1874719b6c5030353250c9b722d6', '156078919', '5.126', ('/var/www/public_html/images/16050917615fabc1b1e98695.10183423344.jpg','/var/www/public_html/images/16050917615fabc1b1e98695.10183423344.jpg'), 'Post message')
print(vkpost_id)
>>> 1843
```
При успешной публикации функция возвращает строку ID нового поста на стене группы (сообщества)
