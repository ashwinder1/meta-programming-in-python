http_status = 201

if http_status == 200 or http_status == 201 :
    print('Success')
elif http_status == 400 :
    print('Not Found')
elif http_status == 500 or http_status == 501 :
    print ('Server Error')
else :
    print ('Unknown')

match http_status :
    case 200 | 201 : # 'or' symbol is different here --> |
        print('Success')
    case 400 :
        print('Not Found')
    case 500 | 501 :
        print('Server Error')
    case _ : # for default condition
        print('Unknown')

        