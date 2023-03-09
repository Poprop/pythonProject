def minimal(l):
    min_number = l[0]
    for el in l:

        if el < min_number:
            min_number = el

            print(min_number)
    return  min_number

nums1 = [73 , 5 , 6 , 7]
min1= minimal(nums1)
#min = nums1 [0]

#for el in nums1:
    #if el < min:
        #min = el

#print(min)

nums2 = [7.3 , 5.4 , 6.3 , 7.3 ]
min2= minimal(nums2)
#min2 = nums2[0]

#for el in nums2:
    #if el < min:
        #min2 = el

#print(min2)

if min1<min2:
    print(min1)
else:print(min2)