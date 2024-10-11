#p19.py
#Jose Melgar
#9/22/2024
#Python 3.12.5
#program  which asks the user for an integer  X. The program then outputs the values from 1  to 1000 as X numbers per line

x = int(input("Enter a number between 10 and 30: "))

if 10 <= x <= 30:
    print(f"Showing values 1 - 1000, with {x} number by line:")
    for i in range(1, 1001):
        print(f"{i:4d}", end=' ')
        if i % x == 0:
            print()
else:
    print("The numbers per line must be between 10 and 30.")


   

"========== RESTART: C:\Users\janth\Desktop\phyton class\class4\p19.py =========="
"Enter a number between 10 and 30: 12"
"Showing values 1 - 1000, with 12 number by line:"
"   1    2    3    4    5    6    7    8    9   10   11   12 "
"  13   14   15   16   17   18   19   20   21   22   23   24 "
"  25   26   27   28   29   30   31   32   33   34   35   36 "
"  37   38   39   40   41   42   43   44   45   46   47   48 "
"  49   50   51   52   53   54   55   56   57   58   59   60 "
"  61   62   63   64   65   66   67   68   69   70   71   72 "
"  73   74   75   76   77   78   79   80   81   82   83   84 "
"  85   86   87   88   89   90   91   92   93   94   95   96 "
"  97   98   99  100  101  102  103  104  105  106  107  108 "
" continue  "
" 949  950  951  952  953  954  955  956  957  958  959  960 "
" 961  962  963  964  965  966  967  968  969  970  971  972 "
" 973  974  975  976  977  978  979  980  981  982  983  984 "
" 985  986  987  988  989  990  991  992  993  994  995  996 "
" 997  998  999 1000 "
