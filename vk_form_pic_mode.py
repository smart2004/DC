import datetime
import os
from dotenv import load_dotenv
from social_spam import Vkontakte


load_dotenv()
token = os.getenv('TOKEN')
vk = Vkontakte()
vk.connect_user(token)

file1 = open(r"test_ids.txt", "r")
vkids = []
lines = file1.readlines()

count = 0
for line in lines:
    vkids.append(line.strip())

try:
    for one in vkids:
        try:
            vk.send_message(int(
                one), image='alfa.jpg', message='В Альфа-Банке дают 500 ₽, если оформишь Альфа-Карту по моей ссылке. Она бесплатная, с суперкэшбэком до 100% каждый месяц и ещё до 30% в категориях на выбор. Вот моя ссылка: \n https://alfa.me/u9zEEo')
            with open("test_ids_actual.txt", "a") as myfile:
                myfile.write(f'{one} \n')
            count += 1
        except Exception as e:
            print(f"An error occurred for id {one}: {str(e)}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
myfile.close()

filename = 'test_ids_actual.txt'
date = datetime.datetime.now().strftime('%Y-%m-%d')
time = datetime.datetime.now().strftime('%H-%M-%S')
new_filename = f'ids{date}+{time}.txt'
os.rename(filename, new_filename)
print(f'File renamed to {new_filename}')

print("Sent qty: ", count)

file1.close()

os.remove(r'test_ids.txt')
