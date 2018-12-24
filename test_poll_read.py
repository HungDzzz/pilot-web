from poll import Poll
import mlab
# 1. connect
mlab.connect()
# 2. read all
poll_list = Poll.objects()  # page  , lazy loading : ko load ngay khi can moi lay ra
# p = poll_list[0]
# print(p.question) # question cua p
# print(p.options)
for p in poll_list:
    print(p.question)
    print(p.options)
    print(p.code)
    print('*'*50)

