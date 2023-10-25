import csv

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

all_data = []
with open("TQQQ.csv", "r" ) as theFile:
    reader = csv.DictReader(theFile)
    for line in reader:
        all_data.append(line)

def cal_profit(buy_quota, sell_quota, tasor, wait_buy_qu, wait_sell_qu):
    last_price = 0
    wait_buy = 0
    wait_sell = 0

    current_day = 0
    newMoney = 100000
    for line in all_data:
        #print("收市:"+line["Close"])
        current_price = all_data[current_day]["Close"]
        low_7_day = all_data[current_day]["Low"]
        high_7_day = all_data[current_day]["High"]
        if current_day > tasor:
            for i in range(tasor):
                if all_data[current_day-i]["Low"] < low_7_day:
                    low_7_day = all_data[current_day-i]["Low"]
                if all_data[current_day-i]["High"] > high_7_day:
                    high_7_day = all_data[current_day-i]["High"]
                #print("day "+str(current_day-i)+": "+all_data[current_day-i]["Low"])
        if(float(current_price)/float(high_7_day) <0.95) and sell_quota > 0 and wait_sell <= 0:
            prRed("日期:"+line["Date"]+", "+str(float(current_price)*sell_quota*100*8+newMoney)+", 現價: "+str(all_data[current_day]["Close"])+"(賣), 賺: "+str(float(current_price)-float(last_price))+", 7天最高: "+str(high_7_day)+", 7天最低: "+str(low_7_day)+"7日最高位下跌了LOW:"+str(float(current_price)/float(low_7_day))+"7日最高位下跌了HIGH:"+str(float(current_price)/float(high_7_day)))
            last_price = current_price
            buy_quota += 1
            sell_quota -= 1
            wait_sell = wait_buy_qu
            newMoney += float(all_data[current_day]["Close"])*100*8
        elif(float(current_price) > float(low_7_day)*1.05) and buy_quota > 0 and wait_buy <= 0:
            prGreen("日期:"+line["Date"]+", "+str(float(current_price)*sell_quota*100*8+newMoney)+", 現價: "+str(all_data[current_day]["Close"])+"(買), 7天最高: "+str(high_7_day)+", 7天最低: "+str(low_7_day)+"7日最高位下跌了LOW:"+str(float(current_price)/float(low_7_day))+"7日最高位下跌了HIGH:"+str(float(current_price)/float(high_7_day)))
            last_price = current_price
            sell_quota += 1
            buy_quota -= 1
            wait_buy = wait_sell_qu
            newMoney -= float(all_data[current_day]["Close"])*100*8
        else:
            print(" 日期:"+line["Date"]+", "+str(float(current_price)*sell_quota*100*8+newMoney)+", 現價: "+str(all_data[current_day]["Close"])+", 7天最高: "+str(high_7_day)+", 7天最低: "+str(low_7_day)+"7日最高位下跌了LOW:"+str(float(current_price)/float(low_7_day))+"7日最高位下跌了HIGH:"+str(float(current_price)/float(high_7_day)))
        wait_buy-=1
        wait_sell-=1
        current_day += 1

    final_value = float(current_price)*sell_quota*200*8+newMoney
    return final_value

print(cal_profit(4, 0, 15, 17, 8))
#for buy_quota in range(6):
#    for tasor in range(21):
#        for wait_buy_qu in range(21):
 #           for wait_sell_qu in range(21):
 #               result = cal_profit(buy_quota+1, 0, tasor, wait_buy_qu, wait_sell_qu)
#                if result > 200000:
 #                   print(f"cal_profit({buy_quota+1}, {tasor}, {wait_buy_qu}, {wait_sell_qu}) = {result}")