import os.path

if os.path.isfile("phone.txt"):
    print("동일한 이름의 파일이 존재합니다.")
else:
    outfile = open("phone.txt","w")
    outfile.write("박소현 010-1234-5678\n")
    outfile.write("김철수 010-1234-5679\n")
    outfile.write("김영희 010-1234-5689")
    print('파일이 생성되었습니다.')
    outfile.close()
    
