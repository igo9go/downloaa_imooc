import os,sys,string
import time

def view_bar(num=1, sum=100, bar_word=":"):
	rate = float(num) / float(sum)
	rate_num = int(rate * 100)
	print '\r%d%% :' %(rate_num)

	for i in range(0, num):
		os.write(1, bar_word)
	sys.stdout.flush()

if __name__ == '__main__':
	for i in range(0, 100):
		time.sleep(0.1)
		view_bar(i, 99)
