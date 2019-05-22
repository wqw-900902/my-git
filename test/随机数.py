import random
def random_k(dict,target):
    # 确定随机数
    total = 0
    for k,v in dict.items():
        total += v
        if total >= target:
            return k

if __name__ == '__main__':
    dict = {"1":2,"2":3,"3":5}
    target = random.randint(0,sum(dict.values()))
    print(target,end=" ")
    print(random_k(dict,target))