from datetime import datetime

today = datetime.now()
date_time = today.strftime('%Y-%m-%H-%M-%S')
print(date_time)