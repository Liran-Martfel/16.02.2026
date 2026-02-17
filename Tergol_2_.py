nums = [7,1,9,2,2,10]
words = ['banana','kiwi','apple','fig','watermelon']
nums.sort()
print(nums)
print (sorted(words))
print (sorted(words, key=len))
print (sorted(words, key=len, reverse=True))

