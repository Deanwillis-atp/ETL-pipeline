import mysql.connector
from datetime import datetime
import yfinance as yf
import json
def bring_in_data():
    data = {}
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='aggregated_stock_data'
    )
    
    cursor = db_connection.cursor()
    query = 'SELECT DISTINCT name,ddate,value FROM company_financials ;' #There was duplicate data
    cursor.execute(query)
    # values = []
    # quarters = []
    
    for name,ddate,value in cursor:
        if name not in data:
            data[name] = {'info':[[ddate,value]]}
        elif name in data:
            data[name]['info'].append([ddate,value]) 
    return data

       
            
data = bring_in_data()





def group_by_year(dta):
    group_year_dict = {}
    for name in dta:
        for data in dta[name]['info']:
            

            year = data[0].year
            date = data[0]
            value = float(data[1])

            if name not in group_year_dict:
                group_year_dict[name] = {}

            if year not in group_year_dict[name]:
                group_year_dict[name][year] = []

            group_year_dict[name][year].append([date,value])

    return group_year_dict
            
group_year = group_by_year(data)
#print(group_year)

def avgp_prec(gryear):
    avg_price_precent = {}
    entries = 0
    for name in gryear:
        for year in gryear[name]:

            spiked_num = None
            spiked_date = None
            sum_rd = []
            amount = 0

            for info in gryear[name][year]: 

                sum_rd.append((info[0],float(info[1])))
            
            prices = [i[1]for i in sum_rd]
            
            for i in prices:
                
                if i > 1:
                    
                    if len(prices) >= 3:
                        entries+=1
                        
                        max_value = max(prices)
                        avg_of_sumrd = (sum(prices) / len(prices))

                        if avg_of_sumrd > 1:
            
                            avg_without_spiked = sum(p for p in prices if p != max_value) / (len(prices) - 1)
                            if avg_without_spiked > 1:
                                prec_inc = (((max_value)-(avg_without_spiked))/(avg_without_spiked)*100)
                            

            for i in sum_rd:
                if i[1] > avg_of_sumrd:
                    amount+=1
                    spiked_num = i[1]
                    spiked_date = i[0]
            
            if name not in avg_price_precent:
                avg_price_precent[name] = {}
            if amount == 1:
                
                avg_price_precent[name][year] = [[spiked_date,spiked_num,round(prec_inc, 2)]]

                        
    return    avg_price_precent #,entries

func = avgp_prec(group_year)
filtered_data = {name: years for name, years in func.items() if years}

# print(filtered_data)


#filtered_data = {name: years for name, years in func.items() if years}

print(json.dumps((filtered_data),indent =4 ,default=str))

# def change_name_to_ticker(filt_dta):
#     for i in filt_dta:
#         print(filt_dta)
        
#     return filt_dta

# result = change_name_to_ticker(filtered_data)
# print(result)