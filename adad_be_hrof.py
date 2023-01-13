#mohammad hossein farahani
#class: يکشنبه 7:45

Number = int(input("adad $ raqami ra vared konid : ")) 
Yekan = Number%10
Number = int(Number/10) 
Dahgan = Number%10
Number = int(Number/10) 
Sadgan = Number%10
Number = int(Number/10) 
Hezargan = Number%10

match Hezargan: 
    case 1: 
        print("one thousand",end=" ") 
    case 2: 
        print("two thousand",end=" ") 
    case 3: 
        print("three thousand",end=" ") 
    case 4: 
        print("four thousand",end=" ") 
    case 5: 
        print("five thousand",end=" ") 
    case 6: 
        print("six thousand",end=" ") 
    case 7: 
        print("seven thousand",end=" ") 
    case 8: 
        print("eight thousand",end=" ") 
    case 9: 
        print("nine thousand",end=" ")
        
match Sadgan: 
    case 1: 
        print("one hundred",end=" ") 
    case 2: 
        print("two hundred",end=" ") 
    case 3: 
        print("three hundred",end=" ") 
    case 4: 
        print("four hundred",end=" ") 
    case 5: 
        print("five hundred",end=" ") 
    case 6: 
        print("six hundred",end=" ") 
    case 7: 
        print("seven hundred",end=" ") 
    case 8: 
        print("eight hundred",end=" ") 
    case 9: 
        print("nine hundred",end=" ") 

match Dahgan: 
    case 2: 
        print("twenty",end=" ") 
    case 3: 
        print("thirty",end=" ") 
    case 4: 
        print("forty",end=" ") 
    case 5: 
        print("fifty",end=" ") 
    case 6: 
        print("sixty",end=" ") 
    case 7: 
        print("seventy",end=" ") 
    case 8: 
        print("eighty",end=" ") 
    case 9: 
        print("ninety",end=" ")
        
if Dahgan == 1: 
    match Yekan: 
        case 0: 
            print("ten") 
        case 1: 
            print("eleven") 
        case 2: 
            print("twelve") 
        case 3: 
            print("thirteen") 
        case 4: 
            print("fourteen") 
        case 5: 
            print("fifteen") 
        case 6: 
            print("sixteen") 
        case 7: 
            print("seventeen") 
        case 8: 
            print("eighteen") 
        case 9: 
            print("nineteen")
 
else : 
    match Yekan: 
        case 1: 
            print("one") 
        case 2: 
            print("two") 
        case 3: 
            print("three") 
        case 4: 
            print("four") 
        case 5: 
            print("five") 
        case 6: 
            print("six") 
        case 7: 
            print("seven") 
        case 8: 
            print("eight") 
        case 9: 
            print("nine")
