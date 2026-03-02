def greedy_coin(uang_pecahan, total_uang):
    result = {}
    banyak_uang_pecahan_terpakai = 0
    
    for uang in uang_pecahan:
        if total_uang >= uang:
            cout = total_uang // uang

            result[uang] = cout

            total_uang -= cout * uang 

            banyak_uang_pecahan_terpakai += cout

    
    return result, banyak_uang_pecahan_terpakai

def display_output(result, total):

    for uang, indeks in result.items():
        print(f'Rp {uang:<7} : Terpakai {indeks}x')

    print('Total lembar terpakai: ', total)

def main():
    uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

    total_uang = 98000

    uang_pecahan, total = greedy_coin(uang_pecahan, total_uang)

    display_output(uang_pecahan, total)


if __name__ == "__main__":
    main()
