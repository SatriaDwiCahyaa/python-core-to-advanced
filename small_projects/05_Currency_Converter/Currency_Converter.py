"""
Currency Converter 
Author: Satria Dwi Cahya
Purpose: understand how to troubleshoot input errors and mathematical logic for currency conversion
"""


def ClearScreen():
    import os
    os.system('cls')

def KonversiPerantara(amount, source_currency):
    if source_currency == 'IDR':
        usd = amount * 0.000059
        return usd
    elif source_currency == 'AUD':
        usd = amount * 0.67
        return usd
    elif source_currency == 'USD':
        return amount
    
def KonversiKeTujuan(amountUSD, target_currency):
    if  target_currency == 'IDR':
        idr = amountUSD * 16724.70
        return idr
    elif target_currency == 'AUD':
        aud = amountUSD * 1.49
        return aud
    elif target_currency == 'USD':
        return amountUSD



currency = ('IDR', 'USD', 'AUD')

while True:
    ClearScreen
    amount = float(input('Enter the amount: ').strip())
    
    if (amount > 0):        
        
        source_currency = input('Source currency (IDR, USD, AUD): ').strip().upper()
        if source_currency not in currency:
            print('Wrong Input!')
            break
        target_currency = input('Target currency (IDR, USD, AUD): ').strip().upper()
        
        if (source_currency not in currency) and (target_currency not in currency) :
            print('Wrong Input!')
            break
        else:
            if source_currency == target_currency:
                print(f'{amount} {source_currency} is equal to {amount} {target_currency}')
            else:
                HasilKonversikeUSD = KonversiPerantara(amount, source_currency)
                Konversi_MataUang = KonversiKeTujuan(HasilKonversikeUSD, target_currency)
                print(f'{amount} {source_currency} is equal to {round(Konversi_MataUang, 2)}')
    else:
        print('Wrong input!')
        continue


    next_convert = input('Next Currency Converter? (Y/N): ').strip().upper()
    if next_convert == 'N': 
        break

