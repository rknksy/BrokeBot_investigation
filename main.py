import datetime
import json, matplotlib.pyplot as pyplot, Data_producer
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates

def main():
    # data = Data_producer.coin_data_collect()
    # json_yazma(data)

    data = json_okuma()



    fig, ax = pyplot.subplots(figsize=(12, 6))

    ax.set(xlabel="Date",
           ylabel="Open 5dk verileri",
           title="Mana Verileri")


    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    print(data['date'][0])

    pyplot.plot(data['date'], data['open'], label = "Open")
    pyplot.plot(data['date'], data['close'], label = "Close")

    pyplot.legend()
    pyplot.grid()

    pyplot.show()


def json_okuma():
    data_loaded = json.load(open('json_data.json'))
    for index, date in enumerate(data_loaded['date']):
        data_loaded['date'][index] = datetime.datetime.strptime(date, "%m/%d/%Y, %H:%M:%S")
    return data_loaded

def json_yazma(data):
    for index, date in enumerate(data['date']):
        data['date'][index] = date.strftime("%m/%d/%Y, %H:%M:%S")

    with open('json_data.json', 'w') as outfile:
        json.dump(data, outfile)




if __name__ == '__main__':
    main()