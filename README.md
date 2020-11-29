# VKpoc - VK piece of code
Простые и быстрые функции для работы с API ВКонтакте стандартными библиотеками Python. Все функции разделяются строго по функционалу.

# Как это работает
1. Создаете приложение в консоли разработчика ВКонтакте.
2. Получаете access_token для вашего приложения используя официальную документацию API ВКонтакте (https://vk.com/dev/manuals), а так же ID группы и версию API ВКонтакте.
2. Используете необходимую функцию для решения определенной задачи.

# Какие функции существуют
1. vkpoc_wp_im() - Публикация поста на стене группы (сообщества) с изображением(ями) и сообщением.

# vkpoc_wp_im()
```
vkpost_id = vkpoc_wp_im('access token', 'group id', 'vk api version', (image,), 'Post message')
print(vkpost_id)
>>> 1843
```

При успешной публикации функция возвращает строку ID нового поста на стене группы (сообщества)
