import subprocess
# import time

# for s in range(1):
setup_path = r'test_ids.py'
a_process = subprocess.Popen([setup_path])
a_process.wait()

setup_path_b = r'vk_form_pic_mode.py'
b_process = subprocess.Popen([setup_path_b])
b_process.wait()

#    time.sleep(87000)
#    s += 1
