def trains_cancelled( tb_trn, lr_trn):
    m = 0
    tbt = list()
    lrt = list()
    i = 0
    for ele in tb_trn:
        temp = list()
        temp.append(ele)
        temp.append(0)
        tbt.append(temp)
    for elem in lr_trn:
        temp = list()
        temp.append(0)
        temp.append(elem)
        lrt.append(temp)
    while i != 102:
        i = i + 1
        cancel_dict = dict()
        for p in range(len(tbt)):
            tbt[p][1] = i
            if str(tbt[p]) not in cancel_dict.keys():
                cancel_dict[str(tbt[p])] = 0
            else:
                m += 1
        for z in range(len(lrt)):
            lrt[z][0] = i
            if str(lrt[z]) not in cancel_dict.keys():
                cancel_dict[str(lrt[z])] = 0
            else:
                m += 1

    print(m)


if __name__ == "__main__":
    tb_trains = list()
    lr_trains = list()
    tb = int(input('no. of trains from top to bottom:'))
    lr = int(input('no. of trains from left to right:'))
    for x in range(tb):
        t = int(input('enter the train no. for top to bottom:'))
        tb_trains.append(t)
    print()
    for y in range(lr):
        t1 = int(input('enter the train no. for left to right:'))
        lr_trains.append(t1)
    trains_cancelled(tb_trains, lr_trains)
