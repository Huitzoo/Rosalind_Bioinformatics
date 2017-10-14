def main():
    months = int(input('Enter the months'))
    litters = int(input('Enter the number of litters'))
    fibo = [1,1]
    if months <= 2:
        print('1')
    else:
        for i in range(2,months):
            fibo.append(litters*fibo[i-2]+fibo[i-1])
    print(fibo)
main()
