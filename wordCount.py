import time

start_time = time.time()
file = open('E:\OneDrive\Desktop\pg100.txt',"r+")
wordCount = {}
for word in file.read().split():
	if word not in wordCount:
		wordCount[word] = 1
	else:
		wordCount[word] += 1
for key in wordCount.keys():
	print(key,'',wordCount[key])
file.close()
print ("---%s seconds ---" % (time.time() - start_time))