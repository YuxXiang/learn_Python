import datetime


number = 23
guess = int(input('Enter an integer : '))

# str 和 bytes 直接转换
# s1 = 'aaa'
# s2 = str(b'aaa', 'utf-8')

s1 = bytes('aaa', encoding='utf-8')
s2 = b'aaa'

if s1 == s2:
  print(" s = bs ")

  s_dt = "2016:07:07 09:08:47"
  s_format = "%Y:%m:%d %H:%M:%S"
  d_dt = datetime.datetime.strptime(s_dt, s_format)

  print(d_dt)

  d_dt = d_dt + datetime.timedelta(days=-1)

  s_ndt = datetime.datetime.strftime(d_dt, s_format)

  print(s_ndt)



elif guess == number:
    # 新块从这里开始     
    print('Congratulations, you guessed it.') 
    print('(but you do not win any prizes!)') 
    # 新块在这里结束 
elif guess < number:
    # 另一代码块     
    print('No, it is a little higher than that') 
    # 你可以在此做任何你希望在该代码块内进行的事情 
else: 
    print('No, it is a little lower than that') 
    # 你必须通过猜测一个大于（>）设置数的数字来到达这里。 

print('Done') 
# 这最后一句语句将在 
# if 语句执行完毕后执行。

